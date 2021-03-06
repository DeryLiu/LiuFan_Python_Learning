'''
https://blog.ansheng.me/article/python-full-stack-way-threads-and-processes/

Thread：
线程是操作系统能够进行运算调度的最小单位，它被包含在进程之中，是进程中的实际运作单位，
一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。
在同一个进程内的线程的数据是可以进行互相访问的。
线程的切换使用过上下文来实现的，比如有一本书，有a和b这两个人(两个线程)看，a看完之后记录当前看到那一页哪一行，然后交给b看，b看完之后记录当前看到了那一页哪一行，此时a又要看了，那么a就通过上次记录的值(上下文)直接找到上次看到了哪里，然后继续往下看。

Process：
一个进程至少要包含一个线程，每个进程在启动的时候就会自动的启动一个线程，
进程里面的第一个线程就是主线程，每次在进程内创建的子线程都是由主线程进程创建和销毁，子线程也可以由主线程创建出来的线程创建和销毁线程。
进程是对各种资源管理的集合，比如要调用内存、CPU、网卡、声卡等，进程要操作上述的硬件之前都必须要创建一个线程，进程里面可以包含多个线程，QQ就是一个进程。
继续拿QQ来说，比如我现在打开了QQ的聊天窗口、个人信息窗口、设置窗口等，那么每一个打开的窗口都是一个线程，他们都在执行不同的任务，比如聊天窗口这个线程可以和好友进行互动，聊天，视频等，个人信息窗口我可以查看、修改自己的资料。
为了进程安全起见，所以两个进程之间的数据是不能够互相访问的(默认情况下)，比如自己写了一个应用程序，然后让别人运行起来，那么我的这个程序就可以访问用户启动的其他应用，我可以通过我自己的程序去访问QQ，然后拿到一些聊天记录等比较隐秘的信息，那么这个时候就不安全了，所以说进程与进程之间的数据是不可以互相访问的，而且每一个进程的内存是独立的。

进程与线程的区别：
线程是执行的指令集，进程是资源的集合
线程的启动速度要比进程的启动速度要快
两个线程的执行速度是一样的
进程与线程的运行速度是没有可比性的
线程共享创建它的进程的内存空间，进程的内存是独立的。
两个线程共享的数据都是同一份数据，两个子进程的数据不是共享的，而且数据是独立的;
同一个进程的线程之间可以直接交流，同一个主进程的多个子进程之间是不可以进行交流，如果两个进程之间需要通信，就必须要通过一个中间代理来实现;
一个新的线程很容易被创建，一个新的进程创建需要对父进程进行一次克隆
一个线程可以控制和操作同一个进程里的其他线程，线程与线程之间没有隶属关系，但是进程只能操作子进程
改变主线程，有可能会影响到其他线程的行为，但是对于父进程的修改是不会影响子进程;
'''

'''
多线程：
多线程在Python内实则就是一个假象，为什么这么说呢，因为CPU的处理速度是很快的，所以我们看起来以一个线程在执行多个任务，每个任务的执行速度是非常之快的，利用上下文切换来快速的切换任务，以至于我们根本感觉不到。

但是频繁的使用上下文切换也是要耗费一定的资源，因为单线程在每次切换任务的时候需要保存当前任务的上下文。

什么时候用到多线程？
首先IO操作是不占用CPU的，只有计算的时候才会占用CPU(譬如1+1=2)，Python中的多线程不适合CPU密集型的任务，适合IO密集型的任务(sockt server)。

启动多个线程
主进程在启动之后会启动一个主线程，下面的脚本中让主线程启动了多个子线程，然而启动的子线程是独立的，所以主线程不会等待子线程执行完毕，而是主线程继续往下执行，并行执行。

for i in range(50):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.start()

join()
join()方法可以让程序等待每一个线程之后完成之后再往下执行，又成为串行执行。

'''
# 让主线程阻塞，子现在并行执行
import threading
import time
def Princ(String):
    print('task', String)
    time.sleep(2)
# 执行子线程的时间
start_time = time.time()
# 存放线程的实例
t_objs = []
for i in range(50):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.start()
    # 为了不让后面的子线程阻塞，把当前的子线程放入到一个列表中
    t_objs.append(t)
# 循环所有子线程实例，等待所有子线程执行完毕
for t in t_objs:
    t.join()
# 当前时间减去开始时间就等于执行的过程中需要的时间
print(time.time() - start_time)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=EVENT=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''
Event

Event是线程间通信最间的机制之一：一个线程发送一个event信号，其他的线程则等待这个信号。用于主线程控制其他线程的执行。
Events 管理一个flag，这个flag可以使用set
()设置成True或者使用clear()重置为False，wait()则用于阻塞，在flag为True之前。flag默认为False。

选项	描述
Event.wait([timeout])	堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）
Event.set()	将标识位设为Ture
Event.clear()	将标识伴设为False
Event.isSet()	判断标识位是否为Ture
'''
import threading
def runthreading(event):
    print("Start...")
    event.wait()
    print("End...")
event_obj = threading.Event()
for n in range(10):
    t = threading.Thread(target=runthreading, args=(event_obj,))
    t.start()
event_obj.clear()
inp = input("True/False?>> ")
if inp == "True":
    event_obj.set()


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=守护进程=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''
守护进程(守护线程)
一个主进程可以启动多个守护进程，但是主进程必须要一直运行，如果主进程挂掉了，那么守护进程也会随之挂掉
程序会等待主线程(进程)执行完毕，但是不会等待守护进程(线程)
'''
import threading
import time
def Princ(String):
    print('task', String)
    time.sleep(2)
for i in range(50):
    t = threading.Thread(target=Princ, args=('t-%s' % (i),))
    t.setDaemon(True)  # 把当前线程设置为守护线程，要在start之前设置
    t.start()

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=场景预设=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
场景预设：
比如现在有一个FTP服务，每一个用户连接上去的时候都会创建一个守护线程，现在已经有300个用户连接上去了，就是说已经创建了300个守护线程，
但是突然之间FTP服务宕掉了，这个时候就不会等待守护线程执行完毕再退出，而是直接退出，如果是普通的线程，那么就会登台线程执行完毕再退出。
'''
from multiprocessing import Process
import time
def runprocess(arg):
    print(arg)
    time.sleep(2)
p = Process(target=runprocess, args=(11,))
p.daemon=True
p.start()
print("end")

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=信号量=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据
'''
import threading
import time
def run(n):
    semaphore.acquire()  # 获取信号，信号可以有多把锁
    time.sleep(1)  # 等待一秒钟
    print("run the thread: %s\n" % n)
    semaphore.release()  # 释放信号
t_objs = []
if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 声明一个信号量，最多允许5个线程同时运行
    for i in range(20):  # 运行20个线程
        t = threading.Thread(target=run, args=(i,))  # 创建线程
        t.start()  # 启动线程
        t_objs.append(t)
for t in t_objs:
    t.join()
print('>>>>>>>>>>>>>')

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=进程间通讯=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
默认情况下进程与进程之间是不可以互相通信的，若要实现互相通信则需要一个中间件，另个进程之间通过中间件来实现通信，下面是进程间通信的几种方式。
'''
# Queue：
from multiprocessing import Process, Queue
def ChildProcess(Q):
    Q.put(['Hello', None, 'World'])  # 在Queue里面上传一个列表
if __name__ == '__main__':
    q = Queue()  # 创建一个Queue
    p = Process(target=ChildProcess, args=(q,))  # 创建一个子进程，并把Queue传给子进程,相当于克隆了一份Queue
    p.start()  # 启动子进程
    print(q.get())  # 获取q中的数据
    p.join()

# Pipes
from multiprocessing import Process, Pipe
def ChildProcess(conn):
    conn.send(['Hello', None, 'World'])  # 写一段数据
    conn.close()  # 关闭
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 生成一个管道实例，parent_conn, child_conn管道的两头
    p = Process(target=ChildProcess, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # 收取消息
    p.join()

# 数据共享
from multiprocessing import Process, Manager
import os
def ChildProcess(Dict, List):
    Dict['k1'] = 'v1'
    Dict['k2'] = 'v2'
    List.append(os.getpid())  # 获取子进程的PID
    print(List)  # 输出列表中的内容
if __name__ == '__main__':
    manager = Manager()  # 生成Manager对象
    Dict = manager.dict()  # 生成一个可以在多个进程之间传递共享的字典
    List = manager.list()  # 生成一个字典
    ProcessList = []  # 创建一个空列表，存放进程的对象，等待子进程执行用于
    for i in range(10):  # 生成是个子进程
        p = Process(target=ChildProcess, args=(Dict, List))  # 创建一个子进程
        p.start()  # 启动
        ProcessList.append(p)  # 把子进程添加到p_list列表中
    for res in ProcessList:  # 循环所有的子进程
        res.join()  # 等待执行完毕
    print('\n')
    print(Dict)
    print(List)

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=进程池=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
同一时间启动多少个进程
'''
from multiprocessing import Pool
import time
def myFun(i):
    time.sleep(2)
    return i+100
def end_call(arg):
    print("end_call>>", arg)
p = Pool(5)  # 允许进程池内同时放入5个进程
for i in range(10):
    p.apply_async(func=myFun, args=(i,),callback=end_call) # # 平行执行,callback是主进程来调用
    # p.apply(func=Foo)  # 串行执行
print("end")
p.close()
p.join() # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=线程池=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
import queue
import threading
import contextlib
import time
StopEvent = object()
class ThreadPool(object):
    def __init__(self, max_num, max_task_num = None):
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        self.max_num = max_num
        self.cancel = False
        self.terminal = False
        self.generate_list = []
        self.free_list = []
    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if self.cancel:
            return
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            self.generate_thread()
        w = (func, args, callback,)
        self.q.put(w)
    def generate_thread(self):
        """
        创建一个线程
        """
        t = threading.Thread(target=self.call)
        t.start()
    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        current_thread = threading.currentThread()
        self.generate_list.append(current_thread)
        event = self.q.get()
        while event != StopEvent:
            func, arguments, callback = event
            try:
                result = func(*arguments)
                success = True
            except Exception as e:
                success = False
                result = None
            if callback is not None:
                try:
                    callback(success, result)
                except Exception as e:
                    pass
            with self.worker_state(self.free_list, current_thread):
                if self.terminal:
                    event = StopEvent
                else:
                    event = self.q.get()
        else:
            self.generate_list.remove(current_thread)
    def close(self):
        """
        执行完所有的任务后，所有线程停止
        """
        self.cancel = True
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1
    def terminate(self):
        """
        无论是否还有任务，终止线程
        """
        self.terminal = True
        while self.generate_list:
            self.q.put(StopEvent)
        self.q.queue.clear()
    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        用于记录线程中正在等待的线程数
        """
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)
# How to use
pool = ThreadPool(5)
def callback(status, result):
    # status, execute action status
    # result, execute action return value
    pass
def action(i):
    print(i)
for i in range(30):
    ret = pool.run(action, (i,), callback)
time.sleep(5)
print(len(pool.generate_list), len(pool.free_list))
print(len(pool.generate_list), len(pool.free_list))
pool.close()
pool.terminate()