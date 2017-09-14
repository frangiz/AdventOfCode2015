
def part_a(input):
	nice_strings = 0
	vowels = ['a', 'e', 'i', 'o', 'u']
	bad_strings = ['ab', 'cd', 'pq', 'xy']
	for s in input:
		nbr_of_vowels = 0
		has_repeating_chars = False
		has_bad_strings = False
		for i, c in enumerate(s):
			if c in vowels:
				nbr_of_vowels += 1
			if i + 1 < len(s):
				has_repeating_chars |= c == s[i + 1]
				if s[i:i+2] in bad_strings:
					has_bad_strings = True
		if nbr_of_vowels >= 3 and has_repeating_chars and not has_bad_strings:
			nice_strings += 1
	return str(nice_strings)

def part_b(input):
	nice_strings = 0
	for s in input:
		has_double_pair = False
		has_xyx = False
		for i, c in enumerate(s[:-2]):
			if s[i] + s[i + 1] in s[i + 2:]:
				has_double_pair = True
		for i, c in enumerate(s):
			if i + 2 < len(s):
				has_xyx |= s[i] == s[i + 2]
		if has_double_pair and has_xyx:
			nice_strings += 1
	return str(nice_strings)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
