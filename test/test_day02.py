import unittest
from days import day02
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day02.part_a(['2x3x4'])
		self.assertEqual(result, '58')

	def test_example_a2(self):
		result = day02.part_a(['1x1x10'])
		self.assertEqual(result, '43')

	def test_example_b1(self):
		result = day02.part_b(['2x3x4'])
		self.assertEqual(result, '34')

	def test_example_b2(self):
		result = day02.part_b(['1x1x10'])
		self.assertEqual(result, '14')

	def test_answer_part_a(self):
		result = day02.part_a(util.get_file_contents('day02.txt'))
		self.assertEqual(result, '1606483')

	def test_answer_part_b(self):
		result = day02.part_b(util.get_file_contents('day02.txt'))
		self.assertEqual(result, '3842356')
