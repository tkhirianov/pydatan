import _thread
import time

shared_variable = 0

def print_time(thread_name, delay):
    global shared_variable
    count = 0
    while count < 10:
        time.sleep(delay)
        count += 1
        shared_variable += 1
        print(f"{thread_name}: {time.ctime(time.time())}, {shared_variable}")

try:
    _thread.start_new_thread(print_time, ("Thread 1", 1))
    _thread.start_new_thread(print_time, ("Thread two", 1.5))
except:
    print("Unable to start threads")

while True:
    pass
