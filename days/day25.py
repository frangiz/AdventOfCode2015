from collections import namedtuple
import re

Pos = namedtuple('Pos', 'row col')

def find_code(start_value, goal, next_code_func):
	local_max_row = 1
	cur_pos = Pos(1, 1)
	cur_code = start_value
	while cur_pos != goal:
		cur_pos, local_max_row = next_pos(cur_pos, local_max_row)
		cur_code = next_code_func(cur_code)
	return cur_code

def next_pos(cur_pos, local_max_row):
	if cur_pos.row == 1:
		return (Pos(local_max_row + 1, 1), local_max_row + 1)
	return (Pos(cur_pos.row - 1, cur_pos.col + 1), local_max_row)

def part_a(input):
	m = re.search('row (\d+), column (\d+)', ''.join(input))
	if m != None:
		return str(find_code(20151125,
		 					Pos(int(m.group(1)), int(m.group(2))),
							lambda x: x * 252533 % 33554393))
	return str(0)

def part_b(input):
	return str(0)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
