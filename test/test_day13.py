import unittest
from days import day13
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		table = day13.Table()
		self.assertEqual(table.find_optimal_seating_arrangement(
			['Alice would gain 54 happiness units by sitting next to Bob.',
			'Alice would lose 79 happiness units by sitting next to Carol.',
			'Alice would lose 2 happiness units by sitting next to David.',
			'Bob would gain 83 happiness units by sitting next to Alice.',
			'Bob would lose 7 happiness units by sitting next to Carol.',
			'Bob would lose 63 happiness units by sitting next to David.',
			'Carol would lose 62 happiness units by sitting next to Alice.',
			'Carol would gain 60 happiness units by sitting next to Bob.',
			'Carol would gain 55 happiness units by sitting next to David.',
			'David would gain 46 happiness units by sitting next to Alice.',
			'David would lose 7 happiness units by sitting next to Bob.',
			'David would gain 41 happiness units by sitting next to Carol.']), 330)

	def test_answer_part_a(self):
		result = day13.part_a(util.get_file_contents('day13.txt'))
		self.assertEqual(result, '709')

	def test_answer_part_b(self):
		result = day13.part_b(util.get_file_contents('day13.txt'))
		self.assertEqual(result, '668')
