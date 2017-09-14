import unittest
from days import day08
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day08.part_a([r'""'])
		self.assertEqual(result, '2')

	def test_example_a2(self):
		result = day08.part_a([r'"abc"'])
		self.assertEqual(result, '2')

	def test_example_a3(self):
		result = day08.part_a([r'"aaa\"aaa"'])
		self.assertEqual(result, '3')

	def test_example_a4(self):
		result = day08.part_a([r'"\x27"'])
		self.assertEqual(result, '5')

	def test_example_a5(self):
		result = day08.part_a([	r'""',
								r'"abc"',
								r'"aaa\"aaa"',
								r'"\x27"'])
		self.assertEqual(result, '12')

	def test_example_b1(self):
		result = day08.part_b([r'""'])
		self.assertEqual(result, '4')

	def test_example_b2(self):
		result = day08.part_b([r'"abc"'])
		self.assertEqual(result, '4')

	def test_example_b3(self):
		result = day08.part_b([r'"aaa\"aaa"'])
		self.assertEqual(result, '6')

	def test_example_b4(self):
		result = day08.part_b([r'"\x27"'])
		self.assertEqual(result, '5')

	def test_answer_part_a(self):
		result = day08.part_a(util.get_file_contents('day08.txt'))
		self.assertEqual(result, '1350')

	def test_answer_part_b(self):
		result = day08.part_b(util.get_file_contents('day08.txt'))
		self.assertEqual(result, '2085')
