def iterativeFibonacci(n):
    fib = [1, 1]
    if n == 0 or n == 1:
        return 1
    
    count = 1
    while count <= n:
        fib[count % 2] = fib[0] + fib [1]
        count += 1

    return fib[count % 2]
# test
num1 = int(input("Enter number(iterative) : "))
print(iterativeFibonacci(num1))


def recursiveFibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursiveFibonacci(n - 1) + recursiveFibonacci( n - 2)
# test
num2 = int(input("Enter number(recursive) : "))
print(recursiveFibonacci(num2))