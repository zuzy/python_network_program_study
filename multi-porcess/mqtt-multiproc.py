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
class Worker:
    status = Value(c_int)
    def __init__(self):
        super().__init__()
        self.tq = Queue()
        self.dq = Queue()
        self.st = Value(c_int)

    def proc(self):
        input = self.tq
        output = self.dq
        val = self.st
        # v_char
        for func, args in iter(input.get, 'STOP'):
            result, val.value = Worker.calculate(func, args)
            # queues.str.value[:] = bytearray(result.encode())
            output.put(result)
    
    @classmethod
    def calculate(cls, func, args):
        result = func(*args)
        cls.status.value = result
        return 'i:%d %s says that %s%s = %s' % \
            (cls.status.value, current_process().name, func.__name__, args, result), result

def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b

class Worker_Cls:
    tq = Queue()
    dq = Queue()
    obj = None
    def __init__(self):
        super().__init__()
        self.st = Value(c_int)
        self.number_to_test = 1
        Worker_Cls.obj = self
        self.isServer = True

    def proc(self):
        input = Worker_Cls.tq
        output = Worker_Cls.dq
        val = self.st
        # v_char
        # for func, args in iter(input.get, 'STOP'):
        for func, args in iter(input.get, 'STOP'):
            # result, val.value = Worker_Cls.calculate(func, args)
            result, val.value = self.calculate(func, args)
            # queues.str.value[:] = bytearray(result.encode())
            output.put(result)
    
    def test_self(self):
        print("self number: {} {}".format(self.number_to_test, current_process().name), flush=True)
        self.number_to_test += 1
    
    # @classmethod
    # def calculate(cls, func, args):
    #     result = func(*args)
    #     cls.obj.test_self()
    #     return '%s says that %s%s = %s' % \
    #         (current_process().name, func.__name__, args, result), result
    
    def calculate(self, func, args):
        result = func(*args)
        self.test_self()
        print("isServer {}".format(self.isServer))
        return '%s says that %s%s = %s' % \
            (current_process().name, func.__name__, args, result), result

    @classmethod
    def mul(cls, a, b):
        time.sleep(0.5*random.random())
        return a * b
    @classmethod
    def plus(cls, a, b):
        time.sleep(0.5*random.random())
        return a + b


#
# Functions referenced by tasks
#


def test():
    NUMBER_OF_PROCESSES = 4

    # Create queues
    # wk = Worker()
    wk = Worker_Cls()
    TASKS1 = [(wk.mul, (i, 7)) for i in range(20)]
    TASKS2 = [(wk.plus, (i, 8)) for i in range(10)]

    # TASKS1 = [(mul, (i, 7)) for i in range(20)]
    # TASKS2 = [(plus, (i, 8)) for i in range(10)]
    # task_queue = Queue()
    # done_queue = Queue()
    # val = Value(ctypes.c_int, 0)

    # qs = Queues(task_queue, done_queue)
    # a = TestArg(task_queue, done_queue)

    # Submit tasks
    for task in TASKS1:
        wk.tq.put(task)
        # task_queue.put(task)

    # Start worker processes
    for _ in range(NUMBER_OF_PROCESSES):
        # Process(target=worker, args=(task_queue, done_queue)).start()
        # Process(target=worker_qs, args=(qs, )).start()
        Process(target=wk.proc).start()

    # Get and print results
    print('Unordered results:')
    for i in range(len(TASKS1)):
        # print('\t', done_queue.get(), qs.v.value)
        print('\t', wk.dq.get(), wk.st.value)

    # Add more tasks using `put()`
    for task in TASKS2:
        wk.tq.put(task)

    # Get and print some more results
    for i in range(len(TASKS2)):
        # print('\t', done_queue.get(), qs.v.value)
        print('\t', wk.dq.get(), wk.st.value)

    # Tell child processes to stop
    for i in range(NUMBER_OF_PROCESSES):
        wk.tq.put('STOP')

    while True:
        time.sleep(1)


if __name__ == '__main__':
    # freeze_support()
    test()