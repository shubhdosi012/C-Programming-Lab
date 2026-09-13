name = input("Enter Student Name: ")

m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))
m4 = int(input("Enter Marks of Subject 4: "))
m5 = int(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n----- RESULT -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")