#Prediction for ENERGY SME. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

dataset = pd.read_csv('iCAB_Monthly.csv')

dataset.shape
dataset.head()

dataset.plot(x='Month', y='Peak', style='o')
plt.title('Month vs Peak')
plt.xlabel('Month')
plt.ylabel('Peak')
plt.show()
#
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.65, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
