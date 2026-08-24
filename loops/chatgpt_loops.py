"""
1. Sum of digits
User se integer n lo aur loop ka use karke uske digits ka sum nikalo.
"""
# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num//=10
# print(sum)

#----------------------------------------------------------------------------------------------------
"""
2. Reverse a number
Loop ka use karke number ko reverse karo.
"""
# num=int(input("Enter a number: "))
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# print(rev)

#----------------------------------------------------------------------------------------------------
"""
3. Count digits
Number mein total kitne digits hain, loop se count karo.
"""
# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     count+=1
#     num//=10
# print(count)

#----------------------------------------------------------------------------------------------------
"""
4. Palindrome number
Check karo ki number palindrome hai ya nahi.
"""
# num=int(input("Enter a number: "))
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num//=10
# if temp==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

#----------------------------------------------------------------------------------------------------
"""
5. Factorial
Loop ka use karke n! calculate karo.
"""
# num=int(input("Enter a number: "))
# fac=1
# while num>0:
#     fac=fac*num
#     num-=1
# print(fac)

#----------------------------------------------------------------------------------------------------
"""
6. Prime number
Check karo ki given number prime hai ya nahi.
"""
# num=int(input("Enter a number: "))
# count=0
# n=1
# while n<=num:
#     if num%n==0:
#         count+=1
#     n+=1
# if count==2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

#----------------------------------------------------------------------------------------------------
"""
7. Print all factors
Given number ke saare factors print karo.
"""
# num=int(input("Enter a number: "))
# for i in range(1,(num//2)+2):
#     if num%i==0:
#         print(i,end=" ")
# print(num)

#----------------------------------------------------------------------------------------------------
"""
8. Count even and odd digits
Number ke andar kitne even aur odd digits hain, count karo.
"""
# num=int(input("Enter a number: "))
# even=0
# odd=0
# while num>0:
#     rem=num%10
#     if rem%2==0:
#         even+=1
#     else:
#         odd+=1
#     num//=10
# print(f"even = {even} , odd = {odd}")

#----------------------------------------------------------------------------------------------------
"""
9. Armstrong number
Check karo ki given number Armstrong number hai ya nahi.
"""
# num=int(input("Enter a number: "))
# temp=num
# digit=0
# sum=0
# while temp>0:
#     temp//=10
#     digit+=1
# temp=num
# while num>0:
#     rem=num%10
#     result=1
#     for i in range(1,digit+1):
#         result=result*rem
#     sum=sum+result
#     num//=10
# if temp==sum:
#     print("Armstrong number")
# else:
#     print("not a Armstrong number")

#----------------------------------------------------------------------------------------------------
"""
10. Multiplication tables
1 se 10 tak ke multiplication tables print karo using nested loops.
"""
# n=1
# while n<=10:
#     print(f"----Table of {n}----")
#     for i in range(1,11):
#         print(f"{n}X{i}={n*i}")
#     n+=1

#----------------------------------------------------------------------------------------------------
"""
11. Fibonacci series
First n Fibonacci numbers print karo.
"""
# n=int(input("Enter a number: "))
# print("0 1",end=" ")
# a=0
# b=1
# c=0
# while n>0:
#    c=a+b
#    print(c,end=" ")
#    a=b
#    b=c
#    n-=1

#----------------------------------------------------------------------------------------------------
"""
12. Prime numbers in a range
1 se 100 ke beech saare prime numbers print karo.
"""
# print("1",end=" ")
# for i in range(2,101):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=" ")

#----------------------------------------------------------------------------------------------------
"""
13. Perfect number
Check karo ki number perfect number hai ya nahi.
"""
num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
    print("Perfect number")
else:
    print("Not a perfect number")