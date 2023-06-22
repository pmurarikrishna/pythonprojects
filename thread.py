import threading
import time

def thread1():
    print("Thread 1")
    time.sleep(5)
    print("Thread 1 is completed")

def thread2():
    print("Thread 2")
    time.sleep(5)
    print("Thread 2 is completed")

def thread3():
    print("Thread 3")
    time.sleep(5)
    print("Thread 3 is completed")

def thread4():
    print("Thread 4")
    time.sleep(5)
    print("Thread 4 is completed")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t3 = threading.Thread(target=thread3)
t4 = threading.Thread(target=thread4)

t1.start()
t2.start()
t3.start()
t4.start()