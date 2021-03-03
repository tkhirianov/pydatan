from multiprocessing import Pool
import os
import time

workers_number = 4
final_fibonacci_number = 40


def fib(n: int) -> int:
    return fib(n-1) + fib(n-2) if n > 2 else 1
    

def main():
    tasks = list(range(1, final_fibonacci_number + 1))
    start_time = time.perf_counter()
    # Уход в паралельные вычисления:
    with Pool(workers_number) as pool_of_processes:
        answers = list(pool_of_processes.map(fib, tasks))
    # Всё, тут мы вышли из режима многозадачности. Работает один родительский процесс.
    finish_time = time.perf_counter()
    print("Duration:", finish_time - start_time)
    
    print(*answers)
    
if __name__ == '__main__':
    main()
