"""6.	Write a program to accept a number from the user; then display the reverse of the entered number.
(Example: Entered number = 12345; Reversed number = 54321)"""
N=int(input("enter a number:"))
rev=0
temp=N
while temp>0:
   rev=rev*10+(temp%10)
   temp=temp//10
if rev==N:
   print(f"{N} is palindrome")
else:
   print(f"{N} is not palindrome")