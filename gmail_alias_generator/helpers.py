from itertools import combinations


def generate_all_aliases(email: str) -> list[str]:
    max_dots = len(email.split("@")[0]) - 1
    current_dots = 0

    email_aliases = []
    while current_dots <= max_dots:
        email_aliases.extend(_generate_combinations_for(email, max_dots, current_dots))
        current_dots += 1

    return email_aliases


def _generate_combinations_for(email: str, max_dots: int, current_dots: int) -> list[str]:
    combinations_indexes = combinations(range(1, max_dots + 1), current_dots)
    # i.e.: for word 'tymek' its (4 after current_dots) cuz we got 4 places where we can put the dot

    aliases = []
    for combination_indexes in combinations_indexes:
        new_alias = ""
        for i, char in enumerate(email):
            if i in combination_indexes:
                new_alias += "."
            new_alias += char

        aliases.append(new_alias)

    return aliases
