import multiprocessing
from time import sleep, ctime
import os

def super_play(file_, time):
    for i in range(2):
        print('Start playing: %s! %s' %(file_, ctime()))
        # print(os.getpid())
        sleep(time)

lists = {'爱情买卖.mp3':3, '阿凡达.mp4':5, '我和你.mp3':4}
processes = []
files = range(len(lists))

for file, time in lists.items():
    p = multiprocessing.Process(target=super_play, args=(file, time))
    processes.append(p)

if __name__ == '__main__':
    for i in files:
        processes[i].start()

    for i in files:
        processes[i].join()

    print('end: %s' %ctime())