import os
import sys
import argparse
import days
from days import *
import time
import util

def exec_day(day_number):
	file_contents = util.get_file_contents('day' +day_number +'.txt')
	func = getattr(days, 'day' +day_number).solve
	return func(file_contents)

def run_day(day):
	start_time = time.time()
	print(exec_day(day))
	end_time = time.time()
	print('Execution took %0.3f ms' % ((end_time - start_time) * 1000.0))

def run_all():
	start_time = time.time()
	for f in os.listdir('inputs'):
		day = f.replace('day', '').replace('.txt', '')
		start_time_day = time.time()
		print('Day' +day)
		print(' ' +str(exec_day(day)))
		end_time_day = time.time()
		print(' Execution took %0.3f ms' % ((end_time_day - start_time_day) * 1000.0))
	end_time = time.time()
	print('-'*30)
	print('Execution of all days took %0.3f ms' % ((end_time - start_time) * 1000.0))

def create_table():
	result = {}
	for f in os.listdir('inputs'):
		day = f.replace('day', '').replace('.txt', '')
		file_contents = util.get_file_contents('day' +day +'.txt')
		result[day] = {}

		start_part_a = time.time()
		getattr(days, 'day' +day).part_a(file_contents)
		end_part_a = time.time()
		result[day]['part_a'] = int((end_part_a - start_part_a) * 10000) / 10

		start_part_b = time.time()
		getattr(days, 'day' +day).part_b(file_contents)
		end_part_b = time.time()
		result[day]['part_b'] = int((end_part_b - start_part_b) * 10000) / 10

	print('day'.ljust(4) +'part_a'.rjust(8) +'part_b'.rjust(8))
	for k, v in result.items():
		print(k.ljust(4) +str(v['part_a']).rjust(8) +str(v['part_b']).rjust(8))
	print('-'*30)

def main():
	parser = argparse.ArgumentParser(prog='AdventOfCode2015')
	parser.add_argument('-d', '--day', type=str, help='The day to execute.')
	parser.add_argument('-a', '--all', action='store_true', help='Run all days.')
	parser.add_argument('-t', '--table', action='store_true', help='Create a table of running times.')
	args = parser.parse_args()

	if args.day != None:
		run_day(args.day)
	elif args.all == True:
		run_all()
	elif args.table == True:
		create_table()
	else:
		print('No arguments, doing nothing.')

if __name__ == '__main__':
	sys.exit(main())
