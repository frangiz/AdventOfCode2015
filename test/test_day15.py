import unittest
from days import day15
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		recipe = day15.Recipe()
		recipe.parse_ingredients([
			'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
			'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
		])
		self.assertEqual(recipe.find_highest_scoring_cookie(), 62842880)

	def test_example_b1(self):
		recipe = day15.Recipe()
		recipe.parse_ingredients([
			'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
			'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
		])
		self.assertEqual(recipe.find_highest_scoring_cookie(500), 57600000)

	def test_answer_part_a(self):
		result = day15.part_a(util.get_file_contents('day15.txt'))
		self.assertEqual(result, '18965440')

	def test_answer_part_b(self):
		result = day15.part_b(util.get_file_contents('day15.txt'))
		self.assertEqual(result, '15862900')
