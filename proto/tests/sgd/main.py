#!/usr/bin/env python
# coding: utf-8

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

class SGD:
    def __init__(self, dataset, degrees = 3):
        self.poly = PolynomialFeatures(degree=degrees)
        self.seed = self.get_seed()
        self.dataset = dataset
        self.X = self.format_data(self.dataset)[0]
        self.y = self.format_data(self.dataset)[1]
        self.train_test_data = self.split_data(self.X, self.y, self.seed)
        self.transformed_data = self.transform_poly(self.poly, self.train_test_data[0], self.train_test_data[2])
        self.regression = self.get_regression(self.transformed_data[0], self.train_test_data[1])

    def set_train_test_seed(self, seed):
        self.seed = seed

    # randomize seed for train/test split
    def get_seed(self):
        return random.randint(0, 9999)

    # format dataset
    def format_data(self, dataset):
        x1 = list(dataset['start'])
        x2= list(dataset['end'])
        X = np.transpose([x1, x2])
        y = list(dataset['val'])
        return (X, y)

    # X_train, X_test, y_train, y_test
    def split_data(self, X, y, train_test_seed):
        X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.3, random_state=train_test_seed)

        X_train = np.array(X_train)
        y_train = np.array(y_train)
        X_test = np.array(X_test)
        y_test = np.array(y_test)

        return (X_train, y_train, X_test, y_test)

    # transform for polynomial fit and standardize data
    def transform_poly(self, poly, X_train, X_test):
        X_train = poly.fit_transform(X_train)
        X_test = poly.fit_transform(X_test)
        scaler = preprocessing.StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        X_test=scaler.transform(X_test)
        return (X_train, X_test)

    # construct Polynomial object
    def get_regression(self, X_train, y_train):
        gradient = SGDRegressor()
        gradient.fit(X_train, y_train)
        return gradient

    def get_tests(self):
        return self.regression.predict(self.transformed_data[1])

    def get_predictions(self, dataset):
        return self.regression.predict(dataset)

def read_file(path):
    return pd.read_csv(path) # path default 'data.csv'

# gradient_errors = []

# # plt.scatter(y_test,gradient.predict(X_test))
# # plt.grid()
# # plt.xlabel('Actual y')
# # plt.ylabel('Predicted y')
# # plt.title('scatter plot between actual y and predicted y')
# # plt.show()
# # print('Mean Squared Error :',mean_squared_error(y_test, gradient.predict(X_test)))
# # print('Mean Absolute Error :',mean_absolute_error(y_test, gradient.predict(X_test)))

# # # print predicted values (truncated) vs actual values
# # print("{:9s} {:9s} {}".format("Predicted", "Actual", "% Error"))
# # for row in range(0, len(gradient_predictions)):
# # 	percent_error = abs((gradient_predictions[row] - y_test[row])/gradient_predictions[row] * 100)
# # 	gradient_errors.append(percent_error)
# # 	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# # # print average percent error
# # print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors)))

# def get_confusion_matrix(x_test, y_test):
#     np.corrcoef(gradient.predict(x_test), y_test)


# newX = [[17000,24000], [26000,34000]]

# newX = np.array(newX)

# newX = poly.fit_transform(newX)

# print(type(X_test))
# print(type(newX))

# print(X_test.shape)
# print(newX.shape)



# print("size of newX:", len(newX))
# print("size of X_test:", len(X_test))

# newY = [18326, 26001]

# newY = np.array(newY)


# # standardizing data
# scaler = preprocessing.StandardScaler().fit(newX)
# newX = scaler.transform(newX)

# print(newY)


# # In[138]:


# # print(newX.shape)

# gradient.partial_fit(newX, newY)

# gradient_predictions_iso = gradient.predict(newX)
# gradient_predictions_total = gradient.predict(X_test)


# gradient_errors_iso = []
# gradient_errors_total = []

# print("number of new points:", len(gradient_predictions_iso))
# print("\n")

# # print predicted values (truncated) vs actual values
# for row in range(0, len(gradient_predictions_iso)):
# 	percent_error = abs((gradient_predictions_iso[row] - newY[row])/gradient_predictions_iso[row] * 100)
# 	gradient_errors_iso.append(percent_error)
# 	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# # print average percent error
# print("Calculating the error among just the two new points")
# print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors_iso)))

# print("\n")
# print("number of total points:", len(gradient_predictions_total))
# # print predicted values (truncated) vs actual values
# for row in range(0, len(gradient_predictions_total)):
# 	percent_error = abs((gradient_predictions_total[row] - y_test[row])/gradient_predictions_total[row] * 100)
# 	gradient_errors_total.append(percent_error)
# 	# print("{:9s} {:9s} {:5f}".format(str(int(gradient_predictions[row])), str(y_test[row]), percent_error))

# # print average percent error
# print("Calculating the error among all of the test points")
# print("\n{:19s} {:5f}".format("Avg % Error:", np.average(gradient_errors_total)))

# print("\n")
# print("Confusion/Covariance Matrix")
# print(np.corrcoef(gradient.predict(X_test), y_test))

