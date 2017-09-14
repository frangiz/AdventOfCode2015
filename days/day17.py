from itertools import combinations

def find_combinations(containers, liters):
	result = []
	containers = [int(n) for n in containers]
	for i in range(0, len(containers)):
		for c in combinations(containers, i):
			if sum(c) == liters:
				result.append(c)
	return result

def find_min_number_of_containers(containers, liters):
	all_combinations = find_combinations(containers, liters)
	# all_combinations is already sorted with the smallest number of elements
	# at the beginning of the list.
	count = 0
	for c in all_combinations:
		if len(c) == len(all_combinations[0]):
			count += 1
		else:
			break
	return count

def part_a(input):
	return str(len(find_combinations(input, 150)))

def part_b(input):
	return str(find_min_number_of_containers(input, 150))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
