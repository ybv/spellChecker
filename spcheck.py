import itertools
import re
import validator

VOWELS = "aeiou"
RE_VOWEL = re.compile("[%s]" % VOWELS)

def dictLoad():
	filew = open('words.txt', 'r+b')
	allwords = set() 
	for line in filew:
		allwords.add(line.strip('\n'))
	return allwords

loaded_dict = dictLoad()

def extract_unique(str):
	newset =set()
	string =""
	for s in str:
		if s not in newset:
			newset.add(s)
			string+=s
	return string

def check_presence(inputchk):
	if inputchk in loaded_dict:
		return True
	else:
		return False

def possibile_dups(dupchk):
	char_counts = []
	allowed=('aeiou')
	for k,v in itertools.groupby(dupchk):
		if len(list(v)) >= 2:
			char_counts.append([k, 2])
		else:
			char_counts.append([k, 1])
	return rec_dubz('', char_counts, allowed=allowed)


def rec_dubz(prev, seq, allowed='aeiou'):
    if not seq:
        return [prev]
    solutions = rec_dubz(prev + seq[0][0], seq[1:], allowed=allowed)
    if seq[0][0] in allowed and seq[0][1]:
        solutions += rec_dubz(prev + seq[0][0] * 2, seq[1:], allowed=allowed)
    return solutions


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

def validate(ipst):
	for inputstr in ipst:
		got =0
		if check_presence(inputstr):
			got =1
			print inputstr
			if got==0:
				extr_unique = extract_unique(inputstr)
				if check_presence(extr_unique):
					got =1
					print extr_unique
				if got==0:
					poss_dups = possibile_dups(inputstr)
					for p in poss_dups:
						if check_presence(p):
							got =1
							print p
					if got==0:
						for p in poss_dups:
							for w in vowels(p):
								if check_presence(w):
									got =1
									print w
									break
				if got==0:
					print inputstr
					print "NO SUGGESTION"
def main():
	
	while 1:
		inputstr =raw_input("> ").lower()
		if 'exit()' in inputstr:
			break
		elif 'validate()' in inputstr:
			ipst=validator.main()
			validate(ipst)
			break
		else:
			got =0
			if check_presence(inputstr):
				got =1
				print inputstr
			if got==0:
				extr_unique = extract_unique(inputstr)
				if check_presence(extr_unique):
					got =1
					print extr_unique
			if got==0:
				poss_dups = possibile_dups(inputstr)
				for p in poss_dups:
					if check_presence(p):
						got =1
						print p
				if got==0:
					for p in poss_dups:
						for w in vowels(p):
							if check_presence(w):
								got =1
								print w
								break
			if got==0:
				print "NO SUGGESTION"

										

if __name__ == '__main__':
    main()