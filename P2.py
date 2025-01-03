import random

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
    choice = input(f"{name}, which shape do you want me to calculate the area of?\n")
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
def choice_1(): #Circle area = 2*pi*r^2 (ask for radius)
    
    pass 

####Square function####

def choice_2(): #Square area = side length^2 (ask for side length)

    pass 

####Trapezoid Function#####

def choice_3(): #Trapezoid area = (a+b/2)h (ask for bases and height)

    pass 


####Circle Function#####

def choice_4(): 

    pass


####Rectangle function###

def choice_5():

    pass
