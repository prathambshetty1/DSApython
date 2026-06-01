exchange_rates={
    "INR":1.0,
    "USD":0.0105440742302826,#do 1/usdvalue
    "EUR":0.0090260853867678,
    "GBP":0.0078369905956113,
    "JPY":1.666666666666667
}

def convert_currency(amount,from_currency,to_currency):
    amount_in_inr=amount/exchange_rates[from_currency]
    converted_amount=amount_in_inr*exchange_rates[to_currency]
    return converted_amount

amount=float(input("Enter amount"))
from_currency=input("From Currency (USD,EUR,INR,GBP,JPY):").upper()
to_currency=input("To Currency (USD,EUR,INR,GBP,JPY):").upper()

if from_currency not in exchange_rates or to_currency not in exchange_rates:
    print("Invalid Currency!!")
else:
    print("After conversion: ",convert_currency(amount,from_currency,to_currency))