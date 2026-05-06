#wap to count the digits greater than 5
n=78653221
greater=0
while n>0:
    digit=n%10
    if digit>5:
        greater+=1
    n=n//10
print(greater)
