from codewars import MemoryManager
import pytest


def test_1():
	mem = MemoryManager([None] * 256)
	with pytest.raises(OSError) as excinfo:
		mem.allocate(512)
	assert "Cannot allocate more memory than exists" in str(excinfo.value)

	pointer1 = mem.allocate(128)
	assert pointer1 >= 0

	with pytest.raises(OSError) as excinfo:
		mem.allocate(129)
	assert "Cannot allocate more memory than exists" in str(excinfo.value)

# def it_2():
# 	mem = MemoryManager([None] * 256)
# 	for i in range(256):
# 		Test.expect(0 <= mem.allocate(1) < 256, "Should be able to allocate 256 blocks of size 1")
#
# def it_3():
# 	mem = MemoryManager([None] * 64)
# 	pointer1 = mem.allocate(32)
# 	pointer2 = mem.allocate(32)
# 	mem.release(pointer1)
# 	Test.expect(mem.allocate(32) < 64, "Should be able to allocate 32 bits")
#
# def it_4():
# 	mem = MemoryManager([None] * 64)
# 	pointer1 = mem.allocate(16)
# 	pointer2 = mem.allocate(16)
# 	pointer3 = mem.allocate(16)
# 	pointer4 = mem.allocate(16)
# 	mem.release(pointer2)
# 	mem.release(pointer3);
# 	Test.expect(mem.allocate(32) < 64, "Deallocated memory should be merged")
#
# def it_5():
# 	mem = MemoryManager([None] * 64)
# 	Test.expect_error("No memory has been allocated", lambda: mem.write(1, 1))
#


def test_6():
	array = [None] * 64
	a, b, c, d = 0, 1, 31, 32
	mem = MemoryManager(array)
	pointer1 = mem.allocate(32)
	mem.write(pointer1, a)
	mem.write(pointer1 + b, b)
	mem.write(pointer1 + c, c)
	with pytest.raises(OSError) as excinfo:
		mem.write(pointer1 + d, d)
	assert "should throw on write to allocated pointer + 32" in str(excinfo.value)
	assert array[pointer1 + a] == a
	assert array[pointer1 + b] == b
	assert array[pointer1 + c] == c
	assert array[pointer1 + d] != d
#
# def it_7():
# 	mem = MemoryManager([None] * 64)
# 	Test.expect_error("No memory has been allocated", lambda: mem.read(1))
#


def test_8():
	mem = MemoryManager([None] * 64)
	pointer1 = mem.allocate(32)
	mem.write(pointer1, 1)
	mem.read(pointer1)
	assert mem.read(pointer1) == 1
	assert mem.read(pointer1 + 1) is None
