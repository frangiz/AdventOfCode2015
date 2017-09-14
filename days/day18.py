from copy import deepcopy

def animate(grid, iterations, always_on=[]):
	grid = [list(l.strip()) for l in grid]
	for pos in always_on:
		grid[pos[1]][pos[0]] = '#'
	for _ in range(iterations):
		grid = do_animation(grid, always_on)
	return [''.join(l) for l in grid]

def do_animation(grid, always_on):
	tmp = deepcopy(grid)
	for y, row in enumerate(tmp):
		for x, _ in enumerate(row):
			if (x, y) not in always_on:
				grid[y][x] = get_new_status(tmp, x, y)
	return grid

def get_new_status(grid, x, y):
	neighbors = get_all_neighbors(grid, x, y)
	if grid[y][x] == '#':
		if neighbors.count('#') in [2, 3]:
			return '#'
		else:
			return '.'

	if grid[y][x] == '.':
		if neighbors.count('#') in [3]:
			return '#'
		else:
			return '.'

def get_all_neighbors(grid, x, y):
	return [
		get_neighbor(grid, x - 1, y - 1),
		get_neighbor(grid, x, y - 1),
		get_neighbor(grid, x + 1, y - 1),
		get_neighbor(grid, x - 1, y),
		get_neighbor(grid, x + 1, y),
		get_neighbor(grid, x - 1, y + 1),
		get_neighbor(grid, x, y + 1),
		get_neighbor(grid, x + 1, y + 1)
	]

def get_neighbor(grid, x, y):
	if y < 0 or y >= len(grid):
		return '.'
	elif x < 0 or x >= len(grid[y]):
		return '.'
	else:
		return grid[y][x]

def part_a(input):
	return str(sum(line.count('#') for line in animate(input, 100)))

def part_b(input):
	return str(sum(line.count('#') for line in animate(input, 100, [
		(0, 0), (99, 0), (0, 99), (99, 99)
	])))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
