#!/usr/bin/env python3

class Node():
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
        yield self
        for n in self:
            yield from n.depth_first()
            # yield n.depth_first()
            

if __name__ == '__main__':
    root = Node(0)
    ch1 = Node(1)
    ch2 = Node(2)
    ch3 = Node(3)
    root.add_child(ch1)
    root.add_child(ch2)
    root.add_child(ch3)

    for ch in root:
        print(ch)

    for ch in root.depth_first():
        print(ch)
        
