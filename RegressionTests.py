# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:15:55 2022

@author: ledin
"""
import os
import numpy as np
import pandas as pd
# import statsmodels.api as sm
# chi-squared test with similar proportions
from scipy.stats import chi2_contingency
# import statsmodels as sm
import statsmodels.regression.linear_model as sm

os.chdir('C:\\Users\\ledin\\Desktop\\Capstone')
print(os.getcwd())

ApealsKids = pd.read_excel('Capstone Data.xlsx',sheet_name=2)
ApealsKids.replace({'Appeal Granted? Y/N':{'Y':1, 'N':0},
                    'Final Grade Appealed/ Rejected Course':{'A':0.90,'B':0.80,'C':0.70,
                                                              'D':0.60,'F':0},
                    '10th Tracked Up, Down, or Same':{'Up':2,'Same':1,'Down':0},
                    '11th Tracked up, down, or same?':{'Up':2,'Same':1,'Down':0},
                    'Course Requested by Appeal':{'Geometry Honors':1,
                                                  'Biology Academic':2,
                                                  'English 9 Honors':3,
                                                  'English 9 Honors ':3,
                                                  'Biology Honors':4},
                    '11th Grade Course Taken':{'AP Physics 1':1,
                                                  'Chemistry Honors':2,
                                                  'AP Biology':3,
                                                  'AP Eng Lang':4,
                                                  'Physics Academic':5,
                                                  'PreCalc Academic':6,
                                                  'Chemistry Academic':7,
                                                  'English Honors 11':8,
                                                  'English 11 Honors':8,
                                                  'English 11 Academic':9,
                                                  'PreCalc Honors':10}},inplace = True)

ApealsKids.rename(columns={'Appeal Granted? Y/N':'Appeal Granted', 
                            'Final Grade Appealed/ Rejected Course':'Final Grade',
                            '10th Tracked Up, Down, or Same':'10th Direction'},inplace = True)

train = ApealsKids[ApealsKids['Grad Cohort'] < 2024]

x = train[[ 'Grad Cohort',
    'Course Requested by Appeal',
    '11th Grade Course Taken',
                      'Appeal Granted',
                    'Final Grade',
                    '10th Direction',]]
y = train[['11th Tracked up, down, or same?']]

x['const'] = 1

result = sm.OLS(y,x).fit()
print(result.summary())











