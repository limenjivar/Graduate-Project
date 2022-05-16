# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:14:54 2022

@author: ledin
"""

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
from six import StringIO
import pydotplus
from IPython.display import Image
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier

# chi-squared test with similar proportions
from scipy.stats import chi2_contingency

os.chdir('C:\\Users\\ledin\\Desktop\\Capstone')
print(os.getcwd())

ApealsKids = pd.read_excel('Capstone Data.xlsx',sheet_name=2)
ApealsKids.replace({'Appeal Granted? Y/N':{'Y':1, 'N':0},
                    'Final Grade Appealed/ Rejected Course':{'A':0.90,'B':0.80,'C':0.70,
                                                             'D':0.60,'F':0},
                    '10th Tracked Up, Down, or Same':{'Up':2,'Same':1,'Down':0},
                    '11th Tracked up, down, or same?':{'Up':2,'Same':1,'Down':0}},inplace = True)
ApealsKids.rename(columns={'Appeal Granted? Y/N':'Appeal Granted', 
                           'Final Grade Appealed/ Rejected Course':'Final Grade',
                           '10th Tracked Up, Down, or Same':'10th Direction'},inplace = True)

stat, p, dof, expected = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],ApealsKids['10th Direction']))

featureCols = [
                     'Appeal Granted',
                    'Final Grade',
                    '10th Direction']
targetNames= ['Up', 'Same','Down']

train = ApealsKids[ApealsKids['Grad Cohort'] < 2024]
test = ApealsKids[ApealsKids['Grad Cohort'] == 2024]

x_train = train[[
                     'Appeal Granted',
                    'Final Grade',
                    '10th Direction',]]
y_train = train[['11th Tracked up, down, or same?']]

x_test = test[[
                     'Appeal Granted',
                    'Final Grade',
                    '10th Direction',]]
y_test = test[['11th Tracked up, down, or same?']]

clf = DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
train_pred = clf.predict(x_train)

y_pred = clf.predict(x_test)

fig = plt.figure(figsize=(25,20))
dot_data = tree.plot_tree(clf,
                    feature_names=featureCols,  
                    class_names=targetNames,
                    filled=True)

print(classification_report(y_train, train_pred))
print(confusion_matrix(y_train, train_pred))


rf  = RandomForestRegressor(n_estimators=1500,max_depth=10,oob_score=True,
                            random_state=42)
rf = rf.fit(x_train,y_train)
rf_pred = rf.predict(x_train)

rf_values = [1,0,-1]
conditions = [(rf_pred >= 0.1),
              (rf_pred<0.1) & (rf_pred >= -0.1),
              (rf_pred < -0.1)
              ]

rf_pred2 = np.select(conditions,rf_values)

    
gnb = GaussianNB()
gnb = gnb.fit(x_train,y_train)
gnb_pred = gnb.predict(x_train)



xgb = XGBClassifier()
xgb = xgb.fit(x_train,y_train)
xgb_pred = xgb.predict(x_train)




print("DT Acuracy", accuracy_score(y_train,train_pred))
print("rf Accuracy: ", accuracy_score(y_train, rf_pred2))
print('Naives Accuracy: ', accuracy_score(y_train, gnb_pred))
print("XGB:", accuracy_score(y_train, xgb_pred))


# print("Random Forest Accuracy: ",accuracy_score(y_train, rf_pred))

# graph = graphviz.Source(dot_data, format="png") 
# graph



# dot_data = StringIO()
# export_graphviz(clf,out_file=dot_data,filled=True, rounded=True,
#                  special_characters=True,feature_names=featureCols, class_names = ['1','0','-1'])
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_png('diabetes.png')
# Image(graph.create_png())

# x_train = ApealsKids[ApealsKids['Grad Cohort'] < 2023]

# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = .43)