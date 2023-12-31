
print('hello')
print('hii')


import pandas as pd
customer=pd.read_csv('Downloads/156c0733-d225-4b76-a984-3ed5e19eb16d_83d04ac6-cb74-4a96-a06a-e0d5442aa126_customers.csv')
customer.head()

order=pd.read_csv('Downloads/419f8355-6271-44cc-a20b-fea8bd241428_83d04ac6-cb74-4a96-a06a-e0d5442aa126_orders.csv')
order.head()

trans=pd.read_csv('Downloads/422ceab9-b775-4f4a-8a04-066006bf204b_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions.csv')
trans.head()

customer.isna().sum()
#looks like theres no missing values

order.isna().sum()
#there are few missing values in orders table.lets fill it with none values

order["ship_mode"].fillna("None",inplace=True)
order["order_approved_at"].fillna(0,inplace=True)
order["order_delivered_carrier_date"].fillna(0,inplace=True)
order["order_delivered_customer_date"].fillna(0,inplace=True)

order.isna().sum()
#now theres no missing values

trans.isna().sum()
#payment type column has missing values


trans['payment_type'].mode()
trans["payment_type"].fillna('credit_card',inplace=True)
#we've replaced the missing values with mode of the column

trans.isna().sum()
#now theres no missing values

#now lets merge the tables
df1=pd.merge(order,trans,on='order_id',how='left')
df1.head()

df2=pd.merge(df1,customer,on="customer_id")
df2.head()

#now lets select the records with sales values more than 150
df3=df2[df2["sales"]>150]
df3

df3['order_id']

df4=df3['customer_name'].unique()

df5=pd.DataFrame(df4)
df5

#now lets work on th second part
df6=df2[df2["sales"]>250]
df6

#we can see that the num. of customers have gone down from 3898 to 2155 as we increased the high trans value to 250

df6['order_id']

df7=df6['customer_name'].unique()

pd.DataFrame(df7)

from datetime import datetime
import numpy as np

df6["month"]=pd.to_datetime(df6["order_purchase_date"])

df6['Month1'] = df6["month"].dt.strftime('%m')
df6['Year1'] = df6["month"].dt.strftime('%Y')
df6

df8=df6.groupby(['Month1','Year1']).agg({'sales':np.sum})
df8.reset_index(inplace=True)

df8