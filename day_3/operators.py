import math
age = 32
height = 1.98
complex_number = 3 + 4j


# def triangle_area():
#     base = input("Set the base of the triangle:")
#     height = input("Set the height of the triangle:")
#     area = 0.5 * float(base) * float(height)
#     return area


# print("The area of the triangle is: ", triangle_area())


# def triangle_perimeter():
#     side_a = input("Set the a side of the triangle:")
#     side_b = input("Set the b side of the triangle:")
#     side_c = input("Set the c side of the triangle:")
#     perimeter = float(side_a) + float(side_b) + float(side_c)

#     return perimeter


# print("The perimeter of the triangle is: ", triangle_perimeter())

# def rectangle_area():
#     reactangle_length = input("Set the length of the rectangle:")
#     rectangle_width = input("Set the width of the rectangle:")
#     area = float(reactangle_length) * float(rectangle_width)
#     perimeter = 2 * area
#     return area, perimeter


# print("the area of the rectangle and his perimeter is: ", rectangle_area())

# def circle_radius():
#     radius_of_the_circle = input("Set the radius of the circle:")
#     area = math.pi * float(radius_of_the_circle) ** 2
#     circunference = 2 * math.pi * float(radius_of_the_circle)
#     return area, circunference


# print("The area of the circle and his circumference is: ", circle_radius())

# def linear_slope():
#     x1 = input("Set the x1:")
#     y1 = input("Set the y1:")
#     x2 = input("Set the x2:")
#     y2 = input("Set the y2:")
#     slope = (float(y2) - float(y1)) / (float(x2) - float(x1))

#     y_intercept = float(y1) - slope * float(x1)
#     x_intercept = float(x1) - slope * float(y1)

#     return slope, y_intercept, x_intercept


# print("The slope, y-intercept and x-intercept of the line is: ", linear_slope())


# def euclidian_distance():
#     x1 = input("Set the x1:")
#     y1 = input("Set the y1:")
#     x2 = input("Set the x2:")
#     y2 = input("Set the y2:")
#     distance = math.sqrt((float(x2) - float(x1)) ** 2 +
#                          (float(y2) - float(y1)) ** 2)
#     slope = (float(x1) - float(x2)) / (float(y2) - float(y1))

#     return distance, slope


# print("The distance between the two points and the slope of the line is: ",
#       euclidian_distance())

# def second_degree_ecuation():
#     a = input("Set the a:")
#     b = input("Set the b:")
#     c = input("Set the c:")

#     positive_y = (-float(b) + math.sqrt(float(b) ** 2 -
#                   4 * float(a) * float(c))) / (2 * float(a))
#     negative_y = (-float(b) - math.sqrt(float(b) ** 2 -
#                   4 * float(a) * float(c))) / (2 * float(a))

#     return positive_y, negative_y


# print("the values for positive and negative y are: ", second_degree_ecuation())


# print(len('python'))
# print(len('dragon'))

# if len('python') > len('dragon'):
#     print('python')
# elif len('dragon') > len('python'):
#     print('dragon')
# else:
#     print('same')

# if 'on' in 'python' and 'on' in 'dragon':

#     print('yes there is')

# if "jargon" in "I hope this course is not full of jargon":
#     print('yes there is')


# if "on" in "python" and "on" in "dragon":
#     print('yes there is')
# else:
#     print('no there is not')

# length = len('python')
# to_float = float(length)
# to_string = str(to_float)
# print(to_string)

# def is_even(number):
#     if (number % 2 == 0):
#         return True
#     else:
#         return False


# print(is_even(2))
# print(is_even(3))

# floor_division = (7//3)

# if floor_division == 2.7:
#     print('yes')
# else:
#     print('no')

# if type('10') == type(10):
#     print('yes')
# else:
#     print('no')

# if float('9.8') == 10:
#     print('yes')
# else:
#     print('no')


# def semanal_salary():
#     hours = input("How many hours do you work per week?")
#     rate = input("What is your hourly rate?")
#     salary = float(hours) * float(rate)
#     return salary


# print("your semanal salary is: ", semanal_salary(), "€")

# def years_to_seconds():
#     years = input("How old are you?")
#     days = int(years) * 365
#     hours = days * 24
#     seconds = hours * 3600
#     return seconds


# print("your age in seconds is:", years_to_seconds())


def table(number):
    newArr = []
    newArr.append(number)
    newItem = 1
    newArr.append(newItem)
    newItem = number * number
    newArr.append(newItem)
    newItem = number * newArr[len(newArr)-1]
    newArr.append(newItem)
    return newArr


print(table(4))
