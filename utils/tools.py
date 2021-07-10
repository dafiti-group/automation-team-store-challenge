import re


def only_numbers(string: str) -> str:
    pattern = r'\D'
    return re.sub(pattern, '', string)
