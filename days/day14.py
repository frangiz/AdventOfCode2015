from collections import namedtuple
import re

Reindeer = namedtuple('Reindeer', 'name v fly_time rest_time')

class Olympics:
	def __init__(self):
		self.reindeers = []
		self.distance_traveled = {}
		self.points = {}

	def setup_reindeers(self, input):
		for line in input:
			m = re.search('([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
			if m != None:
				self.reindeers.append(Reindeer(name = m.group(1),
					v = int(m.group(2)), fly_time = int(m.group(3)),
					rest_time = int(m.group(4))))
				self.distance_traveled[m.group(1)] = 0
				self.points[m.group(1)] = 0

	def find_longest_distance(self, time):
		for r in self.reindeers:
			full_laps = int(time / (r.fly_time + r.rest_time))
			partial_lap = time % (r.fly_time + r.rest_time)
			distance = (full_laps * r.fly_time * r.v) + (min(partial_lap, r.fly_time) * r.v)
			self.distance_traveled[r.name] = distance
		longest_distance = max(self.distance_traveled.values())
		for k, v in self.distance_traveled.items():
			if v == longest_distance:
				self.points[k] += 1
		return longest_distance

def part_a(input):
	olympics = Olympics()
	olympics.setup_reindeers(input)
	return str(olympics.find_longest_distance(2503))

def part_b(input):
	olympics = Olympics()
	olympics.setup_reindeers(input)
	for t in range(1, 2504):
		olympics.find_longest_distance(t)
	return str(max(olympics.points.values()))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
