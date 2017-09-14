from itertools import permutations
import re
import sys

def find_paths(input):
	routes = {}
	cities = set()
	for line in input:
		m = re.search('([A-Za-z]+) to ([A-Za-z]+) = (\d+)', line)
		if m != None:
			routes[(m.group(1), m.group(2))] = int(m.group(3))
			cities.add(m.group(1))
			cities.add(m.group(2))
	paths = {}
	for perm in permutations(cities):
		total = 0
		for p in list(zip(perm[:-1], perm[1:])):
			if p in routes:
				total += routes[p]
			elif (p[1], p[0]) in routes:
				total += routes[(p[1], p[0])]
		paths[perm] = total
	return paths

def part_a(input):
	return str(min(find_paths(input).values()))

def part_b(input):
	return str(max(find_paths(input).values()))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
