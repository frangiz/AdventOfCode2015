import sys

class RedNosedReindeerNuclearFusionFissionPlant():
	def __init__(self):
		self.replacements = {}

	def calibrate(self, input, reverse=False):
		for line in input:
			k, v = line.strip().split(' => ')
			if reverse:
				k, v = v, k
			if k not in self.replacements:
				self.replacements[k] = []
			self.replacements[k].append(v)

	def find_molecules(self, starting_point):
		result = set()
		for i, _ in enumerate(starting_point):
			for key, values in self.replacements.items():
				if starting_point.startswith(key, i):
					for value in values:
						new_molecule = ''
						if i > 0:
							new_molecule += starting_point[0:i]
						new_molecule += value + starting_point[i + len(key):]
						result.add(new_molecule)
		return result

	def fabricate_molecule(self, target_molecule):
		target = 'e'
		start = target_molecule
		frontier = [(start, 0)]
		while frontier:
			molecule, dist = frontier.pop()
			for neighbour in sorted(self.find_molecules(molecule)):
				if neighbour == target:
					return dist + 1
				frontier.append((neighbour, dist + 1))
		return 0

def part_a(input):
	plant = RedNosedReindeerNuclearFusionFissionPlant()
	plant.calibrate(input)
	molecules = plant.find_molecules('ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF')
	return str(len(molecules))

def part_b(input):
	plant = RedNosedReindeerNuclearFusionFissionPlant()
	plant.calibrate(input, True)
	return str(plant.fabricate_molecule('ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF'))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
