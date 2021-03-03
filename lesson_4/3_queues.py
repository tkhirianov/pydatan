from multiprocessing import Process, Queue
import os
import time

workers_number = 2
final_fibonacci_number = 40


def worker(tasks: Queue, answers: Queue, process_index: int):
    def fib(n: int) -> int:
        return fib(n-1) + fib(n-2) if n > 2 else 1
    
    while not tasks.empty():  # пока очередь не пуста выполняем одну очередную задачу
        number = tasks.get()
        answer = fib(number)
        answers.put((process_index, os.getpid(), number, answer,))
        #print(f"worker {process_index}, PID={os.getpid()}: fib({number}) = {answer}")
    

def main():
    tasks = Queue()
    answers = Queue()
    for n in range(1, final_fibonacci_number + 1):
        tasks.put(n)

    workers = []
    for process_index in range(workers_number):
        worker_process = Process(target = worker,
                                 args = (tasks, answers, process_index,))
        workers.append(worker_process)
    print("Parent process queued all the tasks.")

    start_time = time.perf_counter()
    for worker_process in workers:
        worker_process.start()
    print("Parent process started workers processes.")

    for worker_process in workers:
        worker_process.join()
    # Всё, тут мы вышли из режима многозадачности. Работает один родительский процесс.
    finish_time = time.perf_counter()
    print("Parent process joined all the workers processes. Duration:",
          finish_time - start_time)

    # Отладочная распечатка результатов
    ordered_answers = []
    while not answers.empty():
        process_index, PID, number, answer = answers.get()
        ordered_answers.append((number, answer,))
        print(f"worker {process_index}, PID={PID}: fib({number}) = {answer}")

    # Красивая распечатка полученных результатов:
    ordered_answers.sort()
    print(*(answer for number, answer in ordered_answers))
    
if __name__ == '__main__':
    main()
