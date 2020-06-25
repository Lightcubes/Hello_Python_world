import threading

stdoutmutex = threading.Lock()
threads = []
threadsNumber = 10

class testThreading(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('Thread id: [%s] ===> in loop %s' % (self.myId, i))

def main():
    for i in range(threadsNumber):
        thread = testThreading(i, threadsNumber * 5, stdoutmutex)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()               # wait for thread exits

    print ('Main exiting')


if __name__ == "__main__":
    main()





