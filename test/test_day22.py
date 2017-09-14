import unittest
from days import day22
import util
from days.day22 import *

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = find_least_amount_of_mana_to_win(
			Character('Player', 10, 0, 250, 0, [MagicMissile, Drain, Poison, Shield, Recharge]),
			Character('Boss', 13, 8, 0, 0, [Melee])
		)
		self.assertEqual(result.mana_spent, 226) # Poison, MagicMissile

	def test_example_a2(self):
		result = find_least_amount_of_mana_to_win(
			Character('Player', 10, 0, 250, 0, [MagicMissile, Drain, Poison, Shield, Recharge]),
			Character('Boss', 14, 8, 0, 0, [Melee])
		)
		self.assertEqual(result.mana_spent, 641) # Recharge, Shield, Drain, Poison, MagicMissile

	def test_answer_part_a(self):
		result = day22.part_a(util.get_file_contents('day22.txt'))
		self.assertEqual(result, '1269')

	def test_answer_part_b(self):
		result = day22.part_b(util.get_file_contents('day22.txt'))
		self.assertEqual(result, '1309')
