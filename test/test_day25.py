import unittest
from days import day25
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day25.find_code(
			1, day25.Pos(1, 6), lambda x: x +1
		)
		self.assertEqual(result, 21)

	def test_example_a2(self):
		result = day25.find_code(
			20151125, day25.Pos(1, 6), lambda x: x * 252533 % 33554393
		)
		self.assertEqual(result, 33511524)

	def test_answer_part_a(self):
		result = day25.part_a(util.get_file_contents('day25.txt'))
		self.assertEqual(result, '19980801')
