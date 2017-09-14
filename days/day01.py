def part_a(input):
	floor = 0
	input_str = ''.join(input)
	for c in input_str:
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1
	return str(floor)

def part_b(input):
	floor = 0
	input_str = ''.join(input)
	for i, c in enumerate(input_str):
		if c == '(':
			floor += 1
		elif c == ')':
			floor -= 1
		if floor == -1:
			return str(i + 1)
	return '-1'

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
