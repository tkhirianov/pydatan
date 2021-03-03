from multiprocessing import Process, Queue
import os
import time

final_fibonacci_number = 40


def worker(task: int, process_index: int):
    def fib(n: int) -> int:
        return fib(n-1) + fib(n-2) if n > 2 else 1
    
    number = task
    answer = fib(number)
    print(f"worker {process_index}, PID={os.getpid()}: fib({number}) = {answer}")
    

def main():
    tasks = []
    for n in range(0, final_fibonacci_number + 1):
        tasks.append(n)

    workers = []
    for process_index in range(final_fibonacci_number + 1):
        worker_process = Process(target=worker, args=(tasks[process_index],
                                                      process_index,))
        workers.append(worker_process)
    print("Parent process prepared all the tasks.")

    start_time = time.perf_counter()
    for worker_process in workers:
        worker_process.start()
    print("Parent process started workers processes.")

    for worker_process in workers:
        worker_process.join()
    finish_time = time.perf_counter()
    print("Parent process joined all the workers processes. Duration:",
          finish_time - start_time)
    
    
if __name__ == '__main__':
    main()
