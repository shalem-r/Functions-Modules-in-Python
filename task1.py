def factorial(num):
    # For 0 and 1
    if num == 1 or num == 0:
        return 1
    # For -ve numbers
    elif num<0:
        print("No factorial for -ve numbers")
    # For numbers greater than or equal to 2
    # recursion
    # else:
    #     return num * (factorial(num-1))
    # Using For loop
    else:
        result = 1
        for i in range(2, num + 1):
            result = result * i
        return result

num = int(input("Enter a number: "))

if factorial(num) is not None:
    print("Factorial of", num, "is",factorial(num))