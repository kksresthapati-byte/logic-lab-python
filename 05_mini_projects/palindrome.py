#WAP to check for palindrome
#n=234234
n=int(input("Enter the number:"))
reverse=0
original=n

#to reverse a number
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print("reverse:", reverse)

#to check for palindrome
if original==reverse:
    print("This number is a Palindrome")
else:
    print("This number is not a palindrome")

