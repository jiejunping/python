import threading,time

"""
Python的threading模块为我们提供了线程锁功能,
在threading中提供RLock对象,RLock对象内部维护着一个Lock对象，
它是一种可重入锁。对于Lock对象而言，如果一个线程连续两次进行acquire操作，
那么由于第一次acquire之后没有release，第二次acquire将挂起线程。
这会导致Lock对象永远不会release，使得线程死锁。
而RLock对象允许一个线程多次对其进行acquire操作，
因为在其内部通过一个counter变量维护着线程acquire的次数。
而且每一次的acquire操作必须有一个release操作与之对应，
在所有的release操作完成之后，别的线程才能申请该RLock对象

Semaphore 信号量锁, 该锁允许一定数量的线程同时操作数据
event 事件机制锁, 根据Flag的真假来控制线程
condition 条件锁, 只有满足某条件时候才能释放线程

"""
mylock = threading.RLock()
semaphore = threading.BoundedSemaphore(5);
cd = threading.Condition()

num = 0

#自定义线程类需要继承threading.Thread类
class WorkThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name

    #run(self) 线程启动之后会执行该方法
    def run(self):
        global num
        while True:
            # 从该句开始加锁
            mylock.acquire()
            print('\n%s locked, number: %d' %(self.t_name,num))
            if num >= 4:
                #释放锁
                mylock.release()
                print('\n%s released, number: %d' % (self.t_name, num))
                break
            num +=1
            print('\n%s locked, number: %d' %(self.t_name,num))
            #释放锁
            mylock.release()

def semaphoreTest():
    semaphore.acquire()
    print("\ncurrent thread is: %s"%(threading.currentThread().name))
    time.sleep(1)
    semaphore.release()

def lockTest():
    thread1 = WorkThread("A-worker")
    thread2 = WorkThread("B-worker")

    thread1.start()
    thread2.start()

def condtionTest():
    cd.acquire()
    #设置放行的条件, 该方法接受condition函数的返回值
    cd.wait_for(condtion)
    print(threading.currentThread().name)
    cd.release()

def condtion():
    inputString = input("input your condition: ")
    print(inputString)
    if inputString == "yes":
        return True
    return  False



if __name__ == '__main__':
    lockTest()
    for i in range(10):
        thread = threading.Thread(target=semaphoreTest)
        thread.setName(i)
        thread.start()

    for i in range(10,13):
        threadcondtion = threading.Thread(target=condtionTest)
        threadcondtion.setName(i)
        threadcondtion.start()
        threadcondtion.join()

    print("\nmain thread has been stopped")




