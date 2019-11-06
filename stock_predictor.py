
# This program predicts the price of GOOGLE and FACEBOOK stock for a specific day
# using the Machine Learning algorithm called 
# Support Vector Regression (SVR) & Linear Regression.

#Import the libraries
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# reading data
df = pd.read_csv('google_30_days.csv')
print(df.head(30),"\n\n\n")
input()

#Create the lists / X and Y data sets
dates = []
prices = []

#Get the last row of data (this will be the data that we test on)
print(df.tail(1),"\n\n\n")
input()


#Get all of the data except for the last row
df = df.head(len(df)-1)
print(df,"\n\n\n")
input()

#Get all of the rows from the Date Column
df_dates = df.loc[:, 'Date']
#Get all of the rows from the Open Column
df_open = df.loc[:, 'Open']

print(df_dates, "\n\n\n")
input()
print(df_open, "\n\n\n")
input()

#Create the independent data set X
for date in df_dates:
  dates.append( [int(date.split('-')[2])])
  
#Create the dependent data set Y
for open_price in df_open:
  prices.append(float(open_price))
  
 
#See what days were recorded
print(dates,"\n\n\n")
input()

#See what days were recorded
print(prices,"\n\n\n")
input()
def predict_prices(dates, prices, x):
  
  #Create the 3 Support Vector Regression models
  svr_lin = SVR(kernel='linear', C= 1e3)
  svr_poly= SVR(kernel='poly', C=1e3, degree=2)
  svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
  
  #Train the SVR models 
  svr_lin.fit(dates,prices)
  svr_poly.fit(dates,prices)
  svr_rbf.fit(dates,prices)
  
  #Create the Linear Regression model
  lin_reg = LinearRegression()
  #Train the Linear Regression model
  lin_reg.fit(dates,prices)
  
  #Plot the models on a graph to see which has the best fit
  plt.scatter(dates, prices, color='black', label='Data')
  plt.plot(dates, svr_rbf.predict(dates), color='red', label='SVR RBF')
  plt.plot(dates, svr_poly.predict(dates), color='blue', label='SVR Poly')
  plt.plot(dates, svr_lin.predict(dates), color='green', label='SVR Linear')
  plt.plot(dates, lin_reg.predict(dates), color='orange', label='Linear Reg')
  plt.xlabel('Days')
  plt.ylabel('Price')
  plt.title('Regression')
  plt.legend()
  plt.show()
  
  # return the predicted price for given "x" day
  return lin_reg.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0], svr_rbf.predict(x)[0]
  
  
# predict the price of stock on day x
x= predict_prices(dates, prices, [[28]])
print("predicted price using linear regression : ", x[0])
print("predicted price using SVR Linear regression : ", x[1])
print("predicted price using SVR  Polynomial regression : ", x[2])
print("predicted price using SVR RBF  : ", x[3])
