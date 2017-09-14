import re
from itertools import permutations

class Table:
	def __init__(self):
		self.happiness_table = {}
		self.people = set()

	def find_optimal_seating_arrangement(self, input):
		self.__parse_input(input)
		perm = self.__get_permutations()
		return max([self.__calc_happiness(p) for p in perm])

	def __parse_input(self, input):
		for line in input:
			m = re.search('([A-Za-z]+) would (gain|lose) ([\d]+) happiness units by sitting next to ([A-Za-z]+)', line)
			if m != None:
				v = int(m.group(3)) if m.group(2) == 'gain' else int(m.group(3)) * -1
				self.happiness_table[str(m.group(1)) +':' +str(m.group(4))] = v

	def __get_permutations(self):
		for p in self.happiness_table:
			self.people.add(p.split(':')[0])
			self.people.add(p.split(':')[1])
		return permutations(self.people)

	def __calc_happiness(self, arrangement):
		seatings = list(zip(arrangement[:-1], arrangement[1:]))
		seatings.append((arrangement[-1], arrangement[0]))
		happiness = 0
		for seating in seatings:
			try:
				happiness += self.happiness_table[seating[0] +':' +seating[1]]
				happiness += self.happiness_table[seating[1] +':' +seating[0]]
			except KeyError:
				pass
		return happiness

def part_a(input):
	table = Table()
	return str(table.find_optimal_seating_arrangement(input))

def part_b(input):
	table = Table()
	table.people.add('Me')
	return str(table.find_optimal_seating_arrangement(input))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
