input1=input("Enter a number: ")
input2=input("Enter a number: ")
print("Select an operation")
operation=input("+,-,*,/: ")
operation1=float(input1)+float(input2)
operation2=float(input1)-float(input2)
operation3=float(input1)*float(input2)
operation4=float(input1)/float(input2)
if   operation=="+":
    print(operation1)
elif operation=="-":
    print(operation2)
elif operation=="*":
    print(operation3)
elif operation=="/":
    print(operation4)
else:
    print("Invalid input") 
