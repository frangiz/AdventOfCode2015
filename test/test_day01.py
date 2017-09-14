import unittest
from days import day01
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day01.part_a(['(())'])
		self.assertEqual(result, '0')

		result = day01.part_a(['()()'])
		self.assertEqual(result, '0')

	def test_example_a2(self):
		result = day01.part_a(['((('])
		self.assertEqual(result, '3')

		result = day01.part_a(['(()(()('])
		self.assertEqual(result, '3')

	def test_example_a3(self):
		result = day01.part_a(['))((((('])
		self.assertEqual(result, '3')

	def test_example_a4(self):
		result = day01.part_a(['())'])
		self.assertEqual(result, '-1')

		result = day01.part_a(['))('])
		self.assertEqual(result, '-1')

	def test_example_a5(self):
		result = day01.part_a([')))'])
		self.assertEqual(result, '-3')

		result = day01.part_a([')())())'])
		self.assertEqual(result, '-3')

	def test_answer_part_a(self):
		result = day01.part_a(util.get_file_contents('day01.txt'))
		self.assertEqual(result, '74')

	def test_answer_part_b(self):
		result = day01.part_b(util.get_file_contents('day01.txt'))
		self.assertEqual(result, '1795')
