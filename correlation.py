import pandas as pd
from termcolor import colored
from scipy import stats

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)
data = pd.read_csv('TotalDataSet.csv')

x_values = ['friends', 'groups', 'likes', 'photos', 'no_of_languages', 'no_of_albums', 'no_of_favorite_teams', 'no_of_favorite_athletes', 'no_of_interested_music','no_of_posts', 'no_of_posts_with_description', 'no_of_posts_without_description']
y_values = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']

for i in x_values:
    for j in y_values:
        # cor = data[i].corr(data[j])
        name = '{} and {}'.format(i, j)
        print(colored(name, 'green'))
        print(colored('correlation and p value', 'red'))
        pearson = stats.pearsonr(data[i], data[j])
        print(pearson)
        p_value = pearson[1]
        if p_value < 0.05:
            print(colored('valid combinations', 'blue'))
            print(colored(name, 'green'))
            print(colored('correlation and p value', 'red'))
            print(pearson)






