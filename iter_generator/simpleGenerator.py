#!/usr/bin/env python3

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def countDown(count):
    print('start to count down from {}'.format(count))
    while count > 0:
        yield count
        count -= 1
    print('Count done')

if __name__ == '__main__':
    for n in frange(0, 5, 0.5):
        print(n)

    c = countDown(10)
    while True:
        try:
            print(next(c))
        except StopIteration:
            break
