class PasswordGenerator:
	def __init__(self):
		self.invalid_chars = ['i', 'o', 'l']

	def valid_password(self, password):
		return self.has_increasing_straight(password) and \
			not self.has_invalid_chars(password) and \
			self.has_non_overlapping_pairs(password)

	def next_password(self, password):
		password = self.increment_password(password)
		while not self.valid_password(password):
			password = self.increment_password(password)
		return password

	def increment_password(self, password):
		password = list(password)
		for i in range(len(password) - 1, 0, -1):
			if password[i] == 'z':
				password[i] = 'a'
			else:
				password[i] = chr(ord(password[i]) + 1)
				break
		return ''.join(password)

	def has_increasing_straight(self, password):
		for i in range(1, len(password) - 1):
			if ord(password[i - 1]) + 1 == ord(password[i]) and \
				ord(password[i]) == ord(password[i + 1]) - 1:
				return True
		return False

	def has_invalid_chars(self, password):
		return any(c in password for c in self.invalid_chars)

	def has_non_overlapping_pairs(self, password):
		overlapping_pairs = []
		i = 0
		while (i < len(password) - 1):
			if password[i] == password[i + 1]:
				overlapping_pairs.append(password[i:i+2])
				i += 2
			else:
			 	i += 1
		return len(overlapping_pairs) >= 2

def part_a(input):
	pg = PasswordGenerator()
	return pg.next_password(''.join(input).strip())

def part_b(input):
	pg = PasswordGenerator()
	first_password = pg.next_password(''.join(input).strip())
	return pg.next_password(first_password)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
