def next_number(number):
	count = 0
	current = ''
	result = ''
	for c in number +' ':
		if c == current:
			count += 1
		elif current == '':
			current = c
			count += 1
		else:
			result += str(count) + current
			count = 1
			current = c
	return result


def look_and_say(start_str, iterations):
	current = start_str
	for i in range(iterations):
		current = next_number(current)
	return current

def part_a(input):
	return str(len(look_and_say(''.join(input).strip(), 40)))

def part_b(input):
	return str(len(look_and_say(''.join(input).strip(), 50)))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
