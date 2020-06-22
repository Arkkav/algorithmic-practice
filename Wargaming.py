#!/home/arkkav/projects/algorithmic_practice/env2 python
# -*- coding: utf-8 -*-
"""
Ниже приведенные задания являются обязательными и помогут опередить насколько легко Вам будет справляться
с поставленными задачами на нашей стажировке.Желаем удачи!**Вопрос 1**

Задание № 1 (обязательно к выполнению). На языке Python или С/С++, написать алгоритм (функцию) определения
четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.

Python example: def isEven(value):return value%2==0

C/C++ example: bool isEven(int value){return value%2==0;}

Задание № 2. (Обязательно к выполнению). На языках Python(2.7) и/или С++, написать минимум по 2 класса реализовывающих
циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Задание № 3. (Дополнительно, будет бонусом). На языке Python или С/С++, написать функцию, которая быстрее всего
(по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел
(в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.

"""
## 1 --------------------------------------------
# def benchmark(iters):
# 	def actual_decorator(func):
# 		import time
#
# 		def wrapper(*args, **kwargs):
# 			total = 0
# 			for i in range(iters):
# 				start = time.time()
# 				return_value = func(*args, **kwargs)
# 				end = time.time()
# 				total = total + (end - start)
# 			print('[*] Среднее время выполнения функции {}: {} секунд.'.format(func.__name__ , total / iters))
# 			return return_value
#
# 		return wrapper
#
# 	return actual_decorator
#
#
# # @benchmark(iters=1)
# # def fetch_webpage(url):
# # 	import requests
# # 	webpage = requests.get(url)
# # 	return webpage.text
#
#
# # webpage = fetch_webpage('https://google.com')
# # print(webpage)
#
# @benchmark(iters=10000)
# def is_even(value):
# 	return value % 2 == 0
#
#
# # value % 2 == 0 требует деления и вычитания, побитовые операции проверяют только последний бит
# @benchmark(iters=10000)
# def is_even2(value):
# 	return value & 1 == 0
#
# n = 700000
#
# f = is_even(n)
# print(f)
#
# f = is_even2(n)
# print(f)


# def run():
# 	print()
#
#
# if __name__ == '__main__':
# 	run()


## 2 --------------------------------------------
import numpy as np


class RingBuffer(object):
    def __init__(self, size_max, default_value=0.0, dtype=float):
        """initialization"""
        self.size_max = size_max

        self._data = np.empty(size_max, dtype=dtype)
        self._data.fill(default_value)

        self.size = 0

    def append(self, value):
        """append an element"""
        self._data = np.roll(self._data, 1)
        self._data[0] = value

        self.size += 1

        if self.size == self.size_max:
            self.__class__  = RingBufferFull

    def get_all(self):
        """return a list of elements from the oldest to the newest"""
        return(self._data)

    def get_partial(self):
        return(self.get_all()[0:self.size])

    def __getitem__(self, key):
        """get element"""
        return(self._data[key])

    def __repr__(self):
        """return string representation"""
        s = self._data.__repr__()
        s = s + '\t' + str(self.size)
        s = s + '\t' + self.get_all()[::-1].__repr__()
        s = s + '\t' + self.get_partial()[::-1].__repr__()
        return(s)


class RingBufferFull(RingBuffer):
    def append(self, value):
        """append an element when buffer is full"""
        self._data = np.roll(self._data, 1)
        self._data[0] = value


# -------------------------------------------
class Node(object):
    __slots__ = ['value', 'next_node', ]

    def __init__(self, value=None):
        self.value = value
        self.next_node = None


# class LinkedListIterator:
#     m_RingBuffer = None
#     m_Index = None
#
#     '''Ring Buffer Iterator'''
#     def __init__(self, rb):
#         self.m_RingBuffer = rb
#         self.m_Index = 0
#
#     def __next__(self):
#         if self.m_Index >= self.m_RingBuffer.size:
#             raise StopIteration
#         self.m_Index += 1
#         return self.m_RingBuffer.GetItem(self.m_Index + self.m_RingBuffer.head - 1)


class LinkedList(object):
    __slots__ = ['head', ]

    def __init__(self):
        self.head = None

    def __contains__(self, value):
        last_node = self.head
        while last_node:
            if value == last_node.value:
                return True
            else:
                last_node = last_node.next_node
        return False

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def __getitem__(self, index):
        last_node = self.head
        i = 0
        while i <= index:
            if i == index:
                return last_node.value
            i = i + 1
            last_node = last_node.next_node

    def remove_first_by_value(self, value):
        head_node = self.head
        if head_node is not None:
            if head_node.value == value:
                self.head = head_node.next_node
                head_node = None
                return
        while head_node is not None:
            if head_node.value == value:
                break
            last_node = head_node
            head_node = head_node.next_node
        if head_node is None:
            return
        last_node.next_node = head_node.next_node
        head_node = None
