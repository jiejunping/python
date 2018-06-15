import threading
import time

def run(number):
    # print(threading.current_thread().name + "\n")
    # print(threading.current_thread().getName() + "\n")
    print(threading.currentThread().getName() + "\n")
    print(number)


"""
测试线程为前台线程和后台线程执行情况
当前的t.setDaemon(False)默认为false. 为false表明当前线程为前台线程, 
主线程执行完毕后仍需等待前台线程执行完毕之后方能结束当前进程;
为true表明当前线程为后台线程, 主线程执行完毕后则当前进程结束, 不关注后台线程是否执行完毕
"""
def run2(number):
    time.sleep(1)
    print("current thread is : ", threading.currentThread().name)


#.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == "__main__":
    for i in range(10):
        # 创建的是一个线程 ,MainThread
        # mythread = threading.Thread(target=run(i))

        #创建的是多线程  target=表明线程所执行的函数, args= 表明函数的参数
        mythread = threading.Thread(target=run,args=(i,))
        mythread.start()

    for i in range(10,20):
        mythread2 = threading.Thread(target=run2, args=(i,))
        mythread2.setName(i)
        # mythread2.setDaemon(True)
        mythread2.start()
        # 该方法表示主线程必须在此位置等待子线程执行完毕后才能继续执行主线程后面的代码
        mythread2.join()

    print("main thread has been stopped")


