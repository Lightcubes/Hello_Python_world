"""
revision history
    2020-06-20  initial version
    2020-06-21  add print() detail
    2020-06-22  add mutex to ensure print() work correctly
    2020-06-24  replace sleep with mutex on existing to provide better performance
    2020-06-25  use global variable to indicate subThread ending instead of mutex
    2020-06-25  enhanced final version of _thread
"""
import _thread as thread, time

threadNumber = 5
gmutex = thread.allocate_lock()
threadExitMutex = [thread.allocate_lock() for i in range(threadNumber)]
#exitIndicators = [False] * threadNumber


def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1/100*(myId+1))  # to give up the CPU
        '''
        (1)
        print("The length of %s is %d" % (s,x))
        d,i                 带符号的十进制整数
        o                   不带符号的八进制
        u                   不带符号的十进制
        x                   不带符号的十六进制（小写）
        X                   不带符号的十六进制（大写）
        e                   科学计数法表示的浮点数（小写）
        E                   科学计数法表示的浮点数（大写）
        f,F                 十进制浮点数
        g                   如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
        G                   如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
        C                   单字符（接受整数或者单字符字符串）
        r                   字符串（使用repr转换任意python对象)
        s                   字符串（使用str转换任意python对象）

        (2) 
        print('{0} and {1}'.format('Geeks', 'Portal')) 
        print('{1} and {0}'.format('Geeks', 'Portal'))
        
        output>>>
        Geeks and Portal
        Portal and Geeks 
        
        (3)
        without new line
        print(x, end = '')

        '''
        with mutex:
            print('Thread id: [%s] ===> loop is %s' % (myId, i))
    threadExitMutex[myId].acquire()
#    exitIndicators[myId] = True  //global variables


def main():
    for i in range(threadNumber):
        thread.start_new_thread(counter, (i, threadNumber * 10, gmutex))
    '''
    time.sleep(6)
    for mutex in threadExitMutex:
        while not mutex.locked(): pass
     '''
    while not all (mutex.locked() for mutex in threadExitMutex):
        time.sleep(1/100)
#   while False in exitIndicators: pass
    print("Exiting ... ...")


if __name__ == "__main__":
    main()
