#WAP to Find largest digit, Find smallest digit, Count digits > 5 for a given number
n=int(input("Enter the number:"))
largest_digit=0
smallest_digit=9
count=0

while n>0:
    digit = n % 10

    if digit>largest_digit:
        largest_digit=digit

    if digit<smallest_digit:
        smallest_digit=digit

    if digit>5:
        count+=1
    n=n//10
print("Largest digit:", largest_digit)
print("smallest digit:", smallest_digit)
print("Digits greater than 5 are:", count)
