import re

specs_part_a = {
	'children': lambda x: x == 3,
	'cats': lambda x: x == 7,
	'samoyeds': lambda x: x == 2,
	'pomeranians': lambda x: x == 3,
	'akitas': lambda x: x == 0,
	'vizslas': lambda x: x == 0,
	'goldfish': lambda x: x == 5,
	'trees': lambda x: x == 3,
	'cars': lambda x: x == 2,
	'perfumes': lambda x: x == 1
}

specs_part_b = {
	'children': lambda x: x == 3,
	'cats': lambda x: x > 7,
	'samoyeds': lambda x: x == 2,
	'pomeranians': lambda x: x < 3,
	'akitas': lambda x: x == 0,
	'vizslas': lambda x: x == 0,
	'goldfish': lambda x: x < 5,
	'trees': lambda x: x > 3,
	'cars': lambda x: x == 2,
	'perfumes': lambda x: x == 1
}

def find_match(input, specs):
	for line in input:
		m = re.search('Sue (\d+): ([a-z]+): (\d+), ([a-z]+): (\d+), ([a-z]+): (\d+)', line)
		if m != None:
			things = {
				m.group(2): int(m.group(3)),
				m.group(4): int(m.group(5)),
				m.group(6): int(m.group(7))
			}
			if sum(specs[k](v) for k, v in things.items()) == 3:
				return m.group(1)

def part_a(input):
	return str(find_match(input, specs_part_a))

def part_b(input):
	return str(find_match(input, specs_part_b))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
