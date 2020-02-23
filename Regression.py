import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from termcolor import colored
import numpy as np

# print the csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
dataset_train = pd.read_csv('TrainingSet.csv')
dataset_test = pd.read_csv('TestSet.csv')

# Train the model -------------------------------------------

#   Train test
train_x = dataset_train.drop(['name', '_id', 'id', 'gender', 'quotes', 'birthday'], axis=1)

# actual class variable values
actual_openness = dataset_test['Openness']
actual_con = dataset_test['Conscientiousness']
actual_Extraversion = dataset_test['Extraversion']
actual_Agreeableness = dataset_test['Agreeableness']
actual_Neuroticism = dataset_test['Neuroticism']

# test_set
test_x = dataset_test
openness_x = test_x[['likes', 'groups', 'no_of_posts', 'no_of_posts_with_description']]
conscientiousness_x = test_x[['likes', 'no_of_albums',  'groups']]
extraversion_x = test_x[['likes', 'friends', 'groups']]
aggreeableness_x = test_x[['likes']]
neuroticism_x = test_x[['likes', 'friends']]

# personality prediction logic


def openness():
    x1 = train_x[['likes', 'groups', 'no_of_posts', 'no_of_posts_with_description']]
    openness = train_x['Openness']

    # define multiple linear regression model
    linear_regression = LinearRegression()

    # fit the multiple linear regression model
    linear_regression.fit(x1, openness)

    openness_x = test_x[['likes', 'groups', 'no_of_posts', 'no_of_posts_with_description']]
    openness_pred = linear_regression.predict(openness_x)
    print(colored('Openness and likes,groups,no.of posts and no of posts with description', 'red'))
    # print(openness_pred)

    print(colored('mean squared error', 'green'))
    mse = mean_squared_error(actual_openness, openness_pred)
    print(mse)

    # Root Mean Squared Deviation
    rmsd = np.sqrt(mean_squared_error(actual_openness, openness_pred))
    r2_value = r2_score(actual_openness, openness_pred)
    print(colored('Root Mean Square Error', 'green'))
    print(rmsd)
    print(colored('R^2 Value:', 'green'))
    print(r2_value)

    df = pd.DataFrame({'Actual': actual_openness, 'Predicted': openness_pred})
    print(df.head(20))


def conscientiousness():
    x2 = train_x[['likes', 'no_of_albums',  'groups']]
    conscientiosness = train_x['Conscientiousness']
    linear_regression = LinearRegression()
    linear_regression.fit(x2, conscientiosness)

    conscientiosness_pred = linear_regression.predict(conscientiousness_x)
    print(colored('conscientiosness and likes,groups,no.of posts and no of posts with description', 'red'))
    # print(conscientiosness_pred)

    print(colored('mean squared error', 'green'))
    mse = mean_squared_error(actual_con, conscientiosness_pred)
    print(mse)

    # Root Mean Squared Deviation
    rmsd = np.sqrt(mean_squared_error(actual_con, conscientiosness_pred))
    r2_value = r2_score(actual_con, conscientiosness_pred)
    print(colored('Root Mean Square Error', 'green'))
    print(rmsd)
    print(colored('R^2 Value:', 'green'))
    print(r2_value)

    df = pd.DataFrame({'Actual': actual_con, 'Predicted': conscientiosness_pred})
    print(df.head(20))


def extraversion():
    x3 = train_x[['likes', 'friends', 'groups']]
    extraversion = train_x['Extraversion']
    linear_regression = LinearRegression()
    linear_regression.fit(x3, extraversion)

    extraversion_pred = linear_regression.predict(extraversion_x)
    print(colored('Extraversion and likes,groups,no.of posts and no of posts with description', 'red'))
    # print(extraversion_pred)

    print(colored('mean squared error', 'green'))
    mse = mean_squared_error(actual_Extraversion, extraversion_pred)
    print(mse)

    # Root Mean Squared Deviation
    rmsd = np.sqrt(mean_squared_error(actual_Extraversion, extraversion_pred))
    r2_value = r2_score(actual_Extraversion, extraversion_pred)
    print(colored('Root Mean Square Error', 'green'))
    print(rmsd)
    print(colored('R^2 Value:', 'green'))
    print(r2_value)

    df = pd.DataFrame({'Actual': actual_Extraversion, 'Predicted': extraversion_pred})
    print(df.head(20))


def aggreeableness():
    x4 = train_x[['likes']]
    agreeableness = train_x['Agreeableness']
    linear_regression = LinearRegression()
    linear_regression.fit(x4, agreeableness)

    agreeableness_pred = linear_regression.predict(aggreeableness_x)
    print(colored('Agreeableness and likes,groups,no.of posts and no of posts with description', 'red'))
    # print(agreeableness_pred)

    print(colored('mean squared error', 'green'))
    mse = mean_squared_error(actual_Agreeableness, agreeableness_pred)
    print(mse)

    # Root Mean Squared Deviation
    rmsd = np.sqrt(mean_squared_error(actual_Agreeableness, agreeableness_pred))
    r2_value = r2_score(actual_Agreeableness, agreeableness_pred)
    print(colored('Root Mean Square Error ', 'green'))
    print(rmsd)
    print(colored('R^2 Value:', 'green'))
    print(r2_value)

    df = pd.DataFrame({'Actual': actual_Agreeableness, 'Predicted': agreeableness_pred})
    print(df.head(20))


def neuroticism():
    x5 = train_x[['likes', 'friends']]
    neuroticism = train_x['Neuroticism']
    linear_regression = LinearRegression()
    linear_regression.fit(x5, neuroticism)

    neuroticism_pred = linear_regression.predict(neuroticism_x)
    print(colored('Neuroticism and likes,groups,no.of posts and no of posts with description', 'red'))
    # print(neuroticism_pred)

    print(colored('mean squared error', 'green'))
    mse = mean_squared_error(actual_Neuroticism, neuroticism_pred)
    print(mse)

    # Root Mean Squared Deviation
    rmsd = np.sqrt(mean_squared_error(actual_Neuroticism, neuroticism_pred))
    r2_value = r2_score(actual_Neuroticism, neuroticism_pred)
    print(colored('Root Mean Square Error', 'green'))
    print(rmsd)
    print(colored('R^2 Value:', 'green'))
    print(r2_value)

    df = pd.DataFrame({'Actual': actual_Neuroticism, 'Predicted': neuroticism_pred})
    print(df.head(20))




openness()
conscientiousness()
extraversion()
aggreeableness()
neuroticism()

# predict with the data







