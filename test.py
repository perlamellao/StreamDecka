import threading
import time

def thread1():
    global a
    a=10
    print("Thread 1 {}".format(a))
    time.sleep(10)
    print("Thread 1 {}".format(a))
    
    
def thread2():
    global a
    time.sleep(2)
    print("Thread 2 {}".format(a))
    a=15

if __name__ == "__main__":
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()