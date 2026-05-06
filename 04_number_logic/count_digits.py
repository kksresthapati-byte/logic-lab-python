#count the digits in a number
count=0
n=123456
while n>0:
    n=n//10
    count+=1
print(count)
