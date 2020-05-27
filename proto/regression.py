# imports
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model

# randomize seed for train/test split
TRAIN_TEST_SEED = random.randint(0, 9999)

# fetch Data
dataset = pd.read_csv('data.csv')
x1 = list(dataset['start'])
x2= list(dataset['end'])
y = list(dataset['val'])

# format all independent values
X = np.transpose([x1, x2])

# split data into training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=TRAIN_TEST_SEED)

# dependent variable
vector = y_train

# np array for independent variables in test cases
predict= np.array(X_test)

# construct Polynomial object
poly = PolynomialFeatures(degree=2)

# transform for fit
X_in = poly.fit_transform(X_train)
predict_in = poly.fit_transform(predict)

# use processed data for regression
clf = linear_model.LinearRegression()
clf.fit(X_in, vector)

# predict testing values with regression
predictions = clf.predict(predict_in)

percent_errors = []

# print predicted values (truncated) vs actual values
print("{:9s} {:9s} {}".format("Predicted", "Actual", "% Error"))
for row in range(0, len(predictions)):
	percent_error = abs((predictions[row] - y_test[row])/predictions[row] * 100)
	percent_errors.append(percent_error)
	print("{:9s} {:9s} {:5f}".format(str(int(predictions[row])), str(y_test[row]), percent_error))

# print average percent error
print("\n{:19s} {:5f}".format("Avg % Error:", np.average(percent_errors)))