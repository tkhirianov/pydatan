from numba import jit
import time

final_fibonacci_number = 40

@jit(nopython=True)
def fib(n: int) -> int:
    return fib(n-1) + fib(n-2) if n > 2 else 1
    

def main():
    tasks = list(range(0, final_fibonacci_number + 1))
    start_time = time.perf_counter()
    # Никаких параллельных вычислений! Работаем сами:
    answers = []
    for number in tasks:
        answers.append(fib(number))
    # Работает один родительский процесс по-прежнему.
    finish_time = time.perf_counter()
    print("Duration:", finish_time - start_time)
    
    print(*answers)
    
if __name__ == '__main__':
    main()
