import itertools

def main():
	word= "teepee"
	allowed=('aeiou')
	char_counts = []
	rtn =[]
	for k,v in itertools.groupby(word):
		if len(list(v)) >= 2:
			char_counts.append([k, 2])
		else:
			char_counts.append([k, 1])
	print rec_dubz('', char_counts, allowed=allowed)
def rec_dubz(prev, seq, allowed='aeiou'):
    if not seq:
        return [prev]
    solutions = rec_dubz(prev + seq[0][0], seq[1:], allowed=allowed)
    if seq[0][0] in allowed and seq[0][1]:
        solutions += rec_dubz(prev + seq[0][0] * 2, seq[1:], allowed=allowed)
    return solutions		
	



if __name__ == '__main__':
    main()