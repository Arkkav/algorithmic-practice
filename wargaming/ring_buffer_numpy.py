import numpy as np


class RingBuffer(object):
	__slots__ = ['size_max', 'default_value', '_data', 'size', ]

	def __init__(self, size_max, default_value=0.0, dtype=float):
		self.size_max = size_max
		self.default_value = default_value
		self._data = np.empty(size_max, dtype=dtype)
		self._data.fill(self.default_value)
		self.size = 0

	def append(self, value):
		self._data = np.roll(self._data, 1)
		self._data[0] = value
		if self.size != self.size_max:
			self.size += 1

	def pop(self):
		if self.size == 0:
			return self.default_value
		curr = self._data[self.size - 1]
		self._data[self.size - 1] = self.default_value
		self.size -= 1
		return curr

	def get_all(self):
		return self._data

	def get_partial(self):
		return self.get_all()[0:self.size]

	def __getitem__(self, key):
		return self._data[key]

	def __repr__(self):
		# s = self._data.__repr__()
		# s = s + '\t' + str(self.size)
		# s = s + '\t' + self.get_all()[::-1].__repr__()
		# s = s + '\t' + self.get_partial()[::-1].__repr__()
		return " ".join([str(i) for i in self])


# class RingBufferFull(RingBuffer):
#     def append(self, value):
#         self._data = np.roll(self._data, 1)
#         self._data[0] = value

def run():
	a = RingBuffer(3)
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
	# a.append(3)
	# a.append(4)
	# a.append(5)
	# a.pop()
	# for i in a:
	# 	print(i)

	# print(a.get_partial())
	# print(a.get_all())
	# print(a.size)
	print(a.__repr__())


if __name__ == '__main__':
	run()
