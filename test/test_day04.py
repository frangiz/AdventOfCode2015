import unittest
from days import day04
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day04.part_a('abcdef')
		self.assertEqual(result, '609043')

	def test_example_a2(self):
		result = day04.part_a('pqrstuv')
		self.assertEqual(result, '1048970')

	def test_answer_part_a(self):
		result = day04.part_a(util.get_file_contents('day04.txt'))
		self.assertEqual(result, '282749')

	def test_answer_part_b(self):
		result = day04.part_b(util.get_file_contents('day04.txt'))
		self.assertEqual(result, '9962624')
