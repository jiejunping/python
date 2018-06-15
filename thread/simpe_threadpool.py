import threading,queue,time

#queue先进先出队列
class ThreadPool(object):
    def __init__(self,max_num=10):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return  self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def test(pool,i):
    time.sleep(1)
    print("current thread is : " , i)
    pool.add_thread()


if __name__ == "__main__":
    p = ThreadPool()
    for i in range(20):
        thread = p.get_thread()
        t = thread(target=test,args=(p,i))
        t.start()

    print("main thread has been stopped")





