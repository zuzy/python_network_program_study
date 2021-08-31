#!/usr/bin/env python3


class Node2():
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirst(self)


class DepthFirst(object):
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                nextChild = next(self._child_iter)
                return nextChild
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

if __name__ == '__main__':
    root = Node2(0)
    ch1 = Node2(1)
    ch2 = Node2(2)
    ch3 = Node2((3, 4))
    root.add_child(ch1)
    root.add_child(ch2)
    root.add_child(ch3)

    for ch in root:
        print(ch)

    for ch in root.depth_first():
        print(ch)

                
        
        
