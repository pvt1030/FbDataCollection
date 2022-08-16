import pandas as pd
from sklearn import preprocessing
import numpy as np
from termcolor import colored


# print the csv
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
data = pd.read_csv('dataset.csv')
# print(data)

# pre-processing
# handling missing values
data['groups'] = data['groups'].replace(0, int(round(data['groups'].mean())))
print(data)
# feature extraction
X = data.drop(['name', '_id', 'id'], axis=1)
print(X)
print(type(X))

# normalization
normalized_X = preprocessing.normalize(X)
print(normalized_X)
print(type(normalized_X))
print(normalized_X.shape)

# sorting columns
friends_sorted = data.sort_values(['friends'])
photos_sorted = data.sort_values(['photos'])
groups_sorted = data.sort_values(['groups'])
likes_sorted = data.sort_values(['likes'])
uploaded_photos_sorted = data.sort_values(['uploaded_photos'])
tagged_photos_sorted = data.sort_values(['tagged_photos'])

# model building
print(colored('predicting personality', 'red'))


def denormalize(v):
    new_val = ((v-0)/(1-0)) * (100 - 1) + 1
    return new_val


def modify_csv(o , c , e, a, n):
    X['openness'] = o
    X['conscientiousness'] = c
    X['extraversion'] = e
    X['aggreeableness'] = a
    X['neuroticism'] = n
    print(X)


# for x in range(np.shape(normalized_X)[0]):
#     print(x)
#     row = normalized_X[x]
#     friends = row[0]
#     photos = row[1]
#     groups = row[2]
#     likes = row[3]
#     uploaded_photos = row[4]
#     tagged_photos = row[5]
#     photos = uploaded_photos + tagged_photos

o = []
c = []
e = []
a = []
n = []

for i in X.itertuples():
    # print(i)
    row = i
    friends = row[0]
    photos = row[1]
    groups = row[2]
    likes = row[3]
    uploaded_photos = row[4]
    tagged_photos = row[5]
    photos = uploaded_photos + tagged_photos

    b_o = 63.30898715076901
    b_c = 47.39484303987095
    b_e = 41.20481622748352
    b_a = 62.34876573891016
    b_n = 53.246258287278685

    openness = b_o + 0.00341656 * likes + 0.0907767 * groups
    conscientiousness = b_c + 0.01412139 * likes + -0.13966486 * groups + 0.18113189 * uploaded_photos + 0.04623085 * tagged_photos
    extraversion = b_e + 0.00020431 * likes + 0.17572136 * groups + 0.00286016 * friends
    aggreeableness = b_a + 0.00094047 * likes
    neuroticism = b_n + -0.01206271 * likes + 0.00244296 * friends

    o.append(openness)
    c.append(conscientiousness)
    e.append(extraversion)
    a.append(aggreeableness)
    n.append(neuroticism)

    # print(f'openness :{denormalize(openness)}')
    # print(f'conscientiousness : {denormalize(conscientiousness)}')
    # print(f'extraversion : {denormalize(extraversion)}')
    # print(f'aggreeableness : {denormalize(aggreeableness)}')
    # print(f'neuroticism  : {denormalize(neuroticism)}')


modify_csv(o, c, e, a, n)








