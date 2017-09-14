import unittest
from days import day17
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day17.find_combinations(['20', '15', '10', '5', '5'], 25)
		self.assertEqual(len(result), 4)
		self.assertTrue((15, 10) in result)
		self.assertEqual(result.count((20, 5)), 2)
		self.assertTrue((15, 5, 5) in result)

	def test_example_b1(self):
		result = day17.find_min_number_of_containers(['20', '15', '10', '5', '5'], 25)
		self.assertEqual(result, 3)

	def test_answer_part_a(self):
		result = day17.part_a(util.get_file_contents('day17.txt'))
		self.assertEqual(result, '1304')

	def test_answer_part_b(self):
		result = day17.part_b(util.get_file_contents('day17.txt'))
		self.assertEqual(result, '18')
