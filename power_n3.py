


import numpy as np
import pandas as pd
#import sklearn.linear.model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

'''
nf=open('data3.csv','w')
#nf.write('EAN;Reg;Dt;St;to;Value;Unit')
with open('data1.csv') as o:
	for line3 in o:
		if 'Value' in line3:
			nf.write('EAN;Clas;Date;Mon;Year;StartTime;EndTime;Value;Unit')
		if 'A+' in line3:
			l=line3.split(';')
			l1=l[2].split('/')
			#print l1
			l2=l1[0]
			line4=''
			for u in range(1,len(l1)):
				l2=l2+';'+l1[u]
			line4=l[0]+';'+l[1]+';'+l2+';'+l[3]+';'+l[4]+';'+l[5]+';'+l[6]
			nf.write(str(line4))
			nf.write('\n')
			#print (line4), l[6]
		#print line3
'''		
df=pd.read_csv('data3.csv',sep=';', encoding="utf-8-sig")
#print (df.head())	
y=df['Value']
x=df[['Date','Year','Mon','StartTime']] #increase features here by adding column name from line num 17

#print x,y

#x= x.values.reshape(-1, 1)
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


