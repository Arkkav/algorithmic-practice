class Node(object):
	__slots__ = ['value', 'next_node', ]

	def __init__(self, value=None):
		self.value = value
		self.next_node = None

	def __repr__(self):
		return str(self.value)


class LinkedList(object):
	__slots__ = ['head', 'tail', 'size', 'capacity', ]

	def __init__(self, capacity):
		self.head = self.tail = None
		self.size = 0
		self.capacity = capacity

	def __iter__(self):
		curr = self.head
		for i in range(self.size):
			yield curr
			curr = curr.next_node

	def __repr__(self):
		s = []
		if self.head is None:
			return s
		return " ".join([str(i) for i in self])

	def append(self, new_value):
		new_node = Node(new_value)
		if self.head is None:
			self.size += 1
			self.head = self.tail = new_node
		elif self.size < self.capacity:
			self.size += 1
			self.tail.next_node = new_node
			self.tail = new_node
		else:
			self.head = self.head.next_node
			self.tail.next_node = new_node
			self.tail = new_node
			self.tail.next_node = self.head

	def pop(self):
		if self.head is None:
			return None
		curr_head = self.head
		self.head = self.head.next_node
		self.size -= 1
		return curr_head


def run():
	a = LinkedList(3)
	a.append(1)
	a.append(2)
	a.append(3)
	a.append(4)
	a.append(5)
	a.pop()
	a.pop()
	a.append(6)
	a.pop()
	a.append(7)
	a.pop()
	a.pop()
	a.pop()
	a.append(1)
	a.append(2)
	a.append(3)
	a.append(4)
	a.append(5)
	a.pop()
	for i in a:
		print(i)

	print(a.__repr__())


if __name__ == '__main__':
	run()
