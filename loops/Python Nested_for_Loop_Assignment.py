"""
1. Consider 2 <= x <= 5 and 1 <= y <= 4. Use nested for loops to print every possible
pair (x, y) and also print the total number of pairs.
"""
# count=0
# for x in range(2,6):
#     for y in range(1,5):
#         print(f"({x},{y})",end=" ")
#         count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
2. For 1 <= x <= 6 and 1 <= y <= 5, print only the pairs where x != y. Also print how
many non-repeating pairs were found.
"""
# count=0
# for x in range(1,7):
#     for y in range(1,6):
#         if x!=y:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
3. For 1 <= x <= 6 and 1 <= y <= 6, print only the pairs where x == y. Count the
matching pairs.
"""
# count=0
# for x in range(1,7):
#     for y in range(1,7):
#         if x==y:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
4. For 1 <= x <= 9 and 0 <= y <= 9, print only the pairs for which x + y == 10. Print the
total count.
"""
# count=0
# for x in range(1,10):
#     for y in range(0,10):
#         if x+y==10:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
5. For 1 <= x <= 9 and 1 <= y <= 9, print every pair for which 10 <= x + y <= 15. Also
count them.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if x+y>=10 and x+y<=15:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
6. For 2 <= x <= 9 and 0 <= y <= 6, print only the pairs for which the product x * y is
even. Print the total number of valid pairs.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x*y)%2==0:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
7. For 1 <= x <= 8 and 1 <= y <= 8, print only the pairs for which x * y > x + y
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x*y)>(x+y):
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
8. For 1 <= x <= 9 and 1 <= y <= 9, print only the pairs for which x * y == x + y. Also
print their count.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x*y)==(x+y):
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
9. For 2 <= x <= 9 and 0 <= y <= 6, print only the pairs satisfying 0 <= x - y <= 5.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if x-y>=0 and x-y<=5:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
10. For 2 <= x <= 9 and 0 <= y <= 6, find and print the maximum value of x * y and the
pair (x, y) that produces it.
"""
# value=0
# max_pair=()
# for x in range(1,10):
#     for y in range(1,10):
#         if x*y>value:
#             value=x*y
#             max_pair=(x,y)
# print(value,max_pair)

#-----------------------------------------------------------------------------------------
"""
11. For 1 <= x <= 7 and 1 <= y <= 7, print only the pairs where x + y is odd.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x+y)%2!=0:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
12. For 1 <= x <= 8 and 1 <= y <= 8, print only the pairs where x + y is divisible by 3.
Also count the valid pairs.
"""

# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x+y)%3==0:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
13. For 1 <= x <= 8 and 1 <= y <= 8, print only the pairs where both x and y are even.
"""
# count=0
# for x in range(1,10):
#     if x%2==0:
#         for y in range(1,10):
#             if y%2==0:
#                 print(f"({x},{y})",end=" ")
#                 count+=1
#         print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
14. For 1 <= x <= 9 and 1 <= y <= 9, print only the pairs where both numbers are odd
and x + y > 10.
"""
# count=0
# for x in range(1,10):
#     if x%2!=0:
#         for y in range(1,10):
#             if y%2!=0 and (x+y)>10:
#                 print(f"({x},{y})",end=" ")
#                 count+=1
#         print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
15. For 1 <= x <= 9 and 1 <= y <= 9, print only the pairs where the absolute difference
between x and y is exactly 2. (Do not use lists.)
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x-y)==2 or (y-x)==2:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
16. For 1 <= x <= 9 and 1 <= y <= 9, print only the pairs where x + y is a multiple of 4
and x != y.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x+y)%4==0 and x!=y:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
17. For 1 <= x <= 8 and 1 <= y <= 8, find the pair with the smallest positive product
subject to x + y > 8. Print the product and the pair.
"""
# count=0
# positive_product=1000
# pair=()
# for x in range(1,10):
#     for y in range(1,10):
#         if (x+y)>8:
#             product=x*y
#             if product<positive_product:
#                 positive_product=product
#                 pair=(x,y)
#     print()
# print(positive_product,pair)

#-----------------------------------------------------------------------------------------
"""
18. For 1 <= x <= 9 and 1 <= y <= 9, print pairs where x < y and x + y is even. Also
count the pairs.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if x<y and (x+y)%2==0:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
19. For 2 <= x <= 9 and 1 <= y <= 7, print pairs where x * y is greater than 20 but less
than 40. Print the total count.
"""
# count=0
# for x in range(1,10):
#     for y in range(1,10):
#         if (x*y)>20 and (x*y)<40:
#             print(f"({x},{y})",end=" ")
#             count+=1
#     print()
# print(count)

#-----------------------------------------------------------------------------------------
"""
20. For 1 <= x <= 9 and 1 <= y <= 9, find the pair(s) having the largest sum x + y
among pairs where x * y is even. Print the maximum sum and the pair(s) producing it.
"""
# count=0
# max_sum=0
# pair=()
# for x in range(1,10):
#     for y in range(1,10):
#         if (x*y)%2==0:
#             if (x+y)>max_sum:
#                 max_sum=x+y
#                 pair=(x,y)
#     print()
# print(max_sum,pair)

#-----------------------------------------------------------------------------------------