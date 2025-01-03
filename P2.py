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
    choice = input(f"{name}, which shape do you want me to calculate the area of? (Enter number)\n")
    if choice == 1:
        choice_1()
    elif choice == 2:
        choice_2()
    elif choice == 3:
        choice_3()
    elif choice == 4:
        choice_4()
    elif choice == 5:
        choice_5()
user_select()

####Triangle function###
def choice_1(): #Triangle area = (bh)/2 (ask for base and height)
    tri_b = float(input(f"\n Enter a base: \n>"))
    tri_h =  float(input(f"\nEnter a height: \n>"))
    t_area = (tri_b*tri_h) / 2

choice_1()

####Square function####

def choice_2(): #Square area = side length^2 (ask for side length)
    sq =  float(input(f"\nEnter a side length\n>"))
    s_area = sq*sq
choice_2()

####Trapezoid Function#####

def choice_3(): #Trapezoid area = (a+b/2)h (ask for bases and height)
    t_a = float(input(f"\nEnter a number for base 1\n>"))
    t_b = float(input(f"\nEnter a number for base 2\n>"))
    
    pass 


####Circle Function#####

def choice_4(): #Circle area = pi*r^2 (ask for radius)
    pi = 3.14 #assigning estimated pi value
    radii = float(input(f"\nEnter a radius\n>"))#asking for user input for radius
    #c_area = ({radii}**2)*pi#Attempt to calculate circle area but squaring operation is difficult
    c_area = ({radii}*{radii})*pi#2nd attempt, trying to multiply radii by itself to square
choice_4()


####Rectangle function###

def choice_5():

    pass
