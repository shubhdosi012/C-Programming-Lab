name = input("Enter Name: ")
marks = input("Enter Marks: ")

file = open("student.txt", "a")

file.write(name + " - " + marks + "\n")

file.close()

print("Student Data Saved")