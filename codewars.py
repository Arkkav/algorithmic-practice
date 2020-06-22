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


# import gmpy2, itertools
#
# def sequence():
#     n = 2
#     while True:
#         yield from str(n)
#         n = gmpy2.next_prime(n)
#
# solve = lambda s, l: ''.join(itertools.islice(sequence(), s, s+l))

# --------------------------------------------------------
'''
In this Kata, you will be given a series of times at which an alarm goes off. Your task will be to determine the maximum time interval between alarms. Each alarm starts ringing at the beginning of the corresponding minute and rings for exactly one minute. The times in the array are not in chronological order. Ignore duplicate times, if any.

For example:
solve(["14:51"]) = "23:59". If the alarm goes off now, it will not go off for another 23 hours and 59 minutes.
solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not go off is 11 hours and 40 minutes.
In the second example, the alarm goes off 4 times in a day.
'''
from datetime import timedelta, datetime
# s = ["23:00","04:22","18:05","06:24"]
# s = ["14:51"]
s = ["21:14", "15:34", "14:51", "06:25", "15:30"]


def solve_time(arr):
	if len(arr) == 1:
		return "23:59"
	a = sorted([datetime.strptime(i, '%H:%M') for i in arr])
	g = timedelta(days=1)
	minute = timedelta(minutes=1)
	d = []

	for i in range(-1, len(a) - 1):
		c = a[i+1] - a[i] - minute
		if a[i+1] < a[i]:
			c = c + g
		d.append(c)

	a = max(d).total_seconds()
	hours = a // 3600
	a = a - (hours * 3600)
	minutes = a // 60

	return '{:02}:{:02}'.format(int(hours), int(minutes))

# def solve(arr):
#     k = sorted(int(x[:2])*60 + int(x[3:]) for x in arr)
#     z = [(k[i] - k[i-1])%1440 for i in range(len(k))]
#     return len(k) > 1 and '{:02}:{:02}'.format(*divmod(max(z)-1,60)) or "23:59"


#-----------------------------------------------------------

"""
Just another day in the world of Minecraft, Steve is getting ready to start his next exciting project -- building a railway system!
But first, Steve needs to melt some iron ores in the furnace to get the main building blocks of rails -- iron ingots.Alt text

Each iron ingot takes 11 seconds* to produce. Steve needs a lot of them, and he has the following fuel options to add into the furnace:

Buckets of lava, each lasts 800 seconds*Alt text
Blaze rod, each lasts 120 secondsAlt text
Coals, each lasts 80 secondsAlt text
Blocks of Wood, each lasts 15 secondsAlt text
Sticks, each lasts 1 second*Alt text
In Ruby: Write a function calc_fuel that calculates the minimum amount of fuel needed to produce a certain number of iron ingots. 
In Python: Write a function calc_fuel that calculates the minimum amount of fuel needed to produce a certain number of iron ingots. 
This function should return a dictionary of the form {"lava": 2, "blaze rod": 1, "coal": 1, "wood": 0, "stick": 0}
"""


def calc_fuel(n):
	fuel = {"lava": 800, "blaze rod": 120, "coal": 80, "wood": 15, "stick": 1}
	need = n * 11
	amount = {"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0}
	for key, value in fuel.items():
		if need >= value:
			d = need // value
			amount[key] += d
			need -= value * d
	return amount
#-----------------------------------------------------------
"""
Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. 
It is played between two or more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" 
are pictured on the board, each connecting two specific board squares. (Source Wikipedia)
Your task is to make a simple class called SnakesLadders. The test cases will call the method play(die1, die2) independantly 
of the state of the game or the player turn. The variables die1 and die2 are the die thrown in a turn and are both integers between 1 and 6. 
The player will move the sum of die1 and die2.

Rules
1.  There are two players and both start off the board on square 0.

2.  Player 1 starts and alternates with player 2.

3.  You follow the numbers up the board in order 1=>100

4.  If the value of both die are the same then that player will have another go.

5.  Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square at the top of the ladder. (even if you roll a double).

6.  Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you roll a double).

7.  Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

8.  If the Player rolled a double and lands on the finish square “100” without any remaining moves then the Player wins the game and does not have to roll again.

Returns
Return Player n Wins!. Where n is winning player that has landed on square 100 without any remainding moves left.

Return Game over! if a player has won and another player tries to play.

Otherwise return Player n is on square x. Where n is the current player and x is the sqaure they are currently on.
"""


class SnakesLadders():

	def __init__(self):

		self.Snakes = ((6, 16), (11, 49), (25, 46), (19, 62), (60, 64), (53, 74), (68, 89), (88, 92), (75, 95), (80, 99))
		self.Ladders = (
			(2, 38), (7, 14), (15, 26), (8, 31), (21, 42), (36, 44), (28, 84), (51, 67), (71, 91), (87, 94), (78, 98)
		)
		self.players = 2
		self.player_pos = [0 for i in range(self.players)]
		self.cursor = 0
		self.game_over = False

	def play(self, die1, die2):
		if self.game_over:
			return 'Game over!'
		self.player_pos[self.cursor] += die1 + die2

		if self.player_pos[self.cursor] == 100:
			self.game_over = True
			return 'Player {} Wins!'.format(str(self.cursor + 1))
		elif self.player_pos[self.cursor] > 100:
			self.player_pos[self.cursor] = 100 + 100 - self.player_pos[self.cursor]

		i = 0
		while i <= len(self.Snakes) - 1:
			if self.player_pos[self.cursor] == self.Snakes[i][1]:
				self.player_pos[self.cursor] = self.Snakes[i][0]
				i = 0
			i += 1

		i = 0
		while i <= len(self.Ladders) - 1:
			if self.player_pos[self.cursor] == self.Ladders[i][0]:
				self.player_pos[self.cursor] = self.Ladders[i][1]
				i = 0
			i += 1

		s = 'Player {} is on square {}'.format(str(self.cursor + 1), str(self.player_pos[self.cursor]))
		if die1 == die2:
			pass
		elif self.cursor == self.players - 1:
			self.cursor = 0
		else:
			self.cursor += 1
		return s

# можно было Snakes и Ladders сделать в одном словаре и доставать по get

def run():
	print(calc_fuel(37))


if __name__ == '__main__':
	run()
