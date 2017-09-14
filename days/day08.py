def get_diff(line):
	return len(line.strip()) - len(eval(line.strip()))

def encode(line):
	return '"' +line.replace('\\', '\\\\').replace('"', '\\"') +'"'

def get_diff_part_b(line):
	return len(encode(line)) - len(line)

def part_a(input):
	return str(sum(map(get_diff, input)))

def part_b(input):
	return str(sum(map(get_diff_part_b, input)))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
