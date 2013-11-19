import itertools

import re

VOWELS = "aeiou"
RE_VOWEL = re.compile("[%s]" % VOWELS)

def helper(parts):
    if len(parts) == 1:
        yield parts[0]
    else:
        for vowel in VOWELS:
            for item in helper([vowel.join(parts[:2])] + parts[2:]):
                yield item

def vowels(word):
    parts = re.split(RE_VOWEL, word)
    return list(helper(parts))	
	
def main():
	print vowels("weke")
if __name__ == '__main__':
    main()