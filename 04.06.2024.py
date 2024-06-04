import threading
import time

def func(name):
    print('Start', name)
    time.sleep(0.5)
    print('End', name)


t1 = threading.Thread(target=func, args=('1', ))
t2 = threading.Thread(target=func, args=('2', ))
t3 = threading.Thread(target=func, args=('3', ))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


