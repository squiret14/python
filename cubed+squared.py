
km = input("please enter the number of km")
km = int(km)
miles = km/1.609
print(miles)


import math

def cm_to_inches(cmValue):
    inches = cmValue/2.54
    return (inches)

def a_o_t (height , width):
    area = width*height/2
    return (area)

result = a_o_t(6,5)
print(result)
print("{0:.2f}".format(result))

def c_o_c(radius):
    circumference = radius*2*math.pi
    area = radius*radius*math.pi
    x = [0,0]
    x[0] = area
    x[1] = circumference
    return x

result = c_o_c(int(input("please enter a r")))
print ("radius = ",result[0])
print ("circum = ",result[1]) 


def addNumbers(n,m):
    total = 0
    for i in range(n,m+1):
        total = total + i
    return (total)
print(addNumbers(int(input("enter the first num:")),(int(input("input second nuber : ")))))


def grade(grade):
    mark = ""
    if grade >= 80:
        mark = "distinction"
        return mark
    elif grade >= 65:
        mark ="merit"
        return mark
    elif grade >=50:
        mark ="pass"
        return mark
    else:
        mark ="fail"
        return mark
grade = grade(int(input("please enter you grade as a %")))
name = input("please enter your name")
print("your name is ",name,"and your grade is ",grade)
        




