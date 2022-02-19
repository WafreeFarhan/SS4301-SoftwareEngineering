print("1. Student detail")
print("2. module timetable")
command=input("Enter a command (either 1 or 2): ")

if command == "1":
    stuDetail=input("Enter student ID")
    if stuDetail == "19b9008":
        print("NAME: Muhammad Wafri farhan")
        print("DOB: 11/03/1999")
    else:
        print("Student not found")

elif command == "2":
    print("1. Faculty of science")
    moduleTimetable=input("Enter faculty: ")
    if moduleTimetable == "1":
        print("Monday   : SS-2206 (07:50 - 11:40)")
        print("Tuesday  : SS-4310 (07:50 - 09:40)")
        print("Thursday : SS-4301 (14:10 - 16:00)")
        print("Saturday : SS-4301 (14:10 - 16:00)")
    else:
        print("module timetable not found")