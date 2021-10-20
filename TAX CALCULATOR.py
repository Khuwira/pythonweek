
cost = int(input("enter cost: "))
if cost >100000:
    Tax = 15/100*cost
    print("your tax is", Tax)
elif cost >50000 and cost <=100000:
    Tax = 10/100*cost
    print("your tax is", Tax)
elif cost <=50000:
    Tax = 5/100*cost
    print("your tax is", Tax)
else:
    print('no Tax')


