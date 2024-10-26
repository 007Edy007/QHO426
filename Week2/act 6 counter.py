print("enter the 1st number")
number1 = int(input())
print("enter the 2nd number")
number2 = int(input())
print("enter the 3rd number")
number3 = int(input())
even = 0
odd = 0
if number1%2 == 0:
    even = even + 1
else:
    odd = odd + 1
if number2%2 == 0:
    even = even + 1
else:
    odd = odd + 1
if number3%2 == 0:
    even = even + 1
else:
    odd = odd + 1
print (f"there are {even} even numbers and {odd} odd numbers")

