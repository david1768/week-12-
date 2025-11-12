# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output of 3
print(b) #output of 4
print(a==b) #output False

print(a == b)   # False checks for equality
print(a != b)   # True check if it is not equal to another value
print(a > b)    # False checks for greate than another value
print(a < b)    # True checks for less than another value
print(a >= b)   # False checkcs for greater than and equal to
print(a <= b)   # Truecheck for less than or equal to


#predict the output of the following comparisons:
10 > 5 #output true
7 == 2 * 3 + 1 # true
8 != 8 # false
4 <= 2 + 2 # true

# Write 3 examples that result in True and 3 that result in False.

11 > 6 #output true
6 == 2 * 3 # true
6 <= 3 + 3 # true

11 > 1000 #output false
100 == 2 * 3 # false
10000 <= 3 + 3 # false


# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

#asking student score
score = int(input("what is your score?"))
#make this program for all grading spectrums
#if the score is between 90-100 .. you got an A
# if the score is between 80-89 .. you got a B
#if the sore is between 70-79 .. you got a C
#if between 61-69 .. you got a D
#else you failed

if 90 <= score <= 100:
    print("You got an A")
elif 80 <= score <= 89:
    print("You got a B")
elif 70 <= score <= 79:
    print("You got a C")
elif 61 <= score <= 69:
    print("You got a D")
elif 0 <= score <= 60:
    print("You failed.")



# if score >= 60:
#     print("you passed the test")
# else:
#     print("you didn't pass)")

# #ask for a password
# password = input("what is your password? ")