import matplotlib.pyplot as plt
categories=['Rent','Food','Transport','Entertainment']
expenses=[500,300,200,100]
plt.figure(figsize=(6,6))
plt.pie(expenses,labels=categories,autopct='%1.1f%%',startangle=90,colors=['skyblue','lightgreen','orange','pink'])
plt.title("Monthly Expenses Distribution")
plt.show()