import unittest
from days import day07
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		circuit = day07.Circuit()
		circuit.set(['123 -> x',
					'456 -> y',
					'x AND y -> d',
					'x OR y -> e',
					'x LSHIFT 2 -> f',
					'y RSHIFT 2 -> g',
					'NOT x -> h',
					'NOT y -> i'])
		self.assertEqual(str(circuit.eval('d')), '72')
		self.assertEqual(str(circuit.eval('e')), '507')
		self.assertEqual(str(circuit.eval('f')), '492')
		self.assertEqual(str(circuit.eval('g')), '114')
		self.assertEqual(str(circuit.eval('h')), '65412')
		self.assertEqual(str(circuit.eval('i')), '65079')
		self.assertEqual(str(circuit.eval('x')), '123')
		self.assertEqual(str(circuit.eval('y')), '456')

	def test_answer_part_a(self):
		result = day07.part_a(util.get_file_contents('day07.txt'))
		self.assertEqual(result, '3176')

	def test_answer_part_b(self):
		result = day07.part_b(util.get_file_contents('day07.txt'))
		self.assertEqual(result, '14710')
