# 1.1 Implement a recursive function to calculate the factorial of a given number.

def fact1(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact1(n-1)

number=int(input("enter the number: "))
res=fact1(number)
print(f"the factorial of the given {number} is",res)