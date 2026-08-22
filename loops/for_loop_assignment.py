"""
1. Print the numbers from 1 to 20 using a for loop. For every number, print "Even" if it is even and
"Odd" if it is odd.
"""
# for i in range(1,21):
#     if i%2==0:
#         print(i,"= Even")
#     else:
#         print(i,"= Odd")
#--------------------------------------------------------------------------------------------
"""
2. Use range() to print all numbers from 10 down to 1. For each number, also print "High" if the number
is greater than 5, otherwise print "Low".
"""
# for i in range(10,0,-1):
#     if i>5:
#         print(i,"= High")
#     else:
#         print(i,"= Low")

#--------------------------------------------------------------------------------------------
"""
3. Write a program using range(1, 51) that prints only the numbers divisible by 5.
"""
# for i in range(1,52):
#     if i%5==0:
#         print(i)

#--------------------------------------------------------------------------------------------
"""
4. Use a for loop with range(2, 31, 2). Print each number and classify it as "Small" when it is below 
15, otherwise "Large".
"""
# for i in range(2,32,2):
#     if i<15:
#         print(i,"= small")
#     else:
#         print(i,"= large")

#--------------------------------------------------------------------------------------------
"""
5. Use range(1, 40, 3) and print every generated value. If the value is divisible by 2 print "Divisible by
2"; otherwise print "Not divisible by 2".
"""
# for i in range(1,41,3):
#     if i%2==0:
#         print(i,"= divisible by 2")
#     else:
#         print(i,"= not divisible by 2")

#--------------------------------------------------------------------------------------------
"""
6. Print numbers from 1 to 30. For each number, use if/elif/else to print "Multiple of 3", "Multiple of
5", or "Other". Make sure the conditions are checked in a logical order.
"""
# for i in range(1,31):
#     if i%3==0:
#         print(i,"= multiple of 3")
#     elif i%5==0:
#         print(i,"= multiple of 5")
#     else:
#         print(i,"= other")

#--------------------------------------------------------------------------------------------
"""
7. Using range(50, 0, -5), print the values. If a value is greater than 25 print "Upper Half"; otherwise
print "Lower Half".
"""
# for i in range(50,0,-5):
#     if i>25:
#         print(i,"= upper half")
#     else:
#         print(i,"= lower half")

#--------------------------------------------------------------------------------------------
"""
8. Write a program using range(1, 101) that prints numbers which are divisible by both 3 and 4.
"""
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)

#--------------------------------------------------------------------------------------------
"""
9. Use range(1, 21). For each number, print "Positive" for numbers from 1 to 10 and "Above 10" for
numbers from 11 to 20. Do not use a second loop.
"""
# for i in range(1,22):
#     if i <=10:
#         print(i,"= positive")
#     else:
#         print(i,"= above 10")

#--------------------------------------------------------------------------------------------
"""
10. Print numbers from 20 down to 1 using a decreasing range(). For each number: print "Even > 10" if
it is even and greater than 10, "Odd > 10" if it is odd and greater than 10, otherwise print "10 or less".
"""
# for i in range(20,0,-1):
#     if i>10 and i%2==0:
#         print(i,"= even and greater than 10")
#     elif i>10 and i%2!=0:
#         print(i,"= odd and greater than 10")
#     else:
#         print(i,"= 10 or less")

#--------------------------------------------------------------------------------------------
"""
11. Use range(1, 31) to find and print the numbers that are divisible by 2 but not divisible by 3.
"""
# for i in range(1,31):
#     if i%2==0 and i%3!=0:
#         print(i)

#--------------------------------------------------------------------------------------------
"""
12. Use range(5, 51, 5). For each number, print "Low" for 5, 10, 15, "Medium" for 20, 25, 30, and
"High" for 35, 40, 45, 50. Use if/elif/else.
"""
# for i in range(5,51,5):
#     if i<20:
#         print(i,"= Low")
#     elif i<35:
#         print(i,"= Medium")
#     else:
#         print(i,"= High")

#--------------------------------------------------------------------------------------------
"""
13. Write a program using range(1, 16). If a number is divisible by 2 and 3, print "Both". If it is divisible
only by 2, print "Two". If it is divisible only by 3, print "Three". Otherwise print "Neither".
"""
# for i in range(1,32):
#     if i%2==0 and i%3==0:
#         print(i,"= Both")
#     elif i%2==0:
#         print(i,"= only by 2")
#     elif i%3==0:
#         print(i,"= only by 3")
#     else:
#         print(i,"= Neither")

#--------------------------------------------------------------------------------------------
"""
14. Use a loop with range(100, 49, -10). For each value, check whether it is greater than 75, equal to
70, or less than 70, and print an appropriate message using if/elif/else.
"""
# for i in range(100,49,-10):
#     if i>75:
#         print(i,"= Greater than 75")
#     elif i==75:
#         print(i,"= equal to 70")
#     else:
#         print(i,"= less than 70")

#--------------------------------------------------------------------------------------------
"""
15. Write a program using range(1, 61) to print every number. Classify each number as follows: "Fizz"
if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both 3 and 5, otherwise print the
number itself. Use only one for loop.
"""
for i in range(1,61):
    if i%3==0 and i%5==0:
        print(i,"= FizzBuzz")
    elif i%3==0:
        print(i,"= Fizz")
    elif i%5==0:
        print(i,"= Buzz")
    else:
        print(i)
#--------------------------------------------------------------------------------------------

