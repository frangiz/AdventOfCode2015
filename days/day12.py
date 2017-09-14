import json

def find_sum(obj, exclude_value):
	if type(obj) == int:
		return obj
	elif type(obj) == list:
		return sum(find_sum(x, exclude_value) for x in obj)
	elif type(obj) == dict:
		if not exclude_value in obj.values():
			return sum(find_sum(x, exclude_value) for x in obj) \
				+ sum(find_sum(x, exclude_value) for x in obj.values())
	return 0

def sum_lines(lines, exclude_value=''):
	return find_sum(json.loads(''.join(lines)), exclude_value)

def part_a(input):
	return str(sum_lines(input))

def part_b(input):
	return str(sum_lines(input, 'red'))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
