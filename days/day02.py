def part_a(input):
	total_area = 0
	for dimensions in input:
		l, w, h = map(int, dimensions.split('x'))
		sides = 2*l*w + 2*w*h + 2*h*l
		min_area = min(l*w, l*h, w*h)
		total_area = total_area + sides + min_area
	return str(total_area)

def part_b(input):
	total_ribbon = 0
	for dimensions in input:
		sides = [int(i) for i in dimensions.split('x')]
		sides.sort()
		total_ribbon = total_ribbon + (sides[0] * 2 + sides[1] * 2) \
		 + sides[0] * sides[1] * sides[2]

	return str(total_ribbon)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
