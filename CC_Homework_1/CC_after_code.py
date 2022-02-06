#CALCULATOR PROGRAM
num1=input("Enter a number: ")
num2=input("Enter a number: ")


print("Select an operation")
operation=input("+,-,*,/: ")


add      = float(num1) + float(num2)
minus    = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide   = float(num1) / float(num2)


if   operation=="+":
    print(add)
elif operation=="-":
    print(minus)
elif operation=="*":
    print(multiply)
elif operation=="/":
    print(divide)
else:
    print("Invalid input")
