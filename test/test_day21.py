import unittest
from days import day21
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		p1 = day21.Character('player', 8, 5, 5)
		p2 = day21.Character('boss', 12, 7, 2)
		result = day21.fight(p1, p2)
		self.assertEqual(result, p1)

	def test_answer_part_a(self):
		result = day21.part_a(util.get_file_contents('day21.txt'))
		self.assertEqual(result, '91')

	def test_answer_part_b(self):
		result = day21.part_b(util.get_file_contents('day21.txt'))
		self.assertEqual(result, '158')
