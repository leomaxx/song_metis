
import pickle
import pandas as pd
import numpy as np

from scipy.stats import skew, kurtosis
from collections import Counter
from copy import deepcopy
from fancyimpute import MICE
from datetime import datetime
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import SMOTE

with open('./data/X_train_new.pkl', 'rb') as picklefile:
    X_train_new = pickle.load(picklefile)
with open('./data/y_train_new.pkl', 'rb') as picklefile:
    y_train_new = pickle.load(picklefile)
with open('./data/X_train_2nd.pkl', 'rb') as picklefile:
    X_train_2nd = pickle.load(picklefile)
with open('./data/y_user_train.pkl', 'rb') as picklefile:
    y_user_train = pickle.load(picklefile)

models = [
          ('xgboost', XGBClassifier)
         ]

param_choices = [
    {   'learning_rate':[0.1],
        'n_estimators':[225, 300],
        'max_depth':[5],
        'min_child_weight':range(1,6,3),
        'gamma':[i/10.0 for i in range(0,5)],
        'subsample':[0.8],
        'colsample_bytree':[0.8],
        'objective':['multi:softprob']
    }
]

grids3 = {}
for model_info, params in zip(models, param_choices[:1]):
    name, model = model_info
    grid = RandomizedSearchCV(model(), params, scoring='accuracy', cv=3, n_jobs=-1, verbose=3)
    grid.fit(X_train_new, y_train_new.reshape(-1,))
    s = "{}: best score: {}".format(name, grid.best_score_)
    print(s)
    grids3[name] = grid

model3 = grids3['xgboost'].best_estimator_
with open('../data/model3-12countries-full.pkl', 'wb') as picklefile:
    pickle.dump(model3, picklefile)

print (grids3['xgboost'].best_params_)
