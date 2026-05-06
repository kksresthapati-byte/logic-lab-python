#Sum vs Count Analyzer
#Sum of even digits
#Count of odd digits
#Difference

n=231987
sum_even=0
count_odd=0

while n>0:
    digit=n%10

    if digit%2==0:
        sum_even+=digit

    else:
        count_odd+=1

    n=n//10

difference=sum_even-count_odd


print("Sum of even digits is:", sum_even)
print("Count of odd digits is:",count_odd)
print("Difference between the digits:", difference)
