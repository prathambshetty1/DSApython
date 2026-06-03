import matplotlib.pyplot as plt
import numpy as np
categories=["Rent","Food","Transport","Entertainment"]
expenses=[500,300,200,100]
plt.figure(figsize=(6,6))
plt.pie(expenses,labels=categories,autopct='%1.1f%%',startangle=90,colors=['skyblue','lightgreen','orange','pink'])

centre_circle=plt.Circle((0,0),0.70,fc='white')
fig=plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Monthly Expenses Distribution (Donut Chart)")
plt.show()