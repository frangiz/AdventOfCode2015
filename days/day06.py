import re

class Grid:
	def __init__(self, width, height):
		self.grid = [[0 for x in range(width)] for y in range(height)]

	def instruct(self, instruction):
		m = re.search('turn on (\d+,\d+) through (\d+,\d+)', instruction)
		if m != None:
			self.set_values(m.group(1), m.group(2), self.turn_on)
		m = re.search('toggle (\d+,\d+) through (\d+,\d+)', instruction)
		if m != None:
			self.set_values(m.group(1), m.group(2), self.toggle)
		m = re.search('turn off (\d+,\d+) through (\d+,\d+)', instruction)
		if m != None:
			self.set_values(m.group(1), m.group(2), self.turn_off)

	def set_values(self, start, end, func):
		x0, y0 = start.split(',')
		x1, y1 = end.split(',')
		for x in range(int(x0), int(x1) + 1):
			for y in range(int(y0), int(y1) + 1):
				func(x, y)

	def turn_on(self, x, y):
		self.grid[x][y] = True

	def turn_off(self, x, y):
		self.grid[x][y] = False

	def toggle(self, x, y):
		self.grid[x][y] = not self.grid[x][y]

	def lit_lights(self):
		return sum(map(sum, self.grid))

class GridPartB(Grid):
	def __init__(self, width, height):
		Grid.__init__(self, width, height)

	def turn_on(self, x, y):
		self.grid[x][y] += 1

	def turn_off(self, x, y):
		if self.grid[x][y] > 0:
			self.grid[x][y] -= 1

	def toggle(self, x, y):
		self.grid[x][y] += 2

def part_a(input):
	grid = Grid(1000, 1000)
	for instruction in input:
		grid.instruct(instruction)
	return str(grid.lit_lights())

def part_b(input):
	grid = GridPartB(1000, 1000)
	for instruction in input:
		grid.instruct(instruction)
	return str(grid.lit_lights())

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
