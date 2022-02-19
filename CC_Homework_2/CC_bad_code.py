#Program that allows the user to computate 2 variables by multitudes of operation
#such as addition, subtraction, multiplication, division. Basically a calculator program
input1=input("Enter a number: ")
input2=input("Enter a number: ")
print("Select an operation")
operation=input("+,-,*,/: ")

#Addition operation
operation1=float(input1)+float(input2)
#Subtraction operation
operation2=float(input1)-float(input2)
#Multiplication operation
operation3=float(input1)*float(input2)
#Division operation
operation4=float(input1)/float(input2)

#Addition operation
if   operation=="+":
    print(operation1)
#Subtraction operation    
elif operation=="-":
    print(operation2)
#Multiplication operation
elif operation=="*":
    print(operation3)
#Division operation
elif operation=="/":
    print(operation4)
#Only happens if user selected operations that are not listed above    
else:
    print("Invalid input") 