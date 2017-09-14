class Circuit:
	def __init__(self):
		self.graph = {}
		self.values = {}

	def set(self, instructions):
		for instruction in instructions:
			# source -> target
			# self.graph['a'] = ['b', 'AND', 'c']
			source, target = instruction.split(' -> ')
			self.graph[target.replace('\n', '')] = source.split()

	def eval(self, key):
		if key.isdigit():
			return int(key)
		if key not in self.values:
			source = self.graph[key]
			if len(source) == 1:
				if source[0].isdigit():
					self.values[key] = int(source[0])
				else:
					self.values[key] = self.eval(source[0])
			if 'AND' in source:
				self.values[key] = self.eval(source[0]) & self.eval(source[2])
			if 'OR' in source:
				self.values[key] = self.eval(source[0]) | self.eval(source[2])
			if 'LSHIFT' in source:
				self.values[key] = self.eval(source[0]) << int(source[2])
			if 'RSHIFT' in source:
				self.values[key] = self.eval(source[0]) >> int(source[2])
			if 'NOT' in source:
				self.values[key] = ~self.eval(source[1]) & 0xffff
		return self.values[key]

def part_a(input):
	circuit = Circuit()
	circuit.set(input)
	return str(circuit.eval('a'))

def part_b(input):
	circuit = Circuit()
	circuit.set(input)
	a = circuit.eval('a')
	circuit.values.clear()
	circuit.values['b'] = a
	return str(circuit.eval('a'))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
