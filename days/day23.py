class Computer:
	def __init__(self):
		self.registers = { 'a': 0, 'b': 0 }

	def run(self, input):
		instructions = self.parse_instructions(input)
		index = 0
		while index >= 0 and index < len(instructions):
			index += instructions[index][0](*instructions[index][1:])

	def parse_instructions(self, input):
		instructions = []
		for line in input:
			tokens = line.split()
			if tokens[0] == 'hlf':
				instructions.append((self.__hlf, tokens[1]))
			elif tokens[0] == 'tpl':
				instructions.append((self.__tpl, tokens[1]))
			elif tokens[0] == 'inc':
				instructions.append((self.__inc, tokens[1]))
			elif tokens[0] == 'jmp':
				instructions.append((self.__jmp, tokens[1]))
			elif tokens[0] == 'jie':
				instructions.append((self.__jie, tokens[1].replace(',', ''), tokens[2]))
			elif tokens[0] == 'jio':
				instructions.append((self.__jio, tokens[1].replace(',', ''), tokens[2]))
		return instructions

	def get_value(self, value):
		try:
			return int(value)
		except ValueError:
			return self.registers[value]

	def __hlf(self, op1):
		self.registers[op1] = int(self.registers[op1] / 2)
		return 1

	def __tpl(self, op1):
		self.registers[op1] = self.registers[op1] * 3
		return 1

	def __inc(self, op1):
		self.registers[op1] += 1
		return 1

	def __jmp(self, op1):
		return int(op1)

	def __jie(self, op1, op2):
		if self.registers[op1] % 2 == 0:
			return int(op2)
		return 1

	def __jio(self, op1, op2):
		if self.registers[op1] == 1:
			return int(op2)
		return 1

def part_a(input):
	computer = Computer()
	computer.run(input)
	return str(computer.registers['b'])

def part_b(input):
	computer = Computer()
	computer.registers['a'] = 1
	computer.run(input)
	return str(computer.registers['b'])

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
