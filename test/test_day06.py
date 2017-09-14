import unittest
from days import day06
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day06.part_a(['turn on 0,0 through 999,999'])
		self.assertEqual(result, '1000000')

	def test_example_a2(self):
		result = day06.part_a(['toggle 0,0 through 999,0'])
		self.assertEqual(result, '1000')

	def test_example_a3(self):
		result = day06.part_a(['turn on 0,0 through 999,999',
								'turn off 499,499 through 500,500'])
		self.assertEqual(result, str(1000*1000-4))

	def test_answer_part_a(self):
		result = day06.part_a(util.get_file_contents('day06.txt'))
		self.assertEqual(result, '377891')

	def test_answer_part_b(self):
		result = day06.part_b(util.get_file_contents('day06.txt'))
		self.assertEqual(result, '14110788')
