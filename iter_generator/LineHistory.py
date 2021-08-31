#!/usr/bin/env python3

from collections import deque
import sys

class LineHistory():
    def __init__(self, lines, histlen = 3):
        self._lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):
        for lineno, line in enumerate(self._lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage {} file'.format(sys.argv[0]))
        exit(1)
    with open(sys.argv[1]) as f:
        lines = LineHistory(f, 5)
        for line in lines:
            # print(line, end='')
            if 'done' in line:
                for lno, l in lines.history:
                    print("{:4d}:{}".format(lno, l), end='')
