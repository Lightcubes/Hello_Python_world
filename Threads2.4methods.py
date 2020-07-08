import _thread as _thread
import threading
import time


def action(i):
    print(i ** 32)


# subclass with state
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):  # redefine run for action
        print(self.i ** 16)


Mythread(2).start()  # start invokes run()

# pass action in
thread = threading.Thread(target=(lambda: action(2)))  # run invokes target
thread.start()

# same but no lambda wrapper for state
threading.Thread(target=action, args=(2,)).start()  # callable plus its args

# basic thread module
_thread.start_new_thread(action, (2,))  # all-function interface

time.sleep(1)
