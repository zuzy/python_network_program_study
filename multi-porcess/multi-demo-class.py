#!/usr/bin/python3

import time
import random

from multiprocessing import Process, Queue, current_process, freeze_support
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double, c_int
import ctypes

#
# Function run by worker processes
#

def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = calculate(func, args)
        output.put(result)

def worker_qs(queues):
    input = queues.tq
    output = queues.dq
    val = queues.v
    # v_char
    for func, args in iter(input.get, 'STOP'):
        result, val.value = calculate(func, args)
        # queues.str.value[:] = bytearray(result.encode())
        output.put(result)

# def worker_arg(arg):
#     input = queues.tq
#     output = queues.dq
#     val = queues.v
#     # v_char
#     for func, args in iter(input.get, 'STOP'):
#         result, val.value = calculate(func, args)
#         # queues.str.value[:] = bytearray(result.encode())
#         output.put(result)

#
# Function used to calculate result
#

def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % \
        (current_process().name, func.__name__, args, result), result

#
# Functions referenced by tasks
#

def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b


class Queues:
    def __init__(self, task_queue, done_queue):
        self.tq = task_queue
        self.dq = done_queue
        self.v = Value(ctypes.c_int)
        # self.v_char = Value(ctypes.c_char_p)
        self.str = Array(ctypes.c_char, 128)

class TestArg:
    def __init__(self, testq, doneq):
        super().__init__()
        self.q = Queues(testq, doneq)

def test():
    NUMBER_OF_PROCESSES = 4
    TASKS1 = [(mul, (i, 7)) for i in range(20)]
    TASKS2 = [(plus, (i, 8)) for i in range(10)]

    # Create queues
    task_queue = Queue()
    done_queue = Queue()
    # val = Value(ctypes.c_int, 0)

    # qs = Queues(task_queue, done_queue)
    a = TestArg(task_queue, done_queue)

    # Submit tasks
    for task in TASKS1:
        task_queue.put(task)

    # Start worker processes
    for _ in range(NUMBER_OF_PROCESSES):
        # Process(target=worker, args=(task_queue, done_queue)).start()
        # Process(target=worker_qs, args=(qs, )).start()
        Process(target=worker_qs, args=(a.q, )).start()

    # Get and print results
    print('Unordered results:')
    for i in range(len(TASKS1)):
        # print('\t', done_queue.get(), qs.v.value)
        print('\t', done_queue.get(), a.q.v.value)

    # Add more tasks using `put()`
    for task in TASKS2:
        task_queue.put(task)

    # Get and print some more results
    for i in range(len(TASKS2)):
        # print('\t', done_queue.get(), qs.v.value)
        print('\t', done_queue.get(), a.q.v.value)

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')


if __name__ == '__main__':
    freeze_support()
    test()