import unittest
from days import day20
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day20.presents_for_houses(10, 10)
		expected_result = [0, 10, 30, 40, 70, 60, 120, 80, 150, 130]
		self.assertEqual(result, expected_result)

	def test_answer_part_a(self):
		result = day20.part_a(util.get_file_contents('day20.txt'))
		self.assertEqual(result, '776160')

	def test_answer_part_b(self):
		result = day20.part_b(util.get_file_contents('day20.txt'))
		self.assertEqual(result, '786240')
