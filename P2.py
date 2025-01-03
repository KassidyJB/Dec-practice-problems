import math

#Problem 2: Area Calculator
#DES:Create a program that says: "I can calculate the area of a shape for you.
#  Which shape do you want me to calculate the area of?" 
# and then asks the user to type in the name of a shape (e.g., triangle, rectangle, square, circle).

######Welcoming messages below########
name = input(f"What is your name?\n>")

print(f"\nHi {name}! I can calculate the area of a shape for you.\n")

######Displaying a menu for the shapes the user can pick (limited shapes)########
def display_shape():
    print("1.Triangle")
    print("2.Square")
    print("3.Trapezoid")
    print("4.Circle")
    print("5.Rectangle")
display_shape()



######Evaluating user input, setting the stage for customized responses based on choice number######
def user_select():
    user_ask = (int(input(f"{name}, which shape do you want me to calculate the area of? (Enter number)\n")))
    if user_ask == 1:
        choice_1()
    elif user_ask == 2:
        choice_2()
    elif user_ask == 3:
        choice_3()
    elif user_ask == 4:
        choice_4()
    elif user_ask == 5:
        choice_5()
user_select()

####Triangle function###
def choice_1(): #Triangle area = (bh)/2 (ask for base and height)
    tri_b = float(input(f"\n Enter a base: \n>"))
    tri_h =  float(input(f"\nEnter a height: \n>"))
    t_area = (tri_b*tri_h) / 2
    print(t_area)
choice_1()

####Square function####

def choice_2(): #Square area = side length^2 (ask for side length)
    sq =  float(input(f"\nEnter a side length\n>"))
    s_area = {sq}*{sq} #Attempt to square the input for this formula
    print(s_area)
choice_2()

####Trapezoid Function#####

def choice_3(): #Trapezoid area = (a+b/2)h (ask for bases and height)
    t_a = float(input(f"\nEnter a number for base 1: \n"))#Base 1 input
    t_b = float(input(f"\nEnter a number for base 2: \n"))#Base 2 input
    tr_h = float(input(f"\nEnter height: \n"))#Height input
    tr_area = (t_a + t_b)*tr_h#attempting to use formula for trapezoid. Trapezoid is a shape I added to this list for fun
    print(tr_area)
choice_3()


####Circle Function#####

def choice_4(): #Circle area = pi*r^2 (ask for radius)
    pi = 3.14 #assigning estimated pi value
    radii = float(input(f"\nEnter a radius\n>"))#asking for user input for radius
    #c_area = ({radii}**2)*pi#Attempt to calculate circle area but squaring operation is difficult
    c_area = ({radii}*{radii})*pi#2nd attempt, trying to multiply radii by itself to square
    print(c_area)
choice_4()


####Rectangle function###

def choice_5():#Rectangle Area = L*W
    l = float(input(f"\nEnter length: \n>"))
    w = float(input(f"\nEnter width: \n>"))
    r_area = {l} * {w} #multiplying user input together using the formula
    print(r_area) #printing the product
choice_5()

##I've done code like this befroe but somehow each time I try a number, my choices aren't defined, though 
#they're defined right there