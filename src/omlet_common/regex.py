import re


def validate_email(string: str) -> bool:
    regex = re.compile(r'[A-Za-z0-9_.]+@[A-Za-z]+(\.[A-Z|a-z]{2,})+')
    return bool(regex.fullmatch(string))
