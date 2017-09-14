import unittest
from days import day11
import util

class MyTestCase(unittest.TestCase):
	def test_example_a1(self):
		pg = day11.PasswordGenerator()
		# req #1
		self.assertTrue(pg.has_increasing_straight('hijklmmn'))
		# req #2
		self.assertTrue(pg.has_invalid_chars('hijklmmn'))

		# fails any requirements => invalid password
		self.assertFalse(pg.valid_password('hijklmmn'))

	def test_example_a2(self):
		pg = day11.PasswordGenerator()
		# req #1
		self.assertFalse(pg.has_increasing_straight('abbceffg'))
		# req #3
		self.assertTrue(pg.has_non_overlapping_pairs('abbceffg'))

		# fails any requirements => invalid password
		self.assertFalse(pg.valid_password('abbceffg'))

	def test_example_a3(self):
		pg = day11.PasswordGenerator()
		# req #3
		self.assertFalse(pg.has_non_overlapping_pairs('abbcegjk'))

		# fails any requirements => invalid password
		self.assertFalse(pg.valid_password('abbcegjk'))

	def test_example_a4(self):
		pg = day11.PasswordGenerator()
		self.assertEqual(pg.next_password('abcdefgh'), 'abcdffaa')

	def test_example_a5(self):
		pg = day11.PasswordGenerator()
		self.assertEqual(pg.next_password('ghijklmn'), 'ghjaabcc')

	def test_answer_part_a(self):
		result = day11.part_a(util.get_file_contents('day11.txt'))
		self.assertEqual(result, 'cqjxxyzz')

	def test_answer_part_b(self):
		result = day11.part_b(util.get_file_contents('day11.txt'))
		self.assertEqual(result, 'cqkaabcc')
