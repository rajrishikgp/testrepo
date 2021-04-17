#number is even or divisible by 4
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))


if num1 % 2 == 0:
    print("First number is even")
else:
    print("First number is odd")

if num2 % 4 == 0:
    print ("Second number is divisible by 4")
else:
    print("Second number is not divisible by 4")