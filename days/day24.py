from itertools import combinations
import sys
from functools import reduce
from operator import mul

def find_lowest_QE(input, groups):
	weights = [int(i) for i in input]
	subgroup_weight_goal = sum(weights) / groups

	biggest_possible_qe = reduce(mul, weights)
	for nbr_of_presents in range(len(weights)):
		lowest_qe = biggest_possible_qe
		for comb in combinations(weights, nbr_of_presents):
			if sum(comb) == subgroup_weight_goal:
				lowest_qe = min(lowest_qe, reduce(mul, comb))
		if lowest_qe != biggest_possible_qe:
			return lowest_qe
	return 0

def part_a(input):
	return str(find_lowest_QE(input, 3))

def part_b(input):
	return str(find_lowest_QE(input, 4))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
