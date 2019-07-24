"""3.	Write a program to accept 2 different numbers from the user and print all the prime numbers from the user and print all the prime numbers."""

def is_prime(num):
   if num<2:
      return False
   for i in range(2,num//2+1):
      if num%i==0:
         return False
   return True
LB=int(input("enter lower bound"))
UB=int(input("enter upper bound"))
for i in range(LB,UB+1):
   if is_prime(i):
      print(i)

