
final_fibonacci_number = 40
fib = [0, 1] + [None]*(final_fibonacci_number - 1)
for i in range(2, final_fibonacci_number + 1):
    fib[i] = fib[i-1] + fib[i-2]
for i in range(0, final_fibonacci_number + 1):
    print(fib[i])
