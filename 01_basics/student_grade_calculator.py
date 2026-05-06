#student grade calculator
Name=input("Enter your name:")
marks1=int(input("Enter your marks in maths:"))
marks2=int(input("Enter your marks in physics:"))
marks3=int(input("Enter your marks in English:"))
total_marks=marks1+marks2+marks3
percentage=total_marks/300*100
Grade_A=percentage>90
Grade_B=percentage>75
Grade_C=percentage<75
print(total_marks)
print(percentage)
print(Grade_A)
print(Grade_B)
print(Grade_C)
