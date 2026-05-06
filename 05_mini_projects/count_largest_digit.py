# WAP to Count how many digits are equal to largest digit
#n=765598989
n=int(input("Enter the number:"))
largest=0
original=n
while n>0:
    digit=n%10

    if digit>largest:
        largest=digit
    n=n//10
print("Largest number:", largest)

n=original
count_largest=0
while n>0:
    digit=n%10

    if digit==largest:
        count_largest+=1
    n=n//10
print("count of largest number:", count_largest)
