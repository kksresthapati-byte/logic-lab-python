#Student report card
total_marks=0
n=int(input("Enter the no of subjects:"))
for i in range(n):
    marks=int(input("Enter the subjects marks{i+1}:"))
    total_marks += marks
percentage = total_marks /(n*100) * 100

print("\n----- Report Card -----")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 90:
    print("Grade A: Excellent")
elif percentage >= 70:
    print("Grade B: Good")
elif percentage >= 50:
    print("Grade C: Average")
else:
    print("Fail: Needs Improvement")


