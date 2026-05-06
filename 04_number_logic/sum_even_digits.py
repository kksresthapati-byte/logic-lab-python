
#sum of even digits
n=45789212
total=0
while n>0:
    digit = n % 10
    if digit % 2 == 0:
        total=total+digit
    n=n//10
print(total)
