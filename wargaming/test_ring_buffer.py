#!/home/arkkav/projects/algorithmic_practice/env2 python
# -*- coding: utf-8 -*-
from ring_buffer_node import Node, LinkedList
import pytest


def test_defaults():
	"""Без использования параметров, следует ссылаться на значения по умолчанию."""
	t1 = Node()
	t2 = LinkedList(3)

	assert t1.value is None
	assert t1.next_node is None
	assert t2.head is None
	assert t2.tail is None
	assert t2.capacity == 3
	assert t2.size == 0


# @pytest.mark.run_these_please
def test_sample1():
	assert (1, 1, 2) == (1, 1, 2)


def test_sample2():
	assert 1 <= 5


def test_sample3():
	assert 5 >= 1

