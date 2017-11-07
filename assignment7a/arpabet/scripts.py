from sys import argv, exit
from .ipa import ipafile


def ipa_file():
    if len(argv) != 2:
        print("Usage: ipa_file FILENAME.")
        exit(1)

    ipafile(argv[1])
