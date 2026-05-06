# For a number:
# Find largest digit
# Find smallest digit
# Find difference between them

n=25439871
largest=0
smallest=9

while n>0:
    digit=n%10

    if digit>largest:
        largest=digit

    if digit<smallest:
        smallest=digit

    n=n//10

difference=largest-smallest

print("Largest:", largest)
print("Smallest:", smallest)
print("Difference:", difference)
