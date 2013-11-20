import itertools
import random
import re

VOWELS = "aeiou"
RE_VOWEL = re.compile("[%s]" % VOWELS)
#http://stackoverflow.com/a/6733563
#http://stackoverflow.com/a/13280796
def random_uppers(string):
	upperlist =[]
	l = len(string)
	newstring=string
	rand_index = random.sample(xrange(l), l-1)
	for r in rand_index:
		newstring = newstring[:r]+newstring[r].upper()+newstring[r+1:]
		upperlist.append(newstring)
	return upperlist


def random_repeats(string):
	randomlist=[]
	l= len(string)
	for i in range(len(string)):
		dups =[]
		pick =string[i]
		for j in range(0,l):
			newstring=""
			newstring=string[:i]+pick*j+string[i:]
			dups.append(newstring)
			randomlist.append(dups)
	merged = list(itertools.chain(*randomlist))
	return merged

def helper(parts):
    if len(parts) == 1:
        yield parts[0]
    else:
        for vowel in VOWELS:
            for item in helper([vowel.join(parts[:2])] + parts[2:]):
                yield item

def misplet_vowels(word):
	parts = re.split(RE_VOWEL, word)
	return list(helper(parts))	

def main():
	print "Enter a string to validate"
	word=raw_input("> ").lower()
	suggests =[]
	test_uppers = random_uppers(word)
	test_repeats = random_repeats(word)
	test_mispelt_vowels = misplet_vowels(word)
	for item in itertools.chain(test_uppers,test_repeats,test_mispelt_vowels):
		suggests.append(item)
	print "Generated test cases"
	print suggests
	return suggests
	#print withuppers
if __name__ == '__main__':
    main()