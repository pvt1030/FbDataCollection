import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn import linear_model
from termcolor import colored

# print the csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
data = pd.read_csv('TrainingSet.csv')
# print(colored('dataset', 'red'))
# print(data)

# pre-processing
# handling missing values
data['groups'] = data['groups'].replace(0, int(round(data['groups'].mean())))
# print(data)
# feature extraction
x = data.drop(['name', '_id', 'id', 'gender', 'quotes', 'birthday'], axis=1)
print(colored('dropped columns', 'red'))
print(x)

# normalization
normalized_X = preprocessing.normalize(x)
print(colored('normalized_X', 'red'))
print(type(normalized_X))
print(normalized_X.shape)


def openness():
    print(colored('Predicting openness from likes,no_of_posts,no_of_posts_with_description and groups', 'red'))
    X = x[['likes', 'groups', 'no_of_posts', 'no_of_posts_with_description']]
    y = x['Openness']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def conscientiousness():
    print(colored('Predicting Conscientiousness from likes,no_of_albums,  and groups', 'red'))
    X = x[['likes', 'no_of_albums',  'groups']]
    y = x['Conscientiousness']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def extraversion():
    print(colored('Predicting Extraversion from likes,friends and groups', 'red'))
    X = x[['likes', 'friends', 'groups']]
    y = x['Extraversion']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def aggreeableness():
    print(colored('Predicting agreeableness from likes', 'red'))
    X = x[['likes']]
    y = x['Agreeableness']
    regr = linear_model.LinearRegression()
    regr.fit(X, y)
    print('Intercept : \n', regr.intercept_)
    print('Coefficients: \n', regr.coef_)


def neuroticism():
    print(colored('Predicting neuroticism from likes and friends', 'red'))
    X = x[['likes', 'friends']]
    y = x['Neuroticism']
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











