document.addEventListener('DOMContentLoaded', function () {
    const generateBtn = document.getElementById('generateButton');
    const emailInput = document.getElementById('emailInput');
    const dotCheckbox = document.getElementById('dotTrick');
    const plusCheckbox = document.getElementById('plusTrick');
    const aliasesSelect = document.getElementById('aliasesPerPage');
    const outputArea = document.getElementById('outputArea');
    const aliasesInfoText = document.getElementById('aliasesInfoText');
    const paginationControls = document.getElementById('paginationControls');
    const copyAllButton = document.getElementById('copyAllButton');

    let currentRequestData = {};
    let currentPage = 1;
    let displayedAliases = [];

    function fetchAndDisplayAliases(page) {
        outputArea.textContent = 'Loading...';
        aliasesInfoText.textContent = '';
        paginationControls.innerHTML = '';
        copyAllButton.disabled = true;
        displayedAliases = [];

        const isNewGeneration = page === 1 && !Object.keys(currentRequestData).length;
        if (isNewGeneration || page === 1) {
            currentRequestData = {
                email: emailInput.value,
                use_dot: dotCheckbox.checked,
                use_plus: plusCheckbox.checked,
                aliases_per_page: parseInt(aliasesSelect.value, 10)
            };
        }

        if (!currentRequestData.use_dot && !currentRequestData.use_plus) {
            outputArea.textContent = 'Please select at least one generation method (dot or plus)';
            aliasesInfoText.textContent = '';
            copyAllButton.disabled = true;
            return;
        }

        const dataToSend = { ...currentRequestData, page: page };
        currentPage = page;

        fetch('/generate-aliases', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        })
            .then(response => {
                if (!response.ok) {
                    return response.json()
                        .then(err => { throw new Error(err.error || `Error: ${response.status}`) })
                        .catch(() => { throw new Error(`Server Error: ${response.status}`) });
                }
                return response.json();
            })
            .then(data => {
                displayedAliases = data.aliases || [];

                if (data.pagination && data.pagination.total_aliases >= 0) {
                    aliasesInfoText.innerHTML = `<strong>Page ${data.pagination.page} out of ${data.pagination.total_pages} (total email aliases: ${data.pagination.total_aliases}):</strong><br>`;
                } else {
                    aliasesInfoText.textContent = '';
                }

                if (displayedAliases.length > 0) {
                    outputArea.innerHTML = displayedAliases.join('<br>');
                    copyAllButton.disabled = false;
                } else {
                    outputArea.textContent = (currentRequestData.use_dot || currentRequestData.use_plus) ? 'No aliases found for this page or criteria' : '';
                    copyAllButton.disabled = true;
                }

                renderSimplePagination(data.pagination);
            })
            .catch(error => {
                console.error('Error lol:', error);
                aliasesInfoText.textContent = `Error: ${error.message}`;
                outputArea.textContent = '';
                paginationControls.innerHTML = '';
                copyAllButton.disabled = true;
                displayedAliases = [];
                currentRequestData = {};
            });
    }

    function renderSimplePagination(paginationInfo) {
        paginationControls.innerHTML = '';

        if (!paginationInfo || paginationInfo.total_pages <= 1) {
            return;
        }

        const { page, total_pages } = paginationInfo;

        const prevButton = document.createElement('button');
        prevButton.textContent = '« Prev';
        prevButton.classList.add('page-item');
        prevButton.disabled = page <= 1;
        prevButton.addEventListener('click', () => fetchAndDisplayAliases(page - 1));
        paginationControls.appendChild(prevButton);

        const nextButton = document.createElement('button');
        nextButton.textContent = 'Next »';
        nextButton.classList.add('page-item');
        nextButton.disabled = page >= total_pages;
        nextButton.addEventListener('click', () => fetchAndDisplayAliases(page + 1));
        paginationControls.appendChild(nextButton);
    }

    copyAllButton.addEventListener('click', function () {
        if (displayedAliases.length === 0) {
            return;
        }

        const textToCopy = displayedAliases.join('\n');
        const originalButtonText = copyAllButton.textContent;

        navigator.clipboard.writeText(textToCopy)
            .then(() => {
                copyAllButton.textContent = 'Copied!';
                console.log('Aliases copied to clipboard');
                setTimeout(() => {
                    copyAllButton.textContent = originalButtonText;
                }, 2000);
            })
            .catch(err => {
                copyAllButton.textContent = 'Copy Failed';
                console.error('Failed to copy aliases: ', err);
                setTimeout(() => {
                    copyAllButton.textContent = originalButtonText;
                }, 3000);
            });
    });

    generateBtn.addEventListener('click', function () {
        currentRequestData = {};
        fetchAndDisplayAliases(1);
    });
});