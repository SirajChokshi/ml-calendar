#!/usr/bin/env python
# coding: utf-8

# In[130]:


# imports
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, mean_absolute_error
from numpy import random
from sklearn.model_selection import train_test_split

# randomize seed for train/test split
TRAIN_TEST_SEED = random.randint(0, 9999)

# fetch Data
dataset = pd.read_csv('data.csv')
x1 = list(dataset['start'])
x2= list(dataset['end'])
y = list(dataset['val'])

print(TRAIN_TEST_SEED)


# In[131]:


# format all independent values
X = np.transpose([x1, x2])

# X is a matrix with all of the independent variable values

print(X.shape)


# In[132]:


# split data into training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=TRAIN_TEST_SEED)

X_train = np.array(X_train)
print(X_train.shape)
y_train = np.array(y_train)
print(y_train.shape)
X_test = np.array(X_test)
print(X_test.shape)
y_test = np.array(y_test)
print(y_test.shape)

# construct Polynomial object
poly = PolynomialFeatures(degree=3)

# transform for polynomial fit
X_train = poly.fit_transform(X_train)

X_test = poly.fit_transform(X_test)

# standardizing data
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)


# In[133]:


print(X_train.shape)
print(y_train.shape)

gradient = SGDRegressor()

gradient.fit(X_train, y_train)

gradient_predictions = gradient.predict(X_test)

gradient_errors = []


# In[134]:


gradient.predict(X_test)

plt.scatter(y_test,gradient.predict(X_test))
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('scatter plot between actual y and predicted y')
plt.show()
print('Mean Squared Error :',mean_squared_error(y_test, gradient.predict(X_test)))
print('Mean Absolute Error :',mean_absolute_error(y_test, gradient.predict(X_test)))


# In[135]:


# SkLearn SGD classifier predicted weight matrix
sklearn_w=gradient.coef_
sklearn_w


# In[136]:


# In[31]:


# print predicted values (truncated) vs actual values
print("{:9s} {:9s} {}".format("Predicted", "Actual", "% Error"))
for row in range(0, len(gradient_predictions)):
	percent_error = abs((gradient_predictions[row] - y_test[row])/gradient_predictions[row] * 100)
	gradient_errors.append(percent_error)
	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors)))

print("Confusion/Covariance Matrix")
print(np.corrcoef(gradient.predict(X_test), y_test))


# In[137]:


newX = [[17000,24000], [26000,34000]]

newX = np.array(newX)

newX = poly.fit_transform(newX)

print(type(X_test))
print(type(newX))

print(X_test.shape)
print(newX.shape)



print("size of newX:", len(newX))
print("size of X_test:", len(X_test))

newY = [18326, 26001]

newY = np.array(newY)


# standardizing data
scaler = preprocessing.StandardScaler().fit(newX)
newX = scaler.transform(newX)

print(newY)


# In[138]:


# print(newX.shape)

gradient.partial_fit(newX, newY)

gradient_predictions_iso = gradient.predict(newX)
gradient_predictions_total = gradient.predict(X_test)


gradient_errors_iso = []
gradient_errors_total = []

print("number of new points:", len(gradient_predictions_iso))
print("\n")

# print predicted values (truncated) vs actual values
for row in range(0, len(gradient_predictions_iso)):
	percent_error = abs((gradient_predictions_iso[row] - newY[row])/gradient_predictions_iso[row] * 100)
	gradient_errors_iso.append(percent_error)
	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("Calculating the error among just the two new points")
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors_iso)))

print("\n")
print("number of total points:", len(gradient_predictions_total))
# print predicted values (truncated) vs actual values
for row in range(0, len(gradient_predictions_total)):
	percent_error = abs((gradient_predictions_total[row] - y_test[row])/gradient_predictions_total[row] * 100)
	gradient_errors_total.append(percent_error)
	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("Calculating the error among all of the test points")
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors_total)))

print("\n")
print("Confusion/Covariance Matrix")
print(np.corrcoef(gradient.predict(X_test), y_test))

