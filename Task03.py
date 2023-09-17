num1 = int(input("Enter two numbers:"))
num2 = int(input("Enter two numbers:"))

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

#I added the type just because I wannna make sure I understood and applied all the information in the session

print(add(num1,num2),type(add(num1,num2)))
print(div(num1,num2),type(div(num1,num2)))
print(mul(num1,num2),type(mul(num1,num2)))
print(sub(num1,num2),type(sub(num1,num2)))
