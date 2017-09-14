import sys

def presents_for_houses(max_house_number, presents, max_times_each_elf=sys.maxsize):
	houses = [0]*max_house_number
	for elf in range(1, max_house_number):
		for house in range(elf, min(max_house_number, elf * max_times_each_elf), elf):
			houses[house] += elf * presents
	return houses

def part_a(input):
	target_presents = int(''.join(input))
	presents = presents_for_houses(int(target_presents / 10), 10)
	for i, p in enumerate(presents):
		if p >= target_presents:
			return str(i)
	return str(0)

def part_b(input):
	target_presents = int(''.join(input))
	presents = presents_for_houses(int(target_presents / 10), 11, 50)
	for i, p in enumerate(presents):
		if p >= target_presents:
			return str(i)
	return str(0)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
