import unittest
from days import day24
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day24.find_lowest_QE(
			['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'], 3
		)
		self.assertEqual(result, 99)

	def test_example_b1(self):
		result = day24.find_lowest_QE(
			['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'], 4
		)
		self.assertEqual(result, 44)

	def test_answer_part_a(self):
		result = day24.part_a(util.get_file_contents('day24.txt'))
		self.assertEqual(result, '10723906903')

	def test_answer_part_b(self):
		result = day24.part_b(util.get_file_contents('day24.txt'))
		self.assertEqual(result, '74850409')
