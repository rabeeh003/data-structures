def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
    
print(factorial(5))

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci( num - 2)

print(fibonacci(6))
