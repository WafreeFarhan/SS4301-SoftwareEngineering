from operator import truediv


def main():
    print("1. Student detail")
    print("2. module timetable")
    command = input("Enter a command: ")
    myGIS = myGIS_Directory(command)

class myGIS_Directory:

    def __init__(self, command, studentDetail, moduleTimetable):
        self.command = command
        self.studentDetail = studentDetail
        self.moduleTimetable = moduleTimetable
        pass

    def get_command(self, command, studentDetail, moduleTimetable):
        if command == "1":
            studentDetail = input("Enter student ID")
        elif command == "2":        
            print("1. Faculty of science")
            moduleTimetable = input("Enter faculty: ")
        else:
            print("command not found")

    def get_studentDetail(self, studentDetail):
        if studentDetail == "19b9008":
            print("NAME: Muhammad Wafri farhan")
            print("DOB: 11/03/1999")
        else:
            print("Student not found")

    def get_moduleTimetable(self, moduleTimetable):
        if moduleTimetable == "1":
            print("Monday   : SS-2206 (07:50 - 11:40)")
            print("Tuesday  : SS-4310 (07:50 - 09:40)")
            print("Thursday : SS-4301 (14:10 - 16:00)")
            print("Saturday : SS-4301 (14:10 - 16:00)")
        else:
            print("module timetable not found")

if __name__ == "__main__":
    main()