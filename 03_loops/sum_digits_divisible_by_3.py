#wap to find sum of digits divisible by 3
n=9876543
total=0
while n>0:
    digit=n%10
    if digit%3==0:
        total=total+digit
    n=n//10
print(total)
