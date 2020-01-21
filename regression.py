import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn import linear_model

# print the csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
data = pd.read_csv('datasetwithpers.csv')
# print(data)

# pre-processing
# handling missing values
data['groups'] = data['groups'].replace(0, int(round(data['groups'].mean())))
print(data)
# feature extraction
x = data.drop(['name', '_id', 'id'], axis=1)
print(x)

# normalization
normalized_X = preprocessing.normalize(x)
print(normalized_X)
print(type(normalized_X))
print(normalized_X.shape)


def openness():
    print('Predicting openness from likes and groups')
    X = x[['likes', 'groups']]
    y = x['o']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def conscientiousness():
    print('Predicting Conscientiousness from likes,uploaded_photos, tagged_photos and groups')
    X = x[['likes', 'uploaded_photos', 'tagged_photos',  'groups']]
    y = x['c']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def extraversion():
    print('Predicting Extraversion from likes,friends and groups')
    X = x[['likes', 'friends', 'groups']]
    y = x['e']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def aggreeableness():
    print('Predicting agreeableness from likes')
    X = x[['likes']]
    y = x['a']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def neuroticism():
    print('Predicting neuroticism from likes and friends')
    X = x[['likes', 'friends']]
    y = x['n']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


openness()
conscientiousness()
extraversion()
aggreeableness()
neuroticism()



# # normalization
# normalized_X = preprocessing.normalize(X)
# print(normalized_X)
# print(type(normalized_X))
# print(normalized_X.shape)






