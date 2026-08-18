"""
Q1. Given the string "PythonProgramming", print only the first 6 characters using string slicing.
"""
# st="PythonProgramming"
# print(st[0:7])

#---------------------------------------------------------------------------------------------------
"""
Q2. Given the string "DataScience", print the last 5 characters using negative indexing and slicing.
"""
# st="DataScience"
# print(st[-5:])

#---------------------------------------------------------------------------------------------------
"""
Q3. Given the string "Programming", print the characters from index 3 to index 7 using slicing.
"""
# st="Programming"
# print(st[3:8])

#---------------------------------------------------------------------------------------------------
"""
Q4. Given the string "ABCDEFGHIJK", print every second character using slicing.
"""
# st="ABCDEFGHIJK"
# print(st[::2])

#---------------------------------------------------------------------------------------------------
"""
Q5. Given the string "PythonIsEasy", print the string in reverse order using slicing.
"""
# st="PythonIsEasy"
# print(st[::-1])

#---------------------------------------------------------------------------------------------------
"""
Q6. Given the string "Hello Python World", extract only the word "Python" using slicing.
"""
# st="Hello Python World"
# print(st[6:12])

#---------------------------------------------------------------------------------------------------
"""
Q7. Given the string "computer", convert the complete string into uppercase using upper().
"""
# st="computer"
# print(st.upper())

#---------------------------------------------------------------------------------------------------
"""
Q8. Given the string "PYTHON PROGRAMMING", convert the complete string into lowercase using lower().
"""
# st="PYTHON PROGRAMMING"
# print(st.lower())

#---------------------------------------------------------------------------------------------------
"""
Q9. Given the string "python", use isupper() to check whether the string contains only uppercase
letters. Display the result.
"""
# st="python"
# print(st.isupper())

#---------------------------------------------------------------------------------------------------
"""
Q10. Given the string "PYTHON", use islower() to check whether the string contains only lowercase
letters. Display the result.
"""
# st="PYTHON"
# print(st.islower())

#---------------------------------------------------------------------------------------------------
"""
Q11. Given the string "PyThOn", use slicing to extract "PyTh" and then convert the extracted part to
uppercase.
"""
# st="PyThOn"
# st=st[:4]
# print(st.upper())

#---------------------------------------------------------------------------------------------------
"""
Q12. Given the string "WELCOME TO PYTHON", use slicing to extract "PYTHON", convert it to
lowercase, and display the result.
"""
# st="WELCOME TO PYTHON"
# st=st[11:17]
# print(st.lower())

#---------------------------------------------------------------------------------------------------
"""
Q13. Given the string "PythonProgramming", extract the first 6 characters and check whether the
extracted string is lowercase using islower(). Then convert it to uppercase.
"""
# st="PythonProgramming"
# st=st[:6]
# print(st.islower())
# print(st.upper())

#---------------------------------------------------------------------------------------------------
"""
Q14. Given the string "PYTHONprogramming", use slicing to extract the first 6 characters and the
last 11 characters separately. Check each extracted part using isupper() and islower().
"""
# st="PYTHONprogramming"
# upper=st[:6]
# lower=st[7:17]
# print(upper.isupper())
# print(lower.islower())

#---------------------------------------------------------------------------------------------------
"""
Q15. Given the string "Learn Python Every Day", use slicing to extract the word "Python". Convert
the extracted word to uppercase and then use isupper() to verify the result. Print the original
extracted word, converted word, and verification result.
"""
st="Learn Python Every Day"
st=st[6:12]
st=st.upper()
print(st.isupper())
