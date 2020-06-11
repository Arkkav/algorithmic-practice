'''
Cut all b elements from all a
'''
a = []
b = [1, 2]


def array_diff(a, b):
	c = []
	for i in a:
		if i not in b:
			c.append(i)
	return c

# -------------------------------------
'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
'''
l = [1, 2, 'a', 'b']


def filter_list(l):
	c = []
	for i in l:
		b = type("")
		if type(i) != b:
			c.append(i)
	return c

# -------------------------------------
'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
'''


# a = 'AAAABBBCCDAABBB'
# b = 'ABBCcAD'
# c = [1,2,2,3,3]


def unique_in_order(a):
	if not a:
		return []
	n = [a[0]]
	for i in range(1, len(a)):
		if a[i] != a[i - 1]:
			n.append(a[i])
	return n


# -------------------------------------
# word = "din"
# word = "recede"
word = "Success"
# word = "(( @"
def duplicate_encode(word):
	"""
	The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

	Examples
	"din"      =>  "((("
	"recede"   =>  "()()()"
	"Success"  =>  ")())())"
	"(( @"     =>  "))(("
	"""

	word = word.lower()
	a = set(word)
	s = ''
	if len(a) == len(word):
		s = '(' * (len(word))
	else:
		for i in word:
			if word.count(i) > 1:
				s += ')'
			else:
				s += '('
	return s


# # best
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# -------------------------------------
'''
Consider a sequence made up of the consecutive prime numbers. This infinite sequence would start with:

"2357111317192329313741434753596167717379..."
You will be given two numbers: a and b, and your task will be to return b elements starting from index a in this sequence.

For example:
solve(10,5) == `19232` Because these are 5 elements from index 10 in the sequence.
'''


def solve(a, b):
	from math import sqrt

	lst = [2]
	list_str = '2'
	i = 3
	f = True
	while f:
		if (i > 10) and (i % 10 == 5):
			i += 2
			continue
		for j in lst:
			if j > int((sqrt(i)) + 1):
				lst.append(i)
				list_str += str(i)
				break
			if i % j == 0:
				break
		else:
			lst.append(i)
			list_str += str(i)
		i += 2
		if len(list_str) >= (a + b):
			list_str = list_str[a:a + b]
			f = False

	return list_str
# --------------------------------------------------------
'''
In this Kata, you will be given a series of times at which an alarm goes off. Your task will be to determine the maximum time interval between alarms. Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute. The times in the array are not in chronological order. Ignore duplicate times, if any.

For example:
solve(["14:51"]) = "23:59". If the alarm goes off now, it will not go off for another 23 hours and 59 minutes.
solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not go off is 11 hours and 40 minutes.
In the second example, the alarm goes off 4 times in a day.
'''
from datetime import time, timedelta


def run():
	print(solve(2, 7))


if __name__ == '__main__':
	run()
