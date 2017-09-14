import re
from collections import namedtuple

Ingredient = namedtuple('Ingredient', 'name cap dur fla tex cal')
MAX_VALUE = 100

class Recipe:
	def __init__(self):
		self.ingredients = []

	def parse_ingredients(self, input):
		for line in input:
			m = re.search('([A-Za-z]+): capacity ([-]?\d+), durability ([-]?\d+), flavor ([-]?\d+), texture ([-]?\d+), calories ([-]?\d+)', line)
			if m != None:
				self.ingredients.append(Ingredient(
					name = m.group(1),
					cap = int(m.group(2)),
					fla = int(m.group(4)),
					dur = int(m.group(3)),
					tex = int(m.group(5)),
					cal = int(m.group(6))
				))

	def find_highest_scoring_cookie(self, matching_calories=0):
		combinations = self.__find_ingredient_combinations()
		return max([self.__calc_score(c, matching_calories) for c in combinations])

	def __find_ingredient_combinations(self):
		amounts = [0] * len(self.ingredients)
		result = []
		for _ in range((MAX_VALUE + 1) ** len(self.ingredients) - 1):
			self.__increment_list(amounts)
			if sum(amounts) == MAX_VALUE:
				result.append(list(amounts))
		return result

	def __increment_list(self, amounts):
		for i, v in enumerate(amounts):
			if v == MAX_VALUE:
				amounts[i] = 0
			else:
				amounts[i] += 1
				break

	def __calc_score(self, combination, matching_calories=0):
		cap = sum([a*b for a,b in zip([i.cap for i in self.ingredients], combination)])
		dur = sum([a*b for a,b in zip([i.dur for i in self.ingredients], combination)])
		fla = sum([a*b for a,b in zip([i.fla for i in self.ingredients], combination)])
		tex = sum([a*b for a,b in zip([i.tex for i in self.ingredients], combination)])
		cal = sum([a*b for a,b in zip([i.cal for i in self.ingredients], combination)])
		if matching_calories > 0 and cal != matching_calories:
			return 0
		if cap < 0 or dur < 0 or fla < 0 or tex < 0:
			return 0
		return cap * dur * fla * tex

def part_a(input):
	recipe = Recipe()
	recipe.parse_ingredients(input)
	return str(recipe.find_highest_scoring_cookie())

def part_b(input):
	recipe = Recipe()
	recipe.parse_ingredients(input)
	return str(recipe.find_highest_scoring_cookie(500))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
