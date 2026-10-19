#syntax

discount= 10
amount= 1200
if amount > 1000:
    discount = amount*10/100

print(f'amount=:',amount-discount)

#syntax-w/o amount

discount= 0
amount= 1200
if amount > 1200:
    amount = amount*10/100

print(f'amount=:',amount-amount)

#syntax-code improvement-w/o shorthand

amount= 1200
if amount > 1000: amount=amount*10/100

print(f'amount=: ',amount)

#if-else-statement

age=21
print(f'age:',age)
if age >= 18:
    print(str(f'eligible to vote'))
else:
    print(str(f'not eligibile to vote'))

#elif-statement
    
amount = int(input('Enter amount: '))
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
        discount = amount * 10 / 100
elif amount > 1000:
        discount = amount * 5 / 100
else:
     discount = 0
print('amount: ',amount - discount)

amount=int(input('Enter amount:'))
if amount>10000:
    discount=amount*20/10000
elif amount>5000:
        discount=amount*10/5000
elif amount>1000:
        discount=amount*5/1000
else:
     discount='0'
print(int(input(f'amount=:',discount-amount)))





            
        
    
