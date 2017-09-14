import unittest
from days import day03
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day03.part_a(['>'])
		self.assertEqual(result, '2')

	def test_example_a2(self):
		result = day03.part_a(['^>v<'])
		self.assertEqual(result, '4')

	def test_example_a3(self):
		result = day03.part_a(['^v^v^v^v^v'])
		self.assertEqual(result, '2')

	def test_example_b1(self):
		result = day03.part_b(['^v'])
		self.assertEqual(result, '3')

	def test_example_b2(self):
		result = day03.part_b(['^>v<'])
		self.assertEqual(result, '3')

	def test_example_b3(self):
		result = day03.part_b(['^v^v^v^v^v'])
		self.assertEqual(result, '11')

	def test_answer_part_a(self):
		result = day03.part_a(util.get_file_contents('day03.txt'))
		self.assertEqual(result, '2572')

	def test_answer_part_b(self):
		result = day03.part_b(util.get_file_contents('day03.txt'))
		self.assertEqual(result, '2631')
