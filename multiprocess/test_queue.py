import  multiprocessing
import os
import time
# from queue import Queue (Queue用在多线程中，作为多线程中target的参数，用在多进程时会报TypeError: can't pickle _thread.lock objects错误)
from multiprocessing import Queue #(Queue用在多进程里，作为多进程中target的参数)

import process


def inputQ(queue, i):
    info = str(os.getpid()) + '(put):' + str(i)
    queue.put(info)
    print(info)

def outputQ(queue, lock):
    while not queue.empty():
        info = queue.get()
        lock.acquire()
        print(str(os.getpid()) + '(get):' + info)
        lock.release()


if __name__ == '__main__':
    record1 = []
    record2 = []
    lock = multiprocessing.Lock()
    queue = Queue(3)

    for i in range(10):
        process = multiprocessing.Process(target=inputQ, args=(queue, i))
        process.start()
        record1.append(process)


    for i in range(10):
        process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()

    for p in record2:
        p.join()



