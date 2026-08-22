"""
1. Write a program using a while loop to print the numbers from 1 to 20.
"""
# n=1
# while n<21:
#     print(n)
#     n+=1

#--------------------------------------------------------------------------------------------
"""
2. Write a program to print all even numbers from 2 to 40 using a while loop.
"""
# n=2
# while n<=40:
#     print(n)
#     n+=2

#--------------------------------------------------------------------------------------------
"""
3. Write a program to print the numbers from 50 down to 1 using a while loop.
"""
# n=50
# while n>=1:
#     print(n)
#     n-=1

#--------------------------------------------------------------------------------------------
"""
4. Write a program to calculate and print the sum of numbers from 1 to 50 using a while loop.
"""
# n=1
# sum=0
# while n<=50:
#     sum+=n
#     n+=1
# print(sum)

#--------------------------------------------------------------------------------------------
"""
5. Write a program to calculate the sum of all odd numbers between 1 and 49 using a while loop.
"""
# n=1
# sum=0
# while n<=49:
#     if n%2!=0:
#         sum+=n
#     n+=1
# print(sum)

#--------------------------------------------------------------------------------------------
"""
6. Write a program that takes a positive integer n and prints its multiplication table from 1 to 10 using a while
loop.
""" 
# n=5
# i=1
# while i<11:
#     print(f"{n}X{i}={n*i}")
#     i+=1

#--------------------------------------------------------------------------------------------
"""
7. Write a program that takes a positive integer and counts how many digits it contains using a while loop.
Example: 58392 -> 5 digits.
"""
# n=12345
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)

#--------------------------------------------------------------------------------------------
"""
8. Write a program that takes an integer and prints its digits one by one from right to left using a while loop.
Example: 4721 -> 1 2 7 4.
"""
# n=4721
# while n>0:
#     rem=n%10
#     print(rem)
#     n=n//10

#--------------------------------------------------------------------------------------------
"""
9. Write a program to reverse an integer using a while loop. Example: 5832 -> 2385.
"""
# n=5832
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)

#--------------------------------------------------------------------------------------------
"""
10. Write a program to find the sum of all digits of an integer using a while loop. Example: 5832 -> 18.
"""
# n=5832
# sum=0
# while n>0:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# print(sum)

#--------------------------------------------------------------------------------------------
"""
11. Write a program to find the largest digit in an integer using a while loop. Example: 5832 -> 8.
"""
# n=858329
# max=0
# while n>0:
#     rem=n%10
#     if rem>max:
#         max = rem
#     n=n//10
# print(max)

#--------------------------------------------------------------------------------------------
"""
12. Write a program to count how many times the digit 5 appears in an integer using a while loop. Example:
155258 -> 3 times.
"""
# n=1552558
# count=0
# while n>0:
#     rem=n%10
#     if rem==5:
#         count+=1
#     n=n//10
# print(count)

#--------------------------------------------------------------------------------------------
"""
13. Write a program to check whether a given integer is a palindrome using a while loop. Example: 1221 ->
palindrome; 1234 -> not a palindrome.
"""
# n=1221
# temp=n
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# if rev==temp:
#     print("palindrome")
# else:
#     print("not a palindrome")

#--------------------------------------------------------------------------------------------
"""
14. Write a program to calculate the factorial of a positive integer using a while loop. Example: 5 -> 120.
"""
# n=6
# fac=1
# while n>0:
#     fac=fac*n
#     n-=1
# print(fac)

#--------------------------------------------------------------------------------------------
"""
15. Write a program to calculate base^power without using the exponent operator (**) or any built-in power
function. Use a while loop.
"""
# n=5
# power=3
# result=1
# while power>0:
#     result=result*n
#     power-=1
# print(result)

#--------------------------------------------------------------------------------------------
"""
16. Write a program to print the first n terms of the sequence 2, 4, 6, 8, 10... using a while loop.
"""
# n=6
# seq=2
# while n>0:
#     print(seq)
#     seq+=2
#     n-=1
#--------------------------------------------------------------------------------------------
"""
17. Write a program to print the first n terms of the sequence 1, 3, 6, 10, 15... using a while loop. Each term is
formed by adding the next counting number.
"""
# n=6
# num=0
# count=1
# while n>0:
#     num=num+count
#     count+=1
#     n-=1
#     print(num,end=" ")

#--------------------------------------------------------------------------------------------
"""
18. Write a program that repeatedly asks the user to enter a number until the user enters 0. At the end, print
the sum of all non-zero numbers entered.
"""
# sum=0
# while True:
#     num=int(input("Enter a number:"))
#     if num==0:
#         break
#     sum=sum+num
# print(sum)

#--------------------------------------------------------------------------------------------
"""
19. Write a program that repeatedly asks the user to enter marks until the user enters -1. Count how many
entered marks are passing (50 or above) and how many are failing (below 50). Assume valid marks are 0 to
100.
"""
# pas=0
# fail=0
# while True:
#     marks=int(input("Enter your marks:"))
#     if marks<0 or marks>100:
#         break
#     if marks>=50:
#         pas+=1
#     if marks<50:
#         fail+=1
# print(f"fail = {fail} pass = {pas}")

#--------------------------------------------------------------------------------------------
"""
20. Write a program for a simple PIN check using a while loop. Give the user a maximum of 3 attempts to
enter the correct PIN. Print Access Granted when correct; otherwise print Account Locked after 3 wrong
attempts.
"""
# attempts=3
# correct_pin=123456
# while True:
#     pin=int(input("Enter your pin: "))
#     if pin==correct_pin:
#         print("access is granted")
#         break
#     else:
#         attempts-=1
#         print(f"access is denied, you have {attempts} attempts left")
#     if attempts==0:
#         print("your account is locked after 3 wrong attempts")
#         break

#--------------------------------------------------------------------------------------------