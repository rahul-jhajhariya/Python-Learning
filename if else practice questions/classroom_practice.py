""" 
1. Write a program using nested if to check whether a number is positive,
negative, or zero, and if positive, also check whether it is even or odd.
"""

# num=5
# if num>0:
#     if num%2==0:
#         print("num is positive and even")
#     else:
#         print("num is positive and odd")
# elif num<0:
#     print("num is negative")
# else:
#     print("num is zero")

#------------------------------------------------------------------------------------------------------------------
"""
2. Write a program using nested if to find the greatest among three numbers.
"""
# a=5
# b=9
# c=7
# if a>b:
#     if a>c:
#         print("a is the greatest")
#     else:
#         print("c is the greatest")
# else:
#     if b>c:
#         print("b is the greatest")
#     else:
#         print("c is the greatest")

#------------------------------------------------------------------------------------------------------------------
"""
3. Write a program using nested if to check whether a student has passed or
failed, and if passed, assign a grade based on marks.
"""
# marks =int(input("Enter your marks: "))
# if marks>=40:
#     if marks>90:
#         print("A+")
#     elif marks>75:
#         print("A")
#     elif marks>60:
#         print("B")
#     else:
#         print("C")
# else:
#     print("you are fail")

#------------------------------------------------------------------------------------------------------------------
"""
4. Write a program using nested if to check whether a person is eligible to
vote, and if eligible, check whether they are a first-time voter.
"""
# age=56
# first-time= "true"
# if age>=18:
#     if first-time= "true":
#         print("He/She is a first time voter")
#     else:
#         print("old voter")
# else:
#         print("not eligible for voting ")

#------------------------------------------------------------------------------------------------------------------
"""
5. Write a program using nested if to check whether a number is divisible by 5, 
and if yes, check whether it is also divisible by 10.
"""
# num=20
# if num%5==0:
#     if num%10==0:
#         print("num is divisible by 5 and 10")
#     else:
#         print("num is divisible by 5")
# else:
#     print("num is not divisivle by 5")

#------------------------------------------------------------------------------------------------------------------
"""
6. Write a program using nested if to check whether a character is an
alphabet, and if it is an alphabet, check whether it is a vowel or consonant.
"""
# char="q"
# if char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
#     if char in "aeiouAEIOU":
#         print("character is a vowel")
#     else:
#         print("character is a consonent")
# else:
#     print("character is not a alphabet")

#------------------------------------------------------------------------------------------------------------------
"""
7. Write a program using nested if to check whether a person is eligible for a
job based on age, and if eligible, check whether they have the required qualification.
"""
# age=45
# required_qual="no"
# if age >25:
#     if required_qual=="yes":
#         print("you are eligible")
#     else:
#         print("you are not eligible")
# else:
#     print("you are not eligible")

#------------------------------------------------------------------------------------------------------------------
"""
8. Write a program using nested if to check whether a number is greater than 50, 
and if yes, check whether it is also greater than 100.
"""
# num=65
# if num>50:
#     if num>100:
#         print("the number is greater than 100")
#     else:
#         print("the number is greater than 50 but less than 100")
# else:
#     print("the number is not greater than 50")

#------------------------------------------------------------------------------------------------------------------
"""
9. Write a program using if-elif-else to check whether a number is positive,
negative, or zero.
"""
# num=5
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

#------------------------------------------------------------------------------------------------------------------
"""
10. Write a program using elif to assign grades based on marks:
A (90–100), B (80–89), C (70–79), D (60–69), F (below 60).
"""
# marks=50
# if marks>90:
#     print("A+")
# elif marks>80:
#     print("B")
# elif marks>70:
#     print("C")
# elif marks>60:
#     print("D")
# else:
#     print("F")

#------------------------------------------------------------------------------------------------------------------
"""
11. Write a program using elif to check whether a given day number (1–7)
corresponds to Monday–Sunday.
"""
# day=21
# dey=day%7
# if dey==1:
#     print("Monday")
# elif dey==2:
#     print("Tuesday")
# elif dey==3:
#     print("Wednesday")
# elif dey==4:
#     print("Thrusday")
# elif dey==5:
#     print("Friday")
# elif dey==6:
#     print("Saturday")
# else:
#     print("Sunday")

#------------------------------------------------------------------------------------------------------------------
"""
12. Write a program using elif to find the largest among three numbers.
"""
# a=5
# b=6
# c=8
# if a>b and a>c:
#     print("a is the greatest")
# elif b>c and b>a:
#     print("b is the greatest")
# else:
#     print("c is the greatest")

#------------------------------------------------------------------------------------------------------------------
"""
13. Write a program using elif to check whether a year is a leap year or not.
"""
# year=100
# if ((year%4==0 and year%100!=0) or year%400==0):
#     print("leap year")
# else:
#     print("not a leap year")

#------------------------------------------------------------------------------------------------------------------
"""
14. Write a program using elif to classify a person’s age group: Child, Teen, Adult, or Senior.
"""
# age=50
# if age>60:
#     print("senior")
# elif age>18:
#     print("adult")
# elif age>5:
#     print("teen")
# else:
#     print("child")

#------------------------------------------------------------------------------------------------------------------
"""
15. Write a program using elif to check whether a character is a vowel, consonant,
digit, or special character.
"""
# char="@"
# if char in "aeiouAEIOU":
#     print("vowel")
# elif char in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
#     print("consonent")
# elif char in "1234567890":
#     print("digit")
# else:
#     print("special character")

#------------------------------------------------------------------------------------------------------------------
"""
16. Write a program using elif to build a simple calculator for +, -, *, and /.
"""
# a=5
# b=6
# operation="/"
# if operation=="+":
#     print(a+b)
# elif operation=="*":
#     print(a*b)
# elif operation=="-":
#     print(a-b)
# else:
#     if b!=0:
#         print(a/b)
#     else:
#         print("denominator cannot be zero")

#------------------------------------------------------------------------------------------------------------------
"""
17. Write a program using elif to check whether a number is divisible by 2, 3, 5, or
none of them.
"""
# num=7
# if num%2==0:
#     print("divisible by 2")
# elif num%3==0:
#     print("divisible by 3")
# elif num%5==0:
#     print("divisible by 5")
# else:
#     print("none of them")

#------------------------------------------------------------------------------------------------------------------
"""
18. Write a program using elif to convert a numeric month value (1–12) into the month
name.
"""
# month = 5

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("may")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("Agust")
# elif month == 9:
#     print("Septamber")
# elif month == 10:
#     print("Octumber")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
# else:
#     print("Invalid month")

#------------------------------------------------------------------------------------------------------------------
"""
19. Write a program using elif to check the type of triangle: Equilateral, Isosceles, or
Scalene.
"""
# side1=5
# side2=7
# side3=7

# if side1+side2>side3 and side1+side3>side2 and side3+side2>side1:
#     if side1==side2==side3:
#         print("Equilateral")
#     elif side1==side2 or side1==side3 or side2==side3:
#         print("Isosceles")
#     else:
#         print("Scalene")
# else:
#     print("not a triangle")

#------------------------------------------------------------------------------------------------------------------
"""
20. Write a program using elif to determine the season based on month number.
"""
# month = "10"

# if month in "345":
#     print("Summer")
# elif month in "6789":
#     print("Monsoon")
# elif month in "10" or month in "11" :
#     print("Autumn")
# elif month in "12" or month in "12":
#     print("Winter")
# else:
#     print("Invalid month")

#------------------------------------------------------------------------------------------------------------------
"""
21. Write a program using elif to calculate electricity bill based on unit ranges.
"""
# unit=150
# bill=0
# if unit>400:
#     bill=(unit-400)*10 + (100*8) + (100*6) + (100*4) + (100*2)
# elif unit>300:
#     bill = (unit-300)*8 + (100*6) + (100*4) + (100*2)
# elif unit>200:
#     bill = (unit-200)*6 + (100*4) + (100*2)
# elif unit>100:
#     bill = (unit-100)*4 + (100*2)
# else:
#     bill = unit*2
# print(bill)

#------------------------------------------------------------------------------------------------------------------
"""
22. Write a program using elif to check whether a number is one-digit, two-digit,
three-digit, or more.
"""
# num=-50000
# if num<0:
#     num=num*(-1)

# if num>=1000 and num<=999:
#     print("4 digit number")
# elif num>=100 and num<=999:
#     print("3 digit number")
# elif num>=10 and num<=99:
#     print("2 digit number")
# elif num>=0 and num<=9:
#     print("1 digit number")
# else:
#     print("5 or more than 5 digit number")

#------------------------------------------------------------------------------------------------------------------
"""
23. Write a program using elif to check the result of a student: Distinction, First
Class, Second Class, Pass, or Fail.
"""
# percentage=50
# if percentage>90:
#     print("Distinction")
# elif percentage>80:
#     print("First class")
# elif percentage>70:
#     print("Second class")
# elif percentage>60:
#     print("Pass")
# else:
#     print("Fail")

#------------------------------------------------------------------------------------------------------------------
"""
24. Write a program using elif to convert percentage into grade category.
"""
# percentage=50
# if percentage>90:
#     print("A")
# elif percentage>80:
#     print("B")
# elif percentage>70:
#     print("C")
# elif percentage>60:
#     print("d")
# else:
#     print("F")

#------------------------------------------------------------------------------------------------------------------
"""
25. Write a program using elif to check traffic light action based on color input.
"""
# traffic_light="red"
# if traffic_light=="red":
#     print("stop")
# elif traffic_light=="orange":
#     print("slow")
# else:
#     print("go")

#------------------------------------------------------------------------------------------------------------------
"""
26. Write a program using elif to classify temperature as Cold, Moderate, or Hot.
"""
# temp=40
# if temp>40:
#     print("hot")
# elif temp>30:
#     print("moderate")
# else:
#     print("cold")

#------------------------------------------------------------------------------------------------------------------
"""
27. Write a program using elif to check whether a number is prime, composite, or
neither.
"""

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------