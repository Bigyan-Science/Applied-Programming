from datetime import date


def printHeader():
    print(f"""
        Sunway Int'l Electricity Authority
            Maitidevi, Kathmandu
                            Date:{date.today()}
     *-------*-------*-------*-------*-------*
    """)


printHeader()
cusName = input("Enter the owner name:")
cusAddress = input("Enter the owner address:")
unit = int(input("Enter the total units consumed:"))
amount = 0
dis = 0

if unit < 100:
    amount = 0
elif 100 < unit <= 200:
    amount = (unit - 100) * 5
elif 200 < unit <= 500:
    amount = (unit - 200) * 10

else:
    amountDis=(unit-500)*10
    amount = (unit - 200) * 10 + 100 * 5
    dis = amountDis\
          /10

print(f""" 

""")
printHeader()
print(f"""Customer Name: {cusName}
Customer Address: {cusAddress}
Consumed unit: {unit}
Total amount to be paid:Rs.{amount}
Total discount price:Rs.{dis}
Total amount after discount:Rs.{amount-dis}

{cusName} Customer of Sunway Int'l Electricity Billing System 
has to pay total amount Rs.{amount-dis} and got discount of Rs.{dis}""")

