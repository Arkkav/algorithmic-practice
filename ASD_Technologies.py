"""
начнем с простого
джуниор программист работает в нетфликс. он сделал массив из фильмов какие посмотрел пользователь "в лоб".
то есть матрицу 10 тыс на 10 тыс (например)
1 - если юзер посмотрел этот фильм. 0 - если не посмотрел.
задача:
1) сделать генератор такой матрицы
2) предложить структуру в какой хранить данные эффективно. много нулей в матрице - наверное не хорошо
3) скрипт который переводит данные из матрицы которую сделал наш джуниор в ваш формат
чем короче код тем лучше
простой скрипт (запускается в юпитере)
"""
import itertools


import random
from numpy import array
from scipy.sparse import csr_matrix, dok_matrix
n = 10000
m = 10000
a = [[random.randint(0, 1) for x in range(n)] for y in range(m)]
# A = array(a)


def sequence(a):
	for i in a:
		yield from i


g = sequence(a)
print(next(g))
print(next(g))
print(next(g))
print()

# print(a)
S = csr_matrix(a)
print(S)
# B = S.todense()
# print(B)
# print()


D = dok_matrix(a)
print(dict(D.items()))





"""
1. Генератор обхода матрицы: функция-генератор sequence(a) возвращает строку на каждой итерации,
а yield from i возвращает итератор каждой стрики i

"""





def run():
	pass


if __name__ == '__main__':
	run()
