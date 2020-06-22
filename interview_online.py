some_guy = 'Fred'
first_names = []
first_names.append(some_guy)

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'

print(some_guy, first_names, another_list_of_names)

#-----------------------------------------
def func(type_='s'):
	if type_ == 's':
		return 'Mark'
	elif type_ == 'i':
		return 20


def dec(func, type_):
	x = 8
	def wrapper():
		value = func(type_)
		if isinstance(value, int):
			return value * x
		elif isinstance(value, basestring):
			return 'Hi' + value
	return wrapper

print dec(func, 'i')()

#-------------------------------------------

class Parent(object):
	x = 1

class Child1(Parent):
	pass

class Child2(Parent):
	pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
