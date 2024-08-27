import re


def is_exclude(request, exclude):
    for pattern in exclude:
        if re.fullmatch(pattern, request.path):
            return True
    return False


def is_exclude_not_strong(request, exclude):
    for pattern in exclude:
        if re.search(pattern, request.path):
            return True
    return False