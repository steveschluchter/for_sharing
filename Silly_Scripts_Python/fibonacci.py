#!/usr/bin/python

from sys import argv

#Some exposure to loops, recursion, and Fibonacci numbers

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    

n = int(argv[1])
print(fibonacci_recursive(n))

def fibonacci_loop(n):

    fib_arr = [1,1]
    
    if n == 1 or n == 2:
        return fib_arr[n]
    else:
        for i in range(2,n):
            fib_arr.append(fib_arr[i-1] + fib_arr[i-2])

        return fib_arr[-1]
    

print(fibonacci_loop(n))
    

