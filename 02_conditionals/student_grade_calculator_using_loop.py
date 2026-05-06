#student grade calculator using if else statement
marks1=int(input("enter your marks in maths:"))
marks2=int(input("enter your marks in physics:"))
marks3=int(input("enter your marks in English:"))
name=input("enter your name:")
total_marks=marks1+marks2+marks3
percentage=total_marks/300*100
if percentage>=90:
    print("Grade A")
elif percentage>=75:
    print("Grade B")
else:
    print("Garde C")
print(percentage)
print(f"Hello {name},I hope you are doing well!\nYour total score in 3 subjects is:{total_marks}\nYou have cleared your exam with {percentage} percentage."

