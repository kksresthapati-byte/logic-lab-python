#WAP for number mirror tool
# Reverse number
# Print original + reverse
# Check palindrome

n=int(input("Enter the number:"))
reverse=0
original=n

#for reversing a number
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(f"Original number: {original}\nReverse number: {reverse}")

#for checking palindrome
if original==reverse:
    print("This number is a palindrome")

else:
    print("This number is not a palindrome")
