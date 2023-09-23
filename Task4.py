import math
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    if n2 == 0:
        return "Error,cannot divide by zero"
    return n1/n2

def tri_area(base,height):
    return 0.5*base*height

def circle_area(radius):
    return math.pi*radius*radius

def rect_area(width,length):
    return length*width
def main_menu():
    while True:
        print("Welcome! This is the Main Menu")
        print("1.Sum")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Devision")
        print("5.Triangle area")
        print("6.Circle area")
        print("7.Rectangle area")
        print("8.Exit")

        ans = input("Enter your choice: ")
        if ans in('1','2','3','4'):
            num1 = float(input("Enter your first number:"))
            num2 = float(input("Enter your second number:"))

        if ans == '8':
            print("Exiting the program")
            break

        if ans == '1':
            print("the summation is :",add(num1,num2))
        elif ans == '2':
            print("The subtraction is :",sub(num1,num2))
        elif ans == '3':
            print("The multiplication is : ",mul(num1,num2))
        elif ans == '4':
            print("The division :",div(num1,num2))
        elif ans == '5':
            base = float(input("Enter the base of the triangle:"))
            height = float(input("Enter the height of the triangle:"))
            print("The area of a triangle is :",tri_area(base,height))

        elif ans == '6':
            radius = float(input("Enter the radius of your circle:"))
            print("The area of the circle is:",circle_area(radius))
        elif ans == '7':
            length = float(input("Enter the length of your rectangle:"))
            width = float(input("Enter the width of your rectangle:"))
            print("The area of your rectangle:",rect_area(length,width))
        else:
            print("Error Invalid choice.Try again:")

main_menu()