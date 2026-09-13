name = input("Enter Name: ")
attendance = input("Enter Attendance: ")

file = open("data/attendance.txt", "a")
file.write(name + " - " + attendance + "\n")
file.close()
print("Attendance Data Saved")