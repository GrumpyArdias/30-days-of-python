import math
# Day 2: 30 Days of python programming

# Exercise 1

first_name = 'Mario'
last_name = 'Herrero'
full_name = first_name + ' ' + last_name
country = 'Spain'
city = 'Madrid'
age = 32
year = 2023
is_married = False
is_true = True
is_light_on = False

type_of_cheese, is_cheese = 'cheddar', True

# Exercise 2

print([first_name, last_name, country, city, age,
      year, is_married, is_true, is_light_on])

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
print(total)
diff = num_two - num_one
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two

area_of_circle = (30**2) * math.pi
print("The area of the circle is ", area_of_circle)
circum_of_circle = 2 * math.pi * 30
print("The circumference of the circle is ", circum_of_circle)


def area(radius):
    return (radius**2) * math.pi


print("The area of the circle is ", area(15))


def personal_data():
    name = input("What is your name?")
    surname = input("What is your surname?")
    age = input("What is your age?")
    country = input("What is your country?")

    return name, surname, age, country


print(personal_data())
