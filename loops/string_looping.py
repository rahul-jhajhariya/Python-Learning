"""
1. Direct indexing - print each character
Write a direct indexing loop that prints every character of "PYTHON" on a separate line.
"""
# st="PYTHON"
# for i in st:
#     print(i)

#--------------------------------------------------------------------------------------------
"""
2. Indirect indexing - print each character
Write an indirect indexing loop that prints every character of "PYTHON" on a separate line.
"""
# st="PYTHON"
# for i in range(len(st)):
#     print(st[i])

#--------------------------------------------------------------------------------------------
"""
3. Print with a space
Use direct indexing to print the characters of "HELLO" on one line with a space between each character.
"""
# st="HELLO"
# for i in st:
#     print(i,end=" ")

#--------------------------------------------------------------------------------------------
"""
4. Print positions
Use indirect indexing to print both the index and character for the string "CODE". Example format: 0 C.
"""
# st="CODE"
# for i in range(len(st)):
#     print(i,st[i])

#--------------------------------------------------------------------------------------------
"""
5. Count a character
Use direct indexing to count how many times the character "a" appears in "banana".
"""
# st="BANANA"
# count=0
# for i in st:
#     if i=="A":
#         count+=1
# print(count)

#--------------------------------------------------------------------------------------------
"""
6. Count vowels
Use direct indexing to count how many vowels (a, e, i, o, u) are present in "education". Keep
the solution simple.
"""
# st="education"
# count=0
# for i in range(len(st)):
#     if st[i] in "aeiouAEIOU":
#         count+=1
# print(count)

#--------------------------------------------------------------------------------------------
"""
7. Print characters in reverse order
Use indirect indexing to print "PYTHON" from the last character to the first character. Do not use slicing.
"""
# st="python"
# for i in range(len(st)-1,-1,-1):
#     print(st[i])

#--------------------------------------------------------------------------------------------
"""
8. Print only characters at even indexes
Use indirect indexing to print the characters at indexes 0, 2, 4, ... from "COMPUTER".
"""
# st="computer"
# for i in range(0,len(st),2):
#     print(st[i])

#--------------------------------------------------------------------------------------------
"""
9. Print only characters at odd indexes
Use indirect indexing to print the characters at indexes 1, 3, 5, ... from "COMPUTER".
"""
# st="computer"
# for i in range(1,len(st),2):
#     print(st[i])

#--------------------------------------------------------------------------------------------
"""
10. Find the first vowel
Use indirect indexing to go through "school" from left to right and print the first vowel you find. Stop the
loop after finding it.
"""
# st="school"
# for i in range(len(st)):
#     if st[i] in "aeiouAEIOU":
#         print(st[i])
#         break

#--------------------------------------------------------------------------------------------
"""
11. Check for a character
Use direct indexing to check whether the character "z" exists in "amazing". Print Found or Not
Found.
"""

# st="amazing"
# count=False
# for i in range(len(st)):
#     if st[i]=="z":
#         count+=True
# if count== True:
#     print("found")
# else:
#     print("not found")

#--------------------------------------------------------------------------------------------
"""
12. Convert lowercase letters to uppercase while printing
Use direct indexing to print every character of "python" in uppercase. Do not create another collection.
"""
# st="python"
# for i in range(len(st)):
#     print(st[i].upper())

#--------------------------------------------------------------------------------------------
"""
13. Compare direct and indirect indexing
For "DATA", write two small loops: one using direct indexing and one using indirect indexing. Both
should print the characters in the same order.
"""
# st="data"
# for i in range(len(st)):
#     print(st[i],end=" ")
# print()
# for i in st:
#     print(i,end=" ")

#--------------------------------------------------------------------------------------------
"""
14. Count characters before a space
Use indirect indexing to go through "hello world" and count how many characters appear before the
space. Print the count.
"""
# st="hello world"
# count=0
# for i in range(len(st)):
#     if st[i]==" ":
#         break
#     count+=1
# print(count)

#--------------------------------------------------------------------------------------------
"""
15. Mini challenge - print matching positions
Use indirect indexing with the string "PROGRAM". Print only the characters whose index is equal to their
position when counting from 0. Example: print index and character together.
"""
# st="program"
# for i in range(len(st)):
#     print(i,st[i])

#--------------------------------------------------------------------------------------------


