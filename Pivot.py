import pandas as pd
data={
    'Region':['North','South','East','West','North','South'],
    'Product':['A','A','B','B','C','C'],
    'Sales':[200,150,300,400,250,350]
}
df=pd.DataFrame(data)

pivot=pd.pivot_table(df,values='Sales',
                     index='Region',columns='Product',
                     aggfunc='sum',fill_value=0)
print("Pivot Table: \n",pivot)