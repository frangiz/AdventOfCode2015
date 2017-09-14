import unittest
from days import day18
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		result = day18.animate([
			'.#.#.#',
			'...##.',
			'#....#',
			'..#...',
			'#.#..#',
			'####..'
		], 4)
		expected_result = [
			'......',
			'......',
			'..##..',
			'..##..',
			'......',
			'......'
		]
		self.assertEqual(result, expected_result)
		self.assertEqual(sum(line.count('#') for line in result), 4)

	def test_example_b1(self):
		result = day18.animate([
			'##.#.#',
			'...##.',
			'#....#',
			'..#...',
			'#.#..#',
			'####.#'
		], 5, [(0, 0), (5, 0), (0, 5), (5, 5)])
		expected_result = [
			'##.###',
			'.##..#',
			'.##...',
			'.##...',
			'#.#...',
			'##...#'
		]
		self.assertEqual(result, expected_result)
		self.assertEqual(sum(line.count('#') for line in result), 17)

	def test_answer_part_a(self):
		result = day18.part_a(util.get_file_contents('day18.txt'))
		self.assertEqual(result, '1061')

	def test_answer_part_b(self):
		result = day18.part_b(util.get_file_contents('day18.txt'))
		self.assertEqual(result, '1006')
