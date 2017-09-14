from collections import namedtuple, deque
import copy
import queue as Q

class Character:
	def __init__(self, name, hp, dmg, mana, armor, attacks):
		self.name = name
		self.hp = hp
		self.dmg = dmg
		self.mana = mana
		self.armor = armor
		self.attacks = attacks

	def __repr__(self):
		rv = copy.deepcopy(self.__dict__)
		rv['attacks'] = [a.__name__ for a in self.attacks]
		return str(rv)

class Attack:
	duration = 0
	mana_cost = 0

	def cast(self, attacker, defender):
		pass

	def tick(self, attacker, defender):
		return None

class MagicMissile(Attack):
	mana_cost = 53

	def cast(self, attacker, defender):
		attacker.mana -= self.mana_cost
		defender.hp -= 4

class Drain(Attack):
	mana_cost = 73

	def cast(self, attacker, defender):
		attacker.hp += 2
		defender.hp -= 2

class Poison(Attack):
	duration = 6
	mana_cost = 173

	def cast(self, attacker, defender):
		pass

	def tick(self, attacker, defender):
		self.duration -= 1
		defender.hp -= 3
		return 'Poison deals 3 damage; its timer is now ' +str(self.duration)

class Shield(Attack):
	duration = 6
	mana_cost = 113

	def cast(self, attacker, defender):
		attacker.armor += 7

	def tick(self, attacker, defender):
		self.duration -= 1
		if self.duration == 0:
			attacker.armor -= 7
		return 'Shield\'s timer is now ' +str(self.duration)

class Recharge(Attack):
	duration = 5
	mana_cost = 229

	def cast(self, attacker, defender):
		pass

	def tick(self, attacker, defender):
		self.duration -= 1
		attacker.mana += 101
		return 'Recharge provides 101 mana; timer is now ' +str(self.duration)

class Melee(Attack):
	def cast(self, attacker, defender):
		defender.hp -= max(attacker.dmg - defender.armor, 1)
		return attacker.name +' attacks for ' +str(attacker.dmg) +' damage.'

class GameState:
	def __init__(self, player, boss):
		self.player = player
		self.boss = boss
		self.parent = None

		self.event_log = []
		self.effects = []
		self.mana_spent = 0

	def __repr__(self):
		return str(self.__dict__)

	def __lt__(self, other):
		return self.mana_spent < other.mana_spent

	def tick_effects(self):
		[self.event_log.append(effect.tick(self.player, self.boss)) for effect in self.effects]
		self.effects = [e for e in self.effects if e.duration > 0]

	@staticmethod
	def CreateFrom(gameState):
		newState = GameState(
			copy.deepcopy(gameState.player),
			copy.deepcopy(gameState.boss))
		newState.parent = gameState
		for e in gameState.effects:
			newState.effects.append(copy.deepcopy(e))
		newState.mana_spent += gameState.mana_spent

		return newState

def find_least_amount_of_mana_to_win(player, boss, part_b=False):
	unvisited_states = Q.PriorityQueue()
	unvisited_states.put(GameState(player, boss))

	while unvisited_states.qsize() > 0:
		gs = unvisited_states.get()
		if gs.player.hp <= 0:
			continue
		if gs.boss.hp <= 0:
			return gs

		# Player's turn
		for attack_type in gs.player.attacks:
			if attack_type in [type(e) for e in gs.effects if e.duration > 1]:
				continue
			state = GameState.CreateFrom(gs)
			if part_b:
				state.player.hp -= 1
				if state.player.hp == 0:
					continue
			state.event_log.append('\n-- Player turn --')
			state.event_log.append('- {0} has {1} hp, {2} armor, {3} mana'.format(
				state.player.name,
				state.player.hp,
				state.player.armor,
				state.player.mana))
			state.event_log.append('- {0} has {1} hp'.format(
				state.boss.name,
				state.boss.hp))
			state.tick_effects()
			if state.player.hp <= 0:
				continue
			if state.boss.hp <= 0:
				return state

			attack = attack_type()
			if state.player.mana < attack.mana_cost:
				continue
			attack.cast(state.player, state.boss)
			state.player.mana -= attack.mana_cost
			state.mana_spent += attack.mana_cost
			state.event_log.append('Player casts {}'.format(attack.__class__.__name__))
			if attack.duration > 0:
				state.effects.append(attack)

			if state.boss.hp <= 0:
				return state

			# Boss's turn
			state.event_log.append('\n-- Boss turn --')
			state.tick_effects()
			if state.player.hp <= 0:
				continue
			if state.boss.hp <= 0:
				return state

			state.event_log.append(Melee().cast(state.boss, state.player))

			if gs.player.hp <= 0:
				continue

			unvisited_states.put(state)

	return None

def print_history(game_state):
	parents = deque()
	current_state = game_state
	while current_state is not None:
		parents.appendleft(current_state)
		current_state = current_state.parent
	for p in parents:
		for event in p.event_log:
			print(event)

def part_a(input):
	hp = input[0].split()[-1]
	damage = input[1].split()[-1]
	state = find_least_amount_of_mana_to_win(
		Character('Player', 50, 0, 500, 0, [MagicMissile, Drain, Poison, Shield, Recharge]),
		Character('Boss', int(hp), int(damage), 0, 0, [Melee])
	)
	#print_history(state)
	return str(state.mana_spent)

def part_b(input):
	hp = input[0].split()[-1]
	damage = input[1].split()[-1]
	state = find_least_amount_of_mana_to_win(
		Character('Player', 50, 0, 500, 0, [MagicMissile, Drain, Poison, Shield, Recharge]),
		Character('Boss', int(hp), int(damage), 0, 0, [Melee]),
		True
	)
	return str(state.mana_spent)

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
