import random
import string
from itertools import combinations


def generate_dot_aliases(email: str) -> list[str]:
    name_part, domain = email.split("@")
    max_dots = len(name_part) - 1
    current_dots = 0

    email_aliases = []
    while current_dots <= max_dots:
        email_aliases.extend(_generate_combinations_for(name_part, max_dots, current_dots))
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


def generate_plus_aliases(email: str, qty: int) -> list[str]:
    name_part, domain = email.split("@", 1)

    email_aliases = []
    for suffix in _generate_plus_suffix(qty):
        mail_alias = f"{name_part}+{suffix}"
        email_aliases.append(mail_alias)

    return email_aliases


def _generate_plus_suffix(qty) -> list[str]:
    return ["".join(random.sample(string.ascii_lowercase, random.randint(8, 12))) for _ in range(qty)]


def generate_all_aliases(email: str) -> list[str]:
    # it should combine both so like it would be: dot email and then + suffix

    dot_aliases = generate_dot_aliases(email)
    suffixes = _generate_plus_suffix(len(dot_aliases))
    all_aliases = [
        f"{name_part_dot_alias}+{plus_suffix}" for name_part_dot_alias, plus_suffix in zip(dot_aliases, suffixes)
    ]
    return all_aliases
