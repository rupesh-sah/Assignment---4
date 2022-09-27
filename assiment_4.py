'''Assignment - 4 Full Stack Web Development using Python MySirG

    User Input Problems'''

#(Q.1) Write a python script to take your name as input from the user and then print it.
names = input("Enter your Name : ")
print(names)

#(Q.2) Write a python script to take input from the user. Input must be a number.
num1 = int(input())
print(num1)

'''(Q.3) Write a python script which takes two numbers from the user, then calculate their sum
and display the result.'''

num2 = int(input("Enter Your First Number : "))
num3 = int(input("Enter Your Second Number : "))
sum_num2_num3 = num2+num3
print(sum_num2_num3)

# (Q.4) Write a python script which takes the radius from the user and display area of a circle.
r = float(input("Enter the radius of the circle: "))
area = 3.1416 * r
print("Radius:", r)
print("Area = ", area)

# (Q.5) Write a python script to calculate the square of a number. Number is entered by the user.
p = int(input("Enter a number "))
k = p*p
  
print("your square number is =", k)

#(Q.6) Write a python script to calculate the area of Triangle. Number is entered by the user.
a = int(input('Enter the first side :'))
b = int(input('Enter the second side :'))
c = int(input('Enter the third side :'))

d = (a+b+c)/2
area = (d*(d-a)*(d-b)*(d-c)) ** 0.5
print('The area of the triangle is :', area)

#(Q.7) Write a python script to calculate average of three numbers, entered by the user

a = int(input('Enter the first number :'))
b = int(input('Enter the second number :'))
c = int(input('Enter the last number :'))

average = (a+b+c)/3
print("The average of three number is :", average)

#(Q.8)Write a python script to calculate simple interest
p = int(input('Enter The num: '))
r = int(input('Enter The second number: '))
t = int(input('Enter The last num :'))

simple_intrest = (p*r*t)/100
print('The simple intrest is :', simple_intrest)

# (Q.9) Write a python script to calculate the volume of a cuboid.
print("Enter length , breadth and height of a cuboid")
l,b,h=float(input('Enter The first number :')),float(input('Enter The second number: ')),float(input('Enter The last num :'))
v=l*b*h
print('Volume is',v)

# (Q.10) Write a python script to calculate area of a rectangle
l = float(input('Enter the length of a Rectangle: '))
b = float(input('Enter the breadth of a Rectangle : '))
Area = l * b
print("Area of a rectangle  is : %.2f" %Area)



