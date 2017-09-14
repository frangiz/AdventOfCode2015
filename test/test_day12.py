import unittest
from days import day12
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		self.assertEqual(day12.sum_lines(['[1,2,3]']), 6)
		self.assertEqual(day12.sum_lines(['{"a":2,"b":4}']), 6)

	def test_example_a2(self):
		self.assertEqual(day12.sum_lines(['[[[3]]]']), 3)
		self.assertEqual(day12.sum_lines(['{"a":{"b":4},"c":-1}']), 3)

	def test_example_a3(self):
		self.assertEqual(day12.sum_lines(['{"a":[-1,1]}']), 0)
		self.assertEqual(day12.sum_lines(['[-1,{"a":1}]']), 0)

	def test_example_a4(self):
		self.assertEqual(day12.sum_lines(['[]']), 0)
		self.assertEqual(day12.sum_lines(['{}']), 0)

	def test_example_b1(self):
		self.assertEqual(day12.sum_lines(['[1,2,3]'], 'red'), 6)

	def test_example_b2(self):
		self.assertEqual(day12.sum_lines(['[1,{"c":"red","b":2},3]'], 'red'), 4)

	def test_example_b3(self):
		self.assertEqual(day12.sum_lines(['{"d":"red","e":[1,2,3,4],"f":5}'], 'red'), 0)

	def test_example_b4(self):
		self.assertEqual(day12.sum_lines(['[1,"red",5]'], 'red'), 6)

	def test_answer_part_a(self):
		result = day12.part_a(util.get_file_contents('day12.txt'))
		self.assertEqual(result, '191164')

	def test_answer_part_b(self):
		result = day12.part_b(util.get_file_contents('day12.txt'))
		self.assertEqual(result, '87842')
