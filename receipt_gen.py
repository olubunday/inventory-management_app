import pandas as pd

sales = salesFunc2()

salesList = list(sales.values())
df = pd.DataFrame(salesList, columns = ['Item','Quantity','Selling Price', 'Total Sale'])
print(df)
total = sum(df['Total Sale'])
dfArr = df.values.tolist()
dfArr.append(['Total','Total','Total','Total'])

df = pd.DataFrame(dfArr,columns = ['Item','Quantity','Selling Price', 'Total Sale'] )
df