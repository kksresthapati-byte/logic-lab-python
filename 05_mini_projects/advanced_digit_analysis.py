#wap to find the smallest
# find the largest
# count the largest digit
# count the smallest digit
# difference between the largest digit and smallest digit
# difference between the largest digit and smallest digit count
n=675438674118228
original=n
largest=0
smallest=9

while n>0:
    digit=n%10

    if digit>largest:
        largest=digit

    if digit<smallest:
        smallest=digit
    n=n//10
difference_1=largest-smallest

print("Largest digit:", largest)
print("Smallest digit:", smallest)
print("Difference between Largest and Smallest digit:", difference_1)

n=original
count_largest=0
count_smallest=0

while n>0:
    digit=n%10

    if digit==largest:
        count_largest+=1

    if digit==smallest:
        count_smallest+=1

    n=n//10
difference_2=count_largest-count_smallest

print("Count of largest digits:", count_largest)
print("Count of smallest digits:", count_smallest)
print("Difference between Largest and Smallest digit count:", difference_2)