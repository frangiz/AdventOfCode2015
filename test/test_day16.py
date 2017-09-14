import unittest
from days import day16
import util

class MyTestCase(unittest.TestCase):
	def test_answer_part_a(self):
		result = day16.part_a(util.get_file_contents('day16.txt'))
		self.assertEqual(result, '213')

	def test_answer_part_b(self):
		result = day16.part_b(util.get_file_contents('day16.txt'))
		self.assertEqual(result, '323')
