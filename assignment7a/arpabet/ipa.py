from .utils import ipa_word
import re
import pronouncing


def ipa(text):
    ret = []

    for token in re.findall(r"\w+", text):
        token_low = token.lower()
        pronunciation = pronouncing.phones_for_word(token_low)

        if pronunciation:
            ret.append(ipa_word(pronunciation[0]))
        else:
            ret.append('?' * len(token_low))

    return " ".join(ret)


def ipafile(filename):
    input_file = open(filename)
    output_file = open('ipa_' + filename, 'w')

    for line in input_file:
        ipa_line = ipa(line)
        output_file.write(ipa_line + "\n")

    # Closing of files not really necessary, but still.
    input_file.close()
    output_file.close()
