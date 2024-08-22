import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# For Linear Regression
data=pd.read_csv('homeprices.csv')
#print(data)
plt.xlabel('Area in sq ft')
plt.ylabel('Prices in $')
plt.scatter(data.area,data.price)

regression_model=linear_model.LinearRegression()
regression_model.fit(data[['area']],data.price)
regression_model.coef_
regression_model.intercept_
regression_model.predict(data[['area']])
#print(regression_model.predict([[3300]]))

print(plt.plot(data.area, regression_model.predict(data[['area']])))

# For Multi-Linear Regression
df=pd.read_csv("homeprice2.csv")
print(df)
df.bedrooms=df.bedrooms.fillna(df.bedrooms.median())
print(df)
reg_model=linear_model.LinearRegression()
reg_model.fit(df[['area','bedrooms','age']],df.price) #independnt variables in double bracket
print(reg_model.predict([[3000,3,40]]))
