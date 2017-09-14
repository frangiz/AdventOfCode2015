import unittest
from days import day09
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day09.part_a([	'London to Dublin = 464',
								'London to Belfast = 518',
								'Dublin to Belfast = 141'])
		self.assertEqual(result, '605')

	def test_example_b1(self):
		result = day09.part_b([	'London to Dublin = 464',
								'London to Belfast = 518',
								'Dublin to Belfast = 141'])
		self.assertEqual(result, '982')

	def test_answer_part_a(self):
		result = day09.part_a(util.get_file_contents('day09.txt'))
		self.assertEqual(result, '251')

	def test_answer_part_b(self):
		result = day09.part_b(util.get_file_contents('day09.txt'))
		self.assertEqual(result, '898')
