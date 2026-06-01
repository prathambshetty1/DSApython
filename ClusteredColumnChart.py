import matplotlib.pyplot as plt
import numpy as np
months=['Jan','Feb','Mar','Apr','May']
product_a=[20,35,30,35,27]
product_b=[25,32,34,20,25]
product_c=[15,20,18,25,22]
x=np.arange(len(months))
bar_width=0.25
plt.bar(x-bar_width,product_a,width=bar_width,label='Product A')
plt.bar(x,product_b,width=bar_width,label='Product B')
plt.bar(x+bar_width,product_c,width=bar_width,label='Product C')
plt.xticks(x,months)
plt.title('Clustered Column Chart')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()