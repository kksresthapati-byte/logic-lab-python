#student attendance system
n=int(input("enter the number of attendance inputs: "))
for i in range(n):
    attendance=int(input("Enter your attendance report{i+1}:"))
    report=attendance/30 * 100
print(f"Total present days:{attendance}")
print(f"Attendance:{report}%")
