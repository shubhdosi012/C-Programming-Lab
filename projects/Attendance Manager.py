name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

total_classes = int(input("Enter Total Classes: "))
attended_classes = int(input("Enter Attended Classes: "))

percentage = (attended_classes / total_classes) * 100

print("\n----- ATTENDANCE REPORT -----")
print("Name:", name)
print("Roll Number:", roll)
print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Status: Eligible")
else:
    print("Status: Short Attendance")