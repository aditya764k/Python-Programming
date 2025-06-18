def factorial(n):

    if (n < 2):
        return 1
    else:
        return n * factorial(n-1)
num = int(input("enter a number : "))
result= factorial(num)
print('Factorial of 5 is : ', result)