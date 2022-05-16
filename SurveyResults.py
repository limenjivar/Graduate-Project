# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:35:33 2022

@author: ledin
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\ledin\\Desktop\\Capstone')
print(os.getcwd())

SurveyR = pd.read_excel('Capstone Data.xlsx', sheet_name=0) 

SurveyR2 = SurveyR[['"Anyone could be an honors student with the right effort and expectations."',
                    '"Students in honors classes receive better instruction."',
                    '"I think the present system of recommending students for courses is appropriate."',
                    '"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."',
                    '"Grades reflect ability."',
                    '"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "']]

colnamelist = list(SurveyR2.columns)

values = ['Strongly Disagree', 'Disagree','Agree','Strongly Agree','No Answer']
for i in colnamelist:
    question = str(i)
    conditions = [(SurveyR2[i] ==1),
                      (SurveyR2[i] ==2),
                               (SurveyR2[i] ==3),
                                        (SurveyR2[i] ==4),
                                        (np.isnan(SurveyR2[i]))
                                        ]
    SurveyR2[i]= np.select(conditions,values)
    


first = SurveyR2.groupby('"Anyone could be an honors student with the right effort and expectations."')['"Anyone could be an honors student with the right effort and expectations."'].count()
first = first.to_frame()
first = first.rename(columns ={'"Anyone could be an honors student with the right effort and expectations."': 'Counts'}).reset_index()
plt.pie(first['Counts'],labels = first['"Anyone could be an honors student with the right effort and expectations."'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"Anyone could be an honors student with the right effort and expectations."')
plt.show()
plt.close()

second = SurveyR2.groupby('"Students in honors classes receive better instruction."')['"Students in honors classes receive better instruction."'].count()
second = second.to_frame()
second = second.rename(columns ={'"Students in honors classes receive better instruction."': 'Counts'}).reset_index()
plt.pie(second['Counts'],labels = second['"Students in honors classes receive better instruction."'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"Students in honors classes receive better instruction."')
plt.show()
plt.close()

third = SurveyR2.groupby('"I think the present system of recommending students for courses is appropriate."')['"I think the present system of recommending students for courses is appropriate."'].count()
third = third.to_frame()
third = third.rename(columns ={'"I think the present system of recommending students for courses is appropriate."': 'Counts'}).reset_index()
plt.pie(third['Counts'],labels = third['"I think the present system of recommending students for courses is appropriate."'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"I think the present system of recommending students for courses is appropriate."')
plt.show()
plt.close()

four = SurveyR2.groupby('"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."')['"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."'].count()
four = four.to_frame()
four = four.rename(columns ={'"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."': 'Counts'}).reset_index()
plt.pie(four['Counts'],labels = four['"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"Students who want to take an honors or AP class should earn the right to do so by getting the requisite grades in the prior school year."')
plt.show()
plt.close()

five = SurveyR2.groupby('"Grades reflect ability."')['"Grades reflect ability."'].count()
five = five.to_frame()
five = five.rename(columns ={'"Grades reflect ability."': 'Counts'}).reset_index()
plt.pie(five['Counts'],labels = five['"Grades reflect ability."'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"Grades reflect ability."')
plt.show()
plt.close()

six = SurveyR2.groupby('"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "')['"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "'].count()
six = six.to_frame()
six = six.rename(columns ={'"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "': 'Counts'}).reset_index()
plt.pie(six['Counts'],labels = six['"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "'],
        startangle=90,shadow=True,autopct='%1.2f%%')
plt.title('"Teaching Academic Level Classes takes more work than teaching Honors Level Classes. "')
plt.show()
plt.close()




