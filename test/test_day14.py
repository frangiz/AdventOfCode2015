import unittest
from days import day14
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		olympics = day14.Olympics()
		olympics.setup_reindeers([
			'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
			'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
		])
		self.assertEqual(olympics.find_longest_distance(1000), 1120)

	def test_example_b1(self):
		olympics = day14.Olympics()
		olympics.setup_reindeers([
			'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
			'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'
		])
		for t in range(1, 1001):
			olympics.find_longest_distance(t)
		self.assertEqual(olympics.points['Dancer'], 689)
		self.assertEqual(olympics.points['Comet'], 312)

	def test_answer_part_a(self):
		result = day14.part_a(util.get_file_contents('day14.txt'))
		self.assertEqual(result, '2660')

	def test_answer_part_b(self):
		result = day14.part_b(util.get_file_contents('day14.txt'))
		self.assertEqual(result, '1256')
