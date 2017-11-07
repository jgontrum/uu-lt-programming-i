import re
from . import ipadict


def ipa_word(s):
    replaced = []
    s = re.sub(r"\d", "", s)
    for w in s.split():
        replaced.append(ipadict.get(w, w))
    return "".join(replaced)
