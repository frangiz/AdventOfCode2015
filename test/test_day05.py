import unittest
from days import day05
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day05.part_a(['ugknbfddgicrmopn'])
		self.assertEqual(result, '1')

	def test_example_a2(self):
		result = day05.part_a(['aaa'])
		self.assertEqual(result, '1')

	def test_example_a3(self):
		result = day05.part_a(['jchzalrnumimnmhp'])
		self.assertEqual(result, '0')

	def test_example_a4(self):
		result = day05.part_a(['haegwjzuvuyypxyu'])
		self.assertEqual(result, '0')

	def test_example_a5(self):
		result = day05.part_a(['dvszwmarrgswjxmb'])
		self.assertEqual(result, '0')

	def test_example_b1(self):
		result = day05.part_b(['qjhvhtzxzqqjkmpb'])
		self.assertEqual(result, '1')

	def test_example_b2(self):
		result = day05.part_b(['xxyxx'])
		self.assertEqual(result, '1')

	def test_example_b3(self):
		result = day05.part_b(['uurcxstgmygtbstg'])
		self.assertEqual(result, '0')

	def test_example_b4(self):
		result = day05.part_b(['ieodomkazucvgmuy'])
		self.assertEqual(result, '0')

	def test_answer_part_a(self):
		result = day05.part_a(util.get_file_contents('day05.txt'))
		self.assertEqual(result, '238')

	def test_answer_part_b(self):
		result = day05.part_b(util.get_file_contents('day05.txt'))
		self.assertEqual(result, '69')
