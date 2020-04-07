import multiprocessing
import time

def proc1(pipe):
    pipe.send('hello')
    print('proc2 rec:', pipe.recv()) #recv一端，如果没有数据就会一直阻塞

def proc2(pipe):
    print('proc1 rec:', pipe.recv())
    pipe.send('hello, too')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    pipe = multiprocessing.Pipe(duplex=True) #单向管道，对象pipe[0]只有读的权限(recv)，而pipe[1]只有写的权限(send)。

    p1 = multiprocessing.Process(target=proc1, args=(pipe[1],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[0],))

    p2.start()
    p1.start()

    p1.join()
    p2.join()

'''
def proc1(pipe):
    for i in range(1,10):
        pipe.send(i)
        print("send {0} to pipe".format(i))
        time.sleep(1)
def proc2(pipe):
    n = 9
    while n >0:
        result = pipe.recv()
        print("recv {0} from pipe".format(result))
        n -= 1

def main():
    pipe = multiprocessing.Pipe(duplex=False)
    print(type(pipe))
    p1 = multiprocessing.Process(target=proc1,args=(pipe[1],))
    p2 = multiprocessing.Process(target=proc2,args=(pipe[0],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    pipe[0].close()
    pipe[1].close()

if __name__ == '__main__':
    main()
'''