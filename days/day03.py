class RoboSanta:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.visited_places = {}

	def visit(self, instructions):
		self.visited_places[(self.x, self.y)] = 1
		for c in instructions:
			if c == '^':
				self.y = self.y - 1
			elif c == 'v':
				self.y = self.y + 1
			elif c == '<':
				self.x = self.x - 1
			elif c == '>':
				self.x = self.x + 1
			if not (self.x, self.y) in self.visited_places:
				self.visited_places[(self.x, self.y)] = 0
			self.visited_places[(self.x, self.y)] += 1

def part_a(input):
	santa = RoboSanta()
	input_str = ''.join(input)
	santa.visit(input_str)

	return str(len(santa.visited_places))

def part_b(input):
	santa = RoboSanta()
	robo_santa = RoboSanta()
	input_str = ''.join(input)
	santa.visit(input_str[::2])
	robo_santa.visit(input_str[1::2])

	visited_places = santa.visited_places.copy()
	visited_places.update(robo_santa.visited_places)

	return str(len(visited_places))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
