import threading
import time

"""

Python中提供的Event就是最简单的通信机制之一.
使用threading.Event可以使一个线程等待其他线程的通知，
我们把这个Event传递到线程对象中，
Event默认内置了一个标志，初始值为False。
一旦该线程通过wait()方法进入等待状态，直到另一个线程调用该Event的set()方法将内置标志设置为True时，
该Event会通知所有等待状态的线程恢复运行。

"""
class WorkThread(threading.Thread):
    def __init__(self,signal):
        threading.Thread.__init__(self)
        self.signal = signal

    def run(self):
        print("xxxx%s,xxxx...." %self.name)
        self.signal.wait()
        print("yyyyy%s,yyyy...." %self.name)


if __name__ == "__main__":
    singal = threading.Event()
    for i in range(0,3):
        thread = WorkThread(singal)
        thread.start()


    print("sleep 3")
    time.sleep(3)
    singal.set()



