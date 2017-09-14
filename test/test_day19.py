import unittest
from days import day19
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		plant = day19.RedNosedReindeerNuclearFusionFissionPlant()
		plant.calibrate([
			'H => HO',
			'H => OH',
			'O => HH'
		])
		result = plant.find_molecules('HOH')
		exprected_result = set(['HOOH', 'HOHO', 'OHOH', 'HOOH', 'HHHH'])
		self.assertTrue(len(result^exprected_result) == 0)
		self.assertEqual(len(result), 4)

	def test_example_b1(self):
		plant = day19.RedNosedReindeerNuclearFusionFissionPlant()
		plant.calibrate([
			'e => H',
			'e => O',
			'H => HO',
			'H => OH',
			'O => HH',
		], True)
		result = plant.fabricate_molecule('HOH')
		self.assertEqual(result, 3)

	def test_example_b2(self):
		plant = day19.RedNosedReindeerNuclearFusionFissionPlant()
		plant.calibrate([
			'e => H',
			'e => O',
			'H => HO',
			'H => OH',
			'O => HH',
		], True)
		result = plant.fabricate_molecule('HOHOHO')
		self.assertEqual(result, 6)

	def test_answer_part_a(self):
		result = day19.part_a(util.get_file_contents('day19.txt'))
		self.assertEqual(result, '576')

	def test_answer_part_b(self):
		result = day19.part_b(util.get_file_contents('day19.txt'))
		self.assertEqual(result, '207')
