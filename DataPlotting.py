#!/usr/bin/env python
# coding: utf-8

# In[237]:


# imports
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# randomize seed for train/test split
TRAIN_TEST_SEED = random.randint(0, 9999)

# fetch Data
dataset = pd.read_csv('/Users/atharvak/Desktop/Projects/time-finder-master/data.csv')
x1 = list(dataset['start'])
x2= list(dataset['end'])
y = list(dataset['val'])

print(TRAIN_TEST_SEED)


# In[238]:


# format all independent values
X = np.transpose([x1, x2])

# X is a matrix with all of the independent variable values
# print(X)


# In[239]:


# split data into training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=TRAIN_TEST_SEED)

# dependent variable
vector = y_train

print(X_test)
print(y_test)

print(len(X_test))
print(len(y_test))


# In[240]:


# np array for independent variables in test cases
predict= np.array(X_test)

print(predict)

# construct Polynomial object
poly = PolynomialFeatures(degree=2)

# transform for fit
# transforms the data for a way so that the model can interpret it
X_in = poly.fit_transform(X_train)

# print(X_in)

predict_in = poly.fit_transform(predict)

# print(predict_in)


# In[241]:


# use processed data for regression
clf = linear_model.LinearRegression()
clf.fit(X_in, vector)

# predict testing values with regression
predictions = clf.predict(predict_in)

percent_errors = []

elastic = linear_model.ElasticNetCV()
elastic.fit(X_in, vector)

elastic_predictions = elastic.predict(predict_in)

more_errors = []


# In[242]:


# print predicted values (truncated) vs actual values
print("{:9s} {:9s} {}".format("Predicted", "Actual", "% Error"))
for row in range(0, len(predictions)):
	percent_error = abs((predictions[row] - y_test[row])/predictions[row] * 100)
	percent_errors.append(percent_error)
	print("{:9s} {:9s} {:5f}".format(str(int(predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(percent_errors)))


# In[243]:


# print predicted values (truncated) vs actual values
print("{:9s} {:9s} {}".format("Predicted", "Actual", "% Error"))
for row in range(0, len(elastic_predictions)):
	percent_error = abs((elastic_predictions[row] - y_test[row])/elastic_predictions[row] * 100)
	more_errors.append(percent_error)
	print("{:9s} {:9s} {:5f}".format(str(int(elastic_predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(more_errors)))


# In[244]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_axis = []
y_axis = []

for row in range(0, len(X_test)):
    x_axis.append(X_test[row][0])
    y_axis.append(X_test[row][1])
    
# print(x_axis)
# print(y_axis)
# print(y_test)

ax.scatter(x_axis, y_axis, y_test, c='r', marker='o')

ax.set_xlabel('Start Time')
ax.set_ylabel('End Time')
ax.set_zlabel('Optimal Suggested Time')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




