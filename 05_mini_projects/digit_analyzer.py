#Digital Analyzer
#wap to count the digits,even digits, odd digits and sum of digits
n=int(input("Enter the number:"))
total_digit=0
even_digit=0
odd_digit=0
sum_digit=0

while n>0:
    digit=n%10

    total_digit+=1
    sum_digit+=total_digit

    if digit % 2 == 0:
        even_digit+=1

    else:
        odd_digit+=1

    n=n//10
print(f'Total digits: {total_digit}')
print(f'Even digits: {even_digit}')
print(f'Odd digits: {odd_digit}')
print(f'Sum digits: {sum_digit}')
