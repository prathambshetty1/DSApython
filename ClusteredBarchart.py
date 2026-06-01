import matplotlib.pyplot as plt
import numpy as np
categories=['Jan','Feb','Mar','Apr','May']
product_a=[20,35,30,35,27]
product_b=[25,32,34,20,25]
product_c=[15,20,18,25,22]
y=np.arange(len(categories))
bar_width=0.25
plt.barh(y-bar_width,product_a,height=bar_width,label='Product A')
plt.barh(y,product_b,height=bar_width,label='Product B')
plt.barh(y+bar_width,product_c,height=bar_width,label='Product C')
plt.yticks(y,categories)
plt.title('Clustered Bar Chart')
plt.xlabel('Sales')
plt.ylabel('Months')
plt.legend()
plt.show()