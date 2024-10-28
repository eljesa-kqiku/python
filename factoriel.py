def iterativeFactoriel(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
# test
num1 = int(input("Enter number(iterative)s : "))
print(iterativeFactoriel(num1))


def recursiveFactoriel(n):
    if n == 0:
        return 1
    return n * recursiveFactoriel(n - 1)
# test
num2 = int(input("Enter number(recursive) : "))
print(recursiveFactoriel(num2))

