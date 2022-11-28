


import numpy as np
import pandas as pd
#import sklearn.linear.model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

'''
nf=open('data2.csv','w')
#nf.write('EAN;Reg;Dt;St;to;Value;Unit')
with open('data1.csv') as o:
	for line3 in o:
		if 'Value' in line3:
			nf.write(line3)
		if 'A+' in line3:
			nf.write(line3)
		#print line3
'''		
df=pd.read_csv('data2.csv',sep=';', encoding="utf-8-sig")
print (df.head())	
y=df['Value']
x=df['Local_from_tm']

print x,y

x= x.values.reshape(-1, 1)
y= y.values.reshape(-1, 1)

X_train, X_test, Y_train, Y_test = train_test_split (x, y, test_size = 0.30, random_state=21)



regressor = LinearRegression()
regressor.fit(X_train,Y_train)

print(regressor.intercept_)
print(regressor.coef_)



y_pred = regressor.predict(X_test)


print('Mean Absolute Error:',metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))


