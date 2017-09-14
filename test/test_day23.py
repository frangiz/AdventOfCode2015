import unittest
from days import day23
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		computer = day23.Computer()
		computer.run([
			'inc a',
			'jio a, +2',
			'tpl a',
			'inc a'
		])
		self.assertEqual(computer.registers['a'], 2)

	def test_answer_part_a(self):
		result = day23.part_a(util.get_file_contents('day23.txt'))
		self.assertEqual(result, '170')

	def test_answer_part_b(self):
		result = day23.part_b(util.get_file_contents('day23.txt'))
		self.assertEqual(result, '247')
