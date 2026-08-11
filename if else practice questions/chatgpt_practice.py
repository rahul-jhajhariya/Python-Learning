#🟢 Level 1 — Basic
# 1. User se ek number lo. Check karo number positive hai ya negative. Agar positive hai, to check karo even hai ya odd.

# n=5
# if n>0:
#     if n%2==0:
#         print("n is positive and even")
#     else:
#         print("n is positive and odd")
# else:
#     print("n is negative")
#---------------------------------------------------------------------------------------------------------------------
'''
2. User ki age lo. Agar age 18 ya usse zyada hai, to check karo Indian citizen hai ya nahi. 
   Dono conditions ke basis par voting eligibility batao.'''

# age=56
# citizen="indian"
# if age>=18:
#     if citizen=="indian":
#         print("He/She is eligible for voting")
#     else:
#         print("not eligible for voting ")
# else:
#         print("not eligible for voting ")
#---------------------------------------------------------------------------------------------------------------------
"""
3. User se marks lo. Agar marks 40 ya usse zyada hain, to check karo:
   marks 75+ → Distinction
   otherwise → Pass
"""
# marks=52
# if marks>40:
#     if marks>75:
#         print("distinction")
#     else:
#         print("pass")
#---------------------------------------------------------------------------------------------------------------------
# 4. User se ek number lo. Agar number 10 se bada hai, to check karo ki woh 20 se bhi bada hai ya nahi.
# num=25
# if num>10:
#     if num>20:
#         print("number is greater than 20")
#     else:
#         print("number is not greater than 20")
#---------------------------------------------------------------------------------------------------------------------
# 5. User se password lo. Agar password correct hai, to check karo username bhi correct hai ya nahi.

# password=input("Enter your password:")
# username="rahul@123"
# if password=="123456":
#     if username=="rahul@123":
#         print("you have entered correct password and username")
#     else:
#         print("you have entered wrong username")
# else:
#     print("entered correct password")  

#---------------------------------------------------------------------------------------------------------------------
#🟡 Level 2 — Intermediate
'''Teen numbers input lo. Pehle check karo a > b, phir nested if se determine karo ki a > c hai ya nahi. 
Finally largest number print karo.'''

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if a>b:
#     if a>c:
#         print("a is the largest")
#     else:
#         print("c is the largest")
# else:
#     if b>c:
#         print("b is the largest")
#     else:
#         print("c is the largest")
#---------------------------------------------------------------------------------------------------------------------
"""
Student ke marks lo. Agar student pass hai (>=40), to nested if-else se grade determine karo:

90+ → A+
75–89 → A
60–74 → B
40–59 → C
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
        
#---------------------------------------------------------------------------------------------------------------------
"""
User ki age aur income lo. Agar age 18+ hai, to check karo income ₹25,000 se zyada hai ya nahi. 
Loan eligibility decide karo.
"""
# age=int(input("Enter your age:"))
# income=int(input("enter your income:"))
# if age>18:
#     if income>25000:
#         print("you are eligible for loan")
#     else:
#         print("you are not eligible for loan")
# else:
#     print("you are not eligible for loan")
#---------------------------------------------------------------------------------------------------------------------
"""
Shopping amount lo. Agar amount ₹1000+ hai, to check karo:

₹5000+ → 20% discount
otherwise → 10% discount
below ₹1000 → No discount
"""
# amount=int(input("Enter the amount:"))
# if amount>1000:
#     if amount>5000:
#         print("20% discount")
#     else:
#         print("10% discount")
# else:
#     print("no discount")

#---------------------------------------------------------------------------------------------------------------------
"""
Ek number lo. Check karo:
Positive hai → nested if se check even/odd
Negative hai → nested if se check even/odd
Zero → Zero print karo
"""
# num=65
# if num>0:
#     if num%2==0:
#         print("positive and even")
#     else:
#         print("positive and odd")
# else:
#     if num%2==0:
#             print("negative and even")
#     else:
#         print("negative and odd")

#---------------------------------------------------------------------------------------------------------------------
#🔴 Level 3 — Advanced
"""
ATM simulation banao:
PIN correct hai → balance check karo
Balance sufficient hai → withdrawal allow karo
Otherwise → insufficient balance
PIN incorrect → access denied
"""
# pinn=123456
# bal=15000
# pin=int(input("Enter your pin:"))
# if pinn==pin:
#     withdrawl=int(input("Enter the withdrawl amount:"))
#     if bal>=withdrawl:
#         bal=bal-withdrawl
#         print("withdrawl succesful")
#         print("remaining bal is:",bal)
#     else:
#         print("insufficent balance")
# else:
#     print("access denied")
#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------