"""
1. Sum of list elements Input: [1, 2,3, 4, 5]
"""
# lst=[1,2,3,4,5]
# sum=0
# for i in range(len(lst)):
#     sum+=lst[i]
# print(sum)

#-------------------------------------------------------------------------------------------------------
"""
2. Find the largest element in a list Input: [3, 7, 2, 9, 1]
"""
# lst=[3, 7, 2, 9, 1]
# mx=lst[0]
# for i in range(len(lst)):
#     if lst[i]>mx:
#         mx=lst[i]
# print(mx)

#-------------------------------------------------------------------------------------------------------
"""
3. Count even numbers in a list Input: [1, 2, 3, 4, 5, 6]
"""
# lst=[1, 2, 3, 4, 5, 6]
# count=0
# for i in range(len(lst)):
#     if lst[i]%2==0:
#         count+=1
# print(count)

#-------------------------------------------------------------------------------------------------------
"""
4. Reverse a list using a loop Input: [1, 2, 3, 4]
"""
# lst=[1, 2, 3, 4]
# rev=[]
# for i in range(len(lst)-1,-1,-1):
#     rev.append(lst[i])
# print(rev)

#-------------------------------------------------------------------------------------------------------
"""
5. Find the second largest element Input: [3, 7, 2, 9, 5]
"""
# lst=[3, 70, 2, 9, 5]
# largest=lst[0]
# sec_largest=lst[0]
# for i in range(len(lst)):
#     if lst[i]>largest:
#         sec_largest=largest
#         largest=lst[i]
#     elif lst[i]>sec_largest and lst[i]!=largest:
#         sec_largest=lst[i]
# print(sec_largest)

#-------------------------------------------------------------------------------------------------------
"""
6. Remove duplicates from a list (preserve order) Input: [1, 2, 2, 3, 1, 4]
"""
# lst=[1, 2, 2, 3, 1,5,5,5,5,5,6,6,6,6,6,7, 4]
# new_lst=[]
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print(new_lst)

#-------------------------------------------------------------------------------------------------------
"""
7. Find all elements greater than the average Input: [1, 2, 3, 4, 10]
"""
# lst=[1, 2, 3, 4,7,8,9, 10]
# sum=0
# new_lst=[]
# for num in lst:
#     sum+=num
# avg=sum/len(lst)
# for num in lst:
#     if num>avg:
#         new_lst.append(num)
# print(new_lst)

#-------------------------------------------------------------------------------------------------------
"""
8. Rotate a list to the left by k positions Input: [1,2,3,4,5], k=2
"""
# lst=[1,2,3,4,5]
# k=2
# for i in range(k):
#     first=lst.pop(0)
#     lst.append(first)
# print(lst)

#-------------------------------------------------------------------------------------------------------
"""
9. Find the longest consecutive sequence in a list Input: [1,2,3,10,11,12,13]
"""
# data= [1,2,3,4,6,5,10,11,12,13]
# data.sort()
# longest=[]
# current=[data[0]]
# for i in range(1,len(data)):
#     if data[i]==data[i-1]+1:
#         current.append(data[i])
#     else:
#         if len(current)>len(longest):
#             longest=current
#         current=[data[i]]
# if len(current)>len(longest):
#     longest=current
# print(longest)
# print(len(longest))

#-------------------------------------------------------------------------------------------------------
"""

"""
