import hashlib
import sys

def part_a(input):
	input = ''.join(input).strip()
	for i in range(0, sys.maxsize):
		m = hashlib.md5()
		m.update((input +str(i)).encode('utf-8'))
		digest = m.digest()
		if digest[0] == 0 and digest[1] == 0 and digest[2] & 0xF0 == 0:
			return str(i)
	return '0'

def part_b(input):
	input = ''.join(input).strip()
	for i in range(0, sys.maxsize):
		m = hashlib.md5()
		m.update((input +str(i)).encode('utf-8'))
		digest = m.digest()
		if digest[0] == 0 and digest[1] == 0 and digest[2] == 0:
			return str(i)
	return '0'

def solve(input):
	return {'a' : part_a(input), 'b' : part_b(input)}
