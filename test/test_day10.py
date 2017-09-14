import unittest
from days import day10
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day10.next_number('1')
		self.assertEqual(result, '11')

	def test_example_a2(self):
		result = day10.next_number('11')
		self.assertEqual(result, '21')

	def test_example_a3(self):
		result = day10.next_number('21')
		self.assertEqual(result, '1211')

	def test_example_a4(self):
		result = day10.next_number('1211')
		self.assertEqual(result, '111221')

	def test_example_a5(self):
		result = day10.next_number('111221')
		self.assertEqual(result, '312211')

	def test_example_a6(self):
		result = day10.look_and_say('1', 5)
		self.assertEqual(result, '312211')

	def test_answer_part_a(self):
		result = day10.part_a(util.get_file_contents('day10.txt'))
		self.assertEqual(result, '360154')

	def test_answer_part_b(self):
		result = day10.part_b(util.get_file_contents('day10.txt'))
		self.assertEqual(result, '5103798')
