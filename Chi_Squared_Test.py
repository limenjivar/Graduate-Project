# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:10:17 2022

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
import matplotlib.pyplot as plt 

os.chdir('C:\\Users\\ledin\\Desktop\\Capstone')
print(os.getcwd())

ApealsKids = pd.read_excel('Capstone Data.xlsx',sheet_name=2)
Grades = pd.read_excel('Letter Grade Analysis Appeal vs Recommended.xlsx')

overall  = Grades[['Cohort','A','B','C','D','F']]
overall = overall.dropna()
overall = overall.groupby(['Cohort'])['A','B','C','D','F'].sum().reset_index()
overall = pd.melt(overall,id_vars=['Cohort'],value_vars=['A','B','C','D','F'])


dat1 = overall[overall['Cohort']=='18-19']
tr1 = plt.bar(dat1['variable'],dat1['value'])

for r1 in tr1:
    h1 = r1.get_height()
    plt.text(r1.get_x() + r1.get_width() / 2., h1 /2 + 35, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

plt.title('Grades: 18-19')
plt.show()

dat2 = overall[overall['Cohort']=='19-20']
tr2 = plt.bar(dat2['variable'],dat2['value'])

for r1 in tr2:
    h1 = r1.get_height()
    plt.text(r1.get_x() + r1.get_width() / 2., h1 /2 + 35, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

plt.title('Grades: 19-20')
plt.show()

dat3 = overall[overall['Cohort']=='20-21']
tr3 = plt.bar(dat3['variable'],dat3['value'])

for r1 in tr3:
    h1 = r1.get_height()
    plt.text(r1.get_x() + r1.get_width() / 2., h1 /2 + 35, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

plt.title('Grades: 20-21')
plt.show()



# ApealsKids.rename(columns={'Appeal Granted? Y/N':'Appeal Granted', 
#                            'Final Grade Appealed/ Rejected Course':'Final Grade',
#                            '10th Tracked Up, Down, or Same':'10th Direction'},inplace = True)

# CoGradApeals = ApealsKids[['Year of Appeal','Final Grade']]
# CoGradApeals = CoGradApeals.groupby(['Year of Appeal','Final Grade'])['Final Grade'].count().to_frame()
# CoGradApeals.rename(columns = {'Final Grade': 'Counts'},inplace=True)
# CoGradApeals.reset_index(inplace =True)

# one = CoGradApeals[CoGradApeals['Year of Appeal']=='18-19']
# bx1 = plt.bar(one['Final Grade'], one['Counts'])

# for r1 in bx1:
#     h1 = r1.get_height()
#     plt.text(r1.get_x() + r1.get_width() / 2., h1 /2, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Year of Appeal: 18-19')
# plt.show()

# two = CoGradApeals[CoGradApeals['Year of Appeal']=='19-20']
# bx2 = plt.bar(two['Final Grade'], two['Counts'])

# for r1 in bx2:
#     h1 = r1.get_height()
#     plt.text(r1.get_x() + r1.get_width() / 2., h1 /2, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Year of Appeal: 19-20')
# plt.show()

# three = CoGradApeals[CoGradApeals['Year of Appeal']=='20-21']
# bx3 = plt.bar(three['Final Grade'], three['Counts'])

# for r1 in bx3:
#     h1 = r1.get_height()
#     plt.text(r1.get_x() + r1.get_width() / 2., h1 /2 +5, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Year of Appeal: 20-21')
# plt.show()

# stat, p, dof, expected = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],
#                                                       ApealsKids['10th Direction']),lambda_="log-likelihood")
# print(p)

# stat2, p2, dof2, expected2 = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],
#                                                       ApealsKids['11th Tracked up, down, or same?']),
#                                            lambda_="log-likelihood")
# print(p2)

# stat3, p3, dof3, expected3 = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],
#                                                       ApealsKids['Course Requested by Appeal']),
#                                            lambda_="log-likelihood")
# print(p3)

# stat4, p4, dof4, expected4 = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],
#                                                       ApealsKids['10th Grade Course Taken']),
#                                            lambda_="log-likelihood")
# print(p4)

# stat5, p5, dof5, expected5 = chi2_contingency(pd.crosstab(ApealsKids['Appeal Granted'],
#                                                       ApealsKids['11th Grade Course Taken']),
#                                            lambda_="log-likelihood")
# print(p5)

# a = pd.crosstab(Grades['Course'], Grades['Status'])
# Grades2 = Grades[['Course','Status','A','B','C','D','F']]
# Grades_Course = Grades2.groupby(['Course'])['A','B','C','D','F'].sum()
# Grades_Status = Grades2.groupby(['Status'])['A','B','C','D','F'].sum()

# ###########################################################################################
# stat6, p6, dof6, expected6 = chi2_contingency(Grades_Course,
#                                            lambda_="log-likelihood")
# print(p6)

# Grades_Course = Grades_Course.reset_index()
# Grades_Course = np.transpose(Grades_Course).reset_index()
# names = Grades_Course.iloc[0]
# Grades_Course = Grades_Course[1:]
# Grades_Course.columns = names

# BA = Grades_Course[['Course','Biology Academic']]
# ax1 = plt.bar(BA['Course'],BA['Biology Academic'])

# for r1 in ax1:
#     h1 = r1.get_height()
#     plt.text(r1.get_x() + r1.get_width() / 2., h1 + 20, "%d" % h1, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Biology Academic')
# plt.show()


# ax2 = plt.bar(Grades_Course['Course'],Grades_Course['Biology Honors'])
# for r2 in ax2:
#     h2 = r2.get_height()
#     plt.text(r2.get_x() + r2.get_width() / 2., h2 + 20, "%d" % h2, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Biology Honors')
# plt.show()

# ax3 = plt.bar(Grades_Course['Course'],Grades_Course['English 9 Honors'])
# for r3 in ax3:
#     h3 = r3.get_height()
#     plt.text(r3.get_x() + r3.get_width() / 2., h3 + 20, "%d" % h3, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('English 9 Honors')
# plt.show()

# ax4 = plt.bar(Grades_Course['Course'],Grades_Course['Geometry Honors'])
# for r4 in ax4:
#     h4 = r4.get_height()
#     plt.text(r4.get_x() + r4.get_width() / 2., h4 + 20, "%d" % h4, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Geometry Honors')
# plt.show()

# #######################################################################################

# stat7, p7, dof7, expected7 = chi2_contingency(Grades_Status,
#                                            lambda_="log-likelihood")
# print(p7)

# Grades_Status = Grades_Status.reset_index()
# Status = Grades_Status[Grades_Status['Status']=='Appealed']
# Status = np.transpose(Status).reset_index()
# Statnames = Status.iloc[0]
# Status = Status[1:]
# Status.columns = Statnames

# ax5 = plt.bar(Status['Status'],Status['Appealed'])
# for r5 in ax5:
#     h5 = r5.get_height()
#     plt.text(r5.get_x() + r5.get_width() / 2., h5 + 5, "%d" % h5, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Appealed')
# plt.show()

# recomend = Grades_Status[Grades_Status['Status']=='Recommended']
# recomend = np.transpose(recomend).reset_index()
# recnames = recomend.iloc[0]
# recomend = recomend[1:]
# recomend.columns = recnames

# ax6 = plt.bar(recomend['Status'],recomend['Recommended'])
# for r6 in ax6:
#     h6 = r6.get_height()
#     plt.text(r6.get_x() + r6.get_width() / 2., h6 + 45, "%d" % h6, ha="center", va="top", color="Black", fontsize=16, fontweight="bold")

# plt.title('Recommended')
# plt.show()







