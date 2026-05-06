#discount calculator
amount=int(input("Enter the amount:"))
discount=0

if amount>10000:
    discount=amount*50/100
    print("Congrats! you will get a discount of 50%")

elif amount>5000 and amount<=10000:
    discount=amount*25/100
    print("Congrats! You will get a discount of 25%")

elif amount>2500 and amount<5000:
    discount=amount*10/100
    print("You will get a discount of 10%")

else:
    print("No discount")

final_price=amount-discount

print("Disount price:", discount)
print("The final amount after discount:", final_price)
