#pract 1 q1
"""
pi = 3.14
radius = int(input("Enter the radius:"))
area_of_circle = pi * radius**2
circumference_of_circle = 2*pi * radius
print("The area of Circle is ", area_of_circle)
print("The circumference of circle is ", circumference_of_circle)"""


# q2
"""user_num = int(input("Enter any number:"))

if user_num % 2 == 0 :
        print("The number is even")
else:
    print("The number is odd")
# q3
marks = int(input("Enter marks obtained:"))
if marks >= 90 :
      print("O grade")
elif marks >= 80:
    print("A grade")
elif marks >= 70:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 50:
    print("D grade")
else :
    print("Fail")"""
#q4
"""num_1 = int(input("Enter"))
num_2 = int(input("Enter "))
num_3 = int(input("Enter "))

if num_1 == num_2 or num_2 == num_3 or num_3 == num_1 :
    print("The sum is", 0)
else:
    print("The sum of those three digits is", num_1+num_2+num_3)"""
#q5
"""sums = 0
for i in range(11,31):
    if i % 2 != 0 :
        sums = sums+i
        print("The sum is",sums)"""
#q6
"""num_1 =  int(input("Enter an integer:"))
num_2= int(input("Enter an integer:"))
sums = num_1 + num_2
if 15 < sums < 20 :
    print("20")
else :
    print("the sum is", sums)"""
#q7
"""a = float(input("Enter the number:"))
b = float(input("Enter the 2nd number:"))
sums = a+b
if a==b or a+b==5 or a-b==5:
    print("True")
else :
    print(sums)"""
#q8
"""for x in range(1500,2700):
    if x % 7==0 or x % 5 ==0:
        print(x)"""
#q9
"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print("")"""
#q10
"""name=input("Enter your name")
current_age=int(input("Enter your current age:"))
current_year=int(input("Enter current ye: "))
year_100 = current_year+(100-current_age)
print(name,"you will turn a 100 on the year:",year_100)"""
#q11
num_1 = int(input("enter first number:"))
num_2 = int(input("enter second number:"))
num_3 = int(input("enter third number:"))
num_4 = int(input("enter fourth number:"))
"""if num_2 < num_1 and num_3 < num_1 and num_4 < num_1 :
    print("The maximum number is first num ",num_1)
elif num_1 < num_2 and num_3 < num_2 and num_4 <num_2 :
    print("Max number is second ",num_2)
elif num_1 < num_3 and num_2 < num_3 and num_4 < num_3:
    print("max number is third", num_3)
elif num_1 < num_4 and num_2 < num_4 and num_3 < num_4:
    print("max num is fourth",num_4)
else :
    print("Minimum nuber is..")
 """
# Create the list directly using the variables
numbers_list = [num1, num2, num3, num4]

# Find the minimum and maximum using the built-in functions
minimum_number = min(numbers_list)
maximum_number = max(numbers_list)

# Display the results
print(f"\nThe numbers you entered are: {numbers_list}")
print(f"The minimum number is: {minimum_number}")
print(f"The maximum number is: {maximum_number}")

