""" 3.Write a Python function to find the nth term of Fibonacci sequence and its
factorial.Return the result as a list."""
fibonacciList = [0,1]
factoriallist = list()
def fibo(N):
    for term in range(3, N + 1):
         value = fibonacciList[term - 2] + fibonacciList[term - 3]
         fibonacciList.append(value)

def factorial(num):
         fact = 1
         for i in range(1, num):
                fact = fact * i
                factoriallist.append(fact)


N = int(input("Enter your number: "))
fibo(N)
factorial(fibonacciList[N-1])
print(fibonacciList)
print(factoriallist)