"""
revision history
    2020-06-20  initial version
    2020-06-21  add print() detail
    2020-06-22  add mutex to ensure print() work correctly
    2020-06-24  replace sleep with mutex on existing to provide better performance
"""
import _thread as thread, time

threadNumber = 5
mutex = thread.allocate_lock()
threadExitMutex = [thread.allocate_lock() for i in range(threadNumber)]


def counter(myId, count):
    for i in range(count):
        # time.sleep(1)
        '''
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

        print('{0} and {1}'.format('Geeks', 'Portal')) 
        print('{1} and {0}'.format('Geeks', 'Portal'))

        output>>>
        Geeks and Portal
        Portal and Geeks 

        without new line
        print(x, end = '')

        '''
        mutex.acquire()
        print('Thread id: [%s] ===> loop is %s' % (myId, i))
        mutex.release()
    threadExitMutex[myId].acquire()


def main():
    for i in range(threadNumber):
        thread.start_new_thread(counter, (i, threadNumber * 2))
    # time.sleep(6)
    for mutex in threadExitMutex:
        while not mutex.locked(): pass
    print("Exiting ... ...")


if __name__ == "__main__":
    main()


