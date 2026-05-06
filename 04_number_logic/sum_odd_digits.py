#sum of odd digits
n=1267543390
total=0
while n>0:
    digit = n % 10
    if digit % 2!= 0:
        total=total+digit
    n = n // 10
print(total)

