#!/home/arkkav/projects/algorithmic_practice/env2 python
# -*- coding: utf-8 -*-


def benchmark(iters):
	def actual_decorator(func):
		import time

		def wrapper(*args, **kwargs):
			total = 0
			for i in range(iters):
				start = time.time()
				return_value = func(*args, **kwargs)
				end = time.time()
				total = total + (end - start)
			print('[*] Среднее время выполнения функции {}: {} секунд.'.format(func.__name__ , total / iters))
			return return_value

		return wrapper

	return actual_decorator


@benchmark(iters=10000)
def is_even(value):
	return value % 2 == 0


# value % 2 == 0 требует деления и вычитания, побитовые операции проверяют только последний бит
@benchmark(iters=10000)
def is_even2(value):
	return value & 1 == 0


def run():
	n = 700000

	f = is_even(n)
	print(f)

	f = is_even2(n)
	print(f)


if __name__ == '__main__':
	run()
