import re


def tokenize(text):
    return re.findall(
        r"\w+['‘`´]?\w+|[.,:;!¡?-–—]",
        text,
        re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL
    )
