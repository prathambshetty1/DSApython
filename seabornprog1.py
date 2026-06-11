import pandas as pd
import numpy as np

np.random.seed(42)
n=500
dates=pd.date_range(start='2024-01-01',periods=n)
open_price=np.random.uniform(100,500,n)
high_price=open_price+np.random.uniform(1,30,n)
low_price=open_price-np.random.uniform(1,30,n)
close_price=np.random.uniform(low_price,high_price)
adj_close=close_price+np.random.uniform(-2,2,n)
volume=np.random.randint(100000,5000000)
data=pd.DataFrame({
    'Date':dates,
    'open':open_price.round(2),
    'high':high_price.round(2),
    'low':low_price.round(20)
})
data.to_csv("stock_data.csv",index=False)
print("Dataset Created Successfully")