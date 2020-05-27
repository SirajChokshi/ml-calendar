#!/usr/bin/env python
# coding: utf-8

# In[25]:


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


# In[26]:


# format all independent values
X = np.transpose([x1, x2])

# X is a matrix with all of the independent variable values

print(X.shape)


# In[27]:


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


# In[28]:


gradient = SGDRegressor()

gradient.fit(X_train, y_train)

gradient_predictions = gradient.predict(X_test)

gradient_errors = []


# In[29]:


gradient.predict(X_test)

plt.scatter(y_test,gradient.predict(X_test))
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('scatter plot between actual y and predicted y')
plt.show()
print('Mean Squared Error :',mean_squared_error(y_test, gradient.predict(X_test)))
print('Mean Absolute Error :',mean_absolute_error(y_test, gradient.predict(X_test)))


# In[30]:


# SkLearn SGD classifier predicted weight matrix
sklearn_w=gradient.coef_
sklearn_w


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

