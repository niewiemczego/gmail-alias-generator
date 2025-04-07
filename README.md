# gmail-alias-generator

A web application built with FastAPI and vanilla JavaScript to generate Gmail aliases using the "dot trick" and "plus trick". This allows you to create variations of your Gmail address that all deliver to your main inbox, useful for signing up for different services or tracking sources.

## Features

*   **Web Interface:** Simple UI to input your email and select generation options.
*   **Dot Trick Generation:** Generates aliases by inserting dots (`.`) between characters in the username part (e.g., `user.name@gmail.com`).
*   **Plus Trick Generation:** Generates aliases by adding a plus (`+`) followed by a tag to the username part (e.g., `username+tag@gmail.com`). (Currently includes basic examples).
*   **Configurable Results:** Choose the number of aliases displayed per page (128, 256, ..., 4096).
*   **Pagination:** Navigate through generated aliases using "Previous" and "Next" buttons.
*   **Copy Results:** Easily copy the list of aliases displayed on the current page to your clipboard.
*   **FastAPI Backend:** Efficient asynchronous backend handling requests.
*   **Client-Side Rendering:** Results and pagination are handled dynamically using JavaScript `fetch`.

## Technology Stack

*   **Backend:** Python, FastAPI, Uvicorn, Pydantic
*   **Frontend:** HTML, CSS, Vanilla JavaScript

## Setup and Installation

Follow these steps to get the application running locally.

### Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package installer)
*   Git (for cloning the repository)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/niewiemczego/gmail-alias-generator.git
    cd gmail-alias-generator
    ```

2.  **Create and activate a virtual environment:** (Recommended)
    *   **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the FastAPI server using Uvicorn:**
    Assuming your main Python file (containing `app = FastAPI()`) is named `main.py` and located inside a package directory like `gmail_alias_generator`:
    ```bash
    uvicorn gmail_alias_generator.main:app --host 127.0.0.1 --port 8000
    ```
    *   If `main.py` is in the project root directory, use:
        ```bash
        uvicorn main:app --host 127.0.0.1 --port 8000
        ```

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1.  Enter your base Gmail address in the input field.
2.  Select whether to generate aliases using the "dot trick" and/or the "plus trick" using the checkboxes.
3.  Choose the desired number of aliases to display per page from the dropdown.
4.  Click the "Generate" button.
5.  The application will display the total number of aliases found and the first page of results.
6.  Use the "Prev" and "Next" buttons to navigate through the pages of results.
7.  Click the "Copy All" button to copy the aliases currently displayed on the page to your clipboard (separated by newlines).

<img width="1549" alt="Screenshot 2025-04-07 at 01 21 19" src="https://github.com/user-attachments/assets/3324cb79-9c07-4da3-ae2e-3c47d665858b" />


