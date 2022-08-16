import pandas as pd
import statsmodels.api as sm
from termcolor import colored

data = pd.read_csv('TotalDataSet.csv')

# Target features
openness = data['Openness']
conscientiousness = data['Conscientiousness']
extraversion = data['Extraversion']
agreeableness = data['Agreeableness']
neuroticism = data['Neuroticism']

# feature matrix
X = data.drop(['name', '_id', 'id', 'gender', 'quotes', 'birthday', 'Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism'], axis=1)

# feature selection -> wrapper_method -> forward selection technique

def forward_selection(x, y, significance_level=0.05):
    initial_features = x.columns.tolist()
    best_features = []
    while len(list(initial_features)) > 0:
        remaining_features = list(set(initial_features)-set(best_features))
        new_pval = pd.Series(index=remaining_features)
        for new_column in remaining_features:
            model = sm.OLS(y, sm.add_constant(data[best_features+[new_column]])).fit()
            new_pval[new_column] = model.pvalues[new_column]
        min_p_value = new_pval.min()
        if min_p_value < significance_level:
            best_features.append(new_pval.idxmin())
        else:
            break
    return best_features


feature_set_openness = forward_selection(X, openness, 0.05)
print(colored('Openness feature matrix'))
print(feature_set_openness)

feature_set_conscientiousness = forward_selection(X, conscientiousness, 0.05)
print(colored('Conscientiousness feature matrix'))
print(feature_set_conscientiousness )

feature_set_extraversion = forward_selection(X, extraversion, 0.05)
print(colored('Extraversion feature matrix'))
print(feature_set_extraversion)

feature_set_agreeableness = forward_selection(X, agreeableness, 0.05)
print(colored('agreeableness feature matrix'))
print(feature_set_agreeableness)

feature_set_neuroticism= forward_selection(X, neuroticism, 0.05)
print(colored('neuroticism feature matrix'))
print(feature_set_neuroticism)
