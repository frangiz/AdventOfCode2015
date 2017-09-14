from collections import namedtuple
import itertools
import math

Item = namedtuple('Item', 'desc cost dmg armor')
Character = namedtuple('Character', 'name hp dmg armor')

class Shop:
	def __init__(self):
		self.weapons = [
			Item('Dagger', 8, 4, 0),
			Item('Shortsword', 10, 5, 0),
			Item('Warhammer', 25, 6, 0),
			Item('Longsword', 40, 7, 0),
			Item('Greataxe', 74, 8, 0)
		]
		self.armor = [
			Item('Leather', 13, 0, 1),
			Item('Chainmail', 31, 0, 2),
			Item('Splintmail', 53, 0, 3),
			Item('Bandedmail', 75, 0, 4),
			Item('Platemail', 102, 0, 5),
			Item('No armor', 0, 0, 0)
		]
		self.rings = [
			Item('Damage +1', 25, 1, 0),
			Item('Damage +2', 50, 2, 0),
			Item('Damage +3', 100, 3, 0),
			Item('Defense +1', 20, 0, 1),
			Item('Defense +2', 40, 0, 2),
			Item('Defense +3', 80, 0, 3),
			Item('No ring', 0, 0, 0)
		]
	def get_items(self):
		return filter(lambda items:
			items[2] != Item('No ring', 0, 0, 0) and items[2] != items[3],
			itertools.product(self.weapons, self.armor, self.rings, self.rings))

def fight(p1, p2):
	p1_req_attacks = p2.hp / max(p1.dmg - p2.armor, 1)
	p2_req_attacks = p1.hp / max(p2.dmg - p1.armor, 1)
	return p1 if p1_req_attacks <= p2_req_attacks else p2

def simulate(input):
	hp, d, a = [line.split()[-1] for line in input]
	boss = Character('Boss', int(hp), int(d), int(a))
	gold_to_spend = 10**10 # Just something big to start with
	for items in Shop().get_items():
		cost = sum(item.cost for item in items)
		dmg = sum(item.dmg for item in items)
		armor = sum(item.armor for item in items)
		player = Character('player', 100, dmg, armor)
		if fight(player, boss) == player:
			gold_to_spend = min(gold_to_spend, cost)

	return(gold_to_spend)

def simulate(input, starting_gold, func):
	hp, d, a = [line.split()[-1] for line in input]
	boss = Character('Boss', int(hp), int(d), int(a))
	gold_to_spend = starting_gold
	for items in Shop().get_items():
		cost = sum(item.cost for item in items)
		dmg = sum(item.dmg for item in items)
		armor = sum(item.armor for item in items)
		player = Character('player', 100, dmg, armor)
		gold_to_spend = func(player, boss, gold_to_spend, cost)

	return(str(gold_to_spend))

def part_a_rule(player, boss, current_gold, cost):
	if fight(player, boss) == player:
		return min(current_gold, cost)
	return current_gold

def part_b_rule(player, boss, current_gold, cost):
	if fight(player, boss) == boss:
		return max(current_gold, cost)
	return current_gold

def part_a(input):
	return str(simulate(input, 10**10, part_a_rule))

def part_b(input):
	return str(simulate(input, 0, part_b_rule))

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
