import pandas as pd
from sklearn import preprocessing
import numpy as np


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
print("iterating the ndarray")

for x in range(np.shape(normalized_X)[0]):
    print(x)
    row = normalized_X[x]
    friends = row[0]
    photos = row[1]
    groups = row[2]
    likes = row[3]
    uploaded_photos = row[4]
    tagged_photos = row[5]
    photos = uploaded_photos + tagged_photos

    b_0 = 0
    e = 1

    openness = b_0 + 0.102 * likes + 0.077 * groups + e
    conscientiousness = b_0 + (-0.088)*likes + (-0.0697)*groups + 0.0330 * photos + e
    extraversion = b_0 + 0.034*likes + 0.069*groups + 0.177*friends + e
    aggreeableness = b_0 + (-0.036)*likes + e
    neuroticism = b_0 + 0.075*likes + (-0.059)*friends + e

    print(f'openness : {openness}')
    print(f'friends : {friends}')
    print(f'photos : {photos}')
    print(f'groups : {groups}')
    print(f'likes : {likes}')
    print(f'uploaded_photos : {uploaded_photos}')
    print(f'tagged_photos : {tagged_photos}')




