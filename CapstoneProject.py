# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:37:04 2022

@author: ledin
"""
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\ledin\\Desktop\\Capstone')
print(os.getcwd())

SurveyR = pd.read_excel('Capstone Data.xlsx', sheet_name=0) 
###########################################################################
FinalGrades = pd.read_excel('Capstone Data.xlsx', sheet_name=1)
###########################################################################
ApealsKids = pd.read_excel('Capstone Data.xlsx',sheet_name=2)

Apeals = ApealsKids.groupby([ApealsKids['Year of Appeal'], ApealsKids['Course Requested by Appeal'] ,ApealsKids['Appeal Granted? Y/N']]).size()
Apeals = Apeals.to_frame().reset_index()
Apeals.rename(columns={0:'Counts'},inplace = True)

ApealsY = Apeals[Apeals['Appeal Granted? Y/N'] == 'Y'].reset_index()
ApealsY1 = ApealsY.groupby(['Year of Appeal'])['Counts'].sum().reset_index()

ApealsN = Apeals[Apeals['Appeal Granted? Y/N'] == 'N'].reset_index()
ApealsN1 = ApealsN.groupby(['Year of Appeal'])['Counts'].sum().reset_index()

ax1 = plt.bar(ApealsY1['Year of Appeal'],ApealsY1['Counts'],color='r', label='Appeals Granted')
ax2 = plt.bar(ApealsN1['Year of Appeal'],ApealsN1['Counts'],bottom = ApealsY1['Counts'],color='b', label='Appeals Not Granted')

plt.title('Total Appeals by Academic Year')
plt.legend(loc="best")

for r1,r2 in zip(ax1,ax2):
    h1 = r1.get_height()
    h2 = r2.get_height()
    plt.text(r1.get_x() + r1.get_width() / 2., h1 / 2., "%d" % h1, ha="center", va="bottom", color="white", fontsize=16, fontweight="bold")
    plt.text(r2.get_x() + r2.get_width() / 2., h1 + h2 / 2., "%d" % h2, ha="center", va="bottom", color="white", fontsize =16,fontweight ="bold")

plt.show()

ApealClass = Apeals.groupby('Course Requested by Appeal')['Counts'].sum().reset_index()
# ApealClass.set_index('Course Requested by Appeal',inplace=True)

ApealsYC = ApealsY[['Course Requested by Appeal','Counts']]
ApealsYC['Course Requested by Appeal'] = ApealsYC['Course Requested by Appeal'].str.rstrip()
ApealsYC1 = ApealsYC.groupby(['Course Requested by Appeal'])['Counts'].sum().reset_index()

ApealsNC = ApealsN[['Course Requested by Appeal','Counts']]
ApealsNC['Course Requested by Appeal'] = ApealsNC['Course Requested by Appeal'].str.rstrip()
ApealsNC1 = ApealsNC.groupby(['Course Requested by Appeal'])['Counts'].sum().reset_index()

ax3 = plt.barh(ApealsYC1['Course Requested by Appeal'], ApealsYC1['Counts'], color='g',label='Apeals Granted')
ax4 = plt.barh(ApealsNC1['Course Requested by Appeal'], ApealsNC1['Counts'],left=ApealsYC1['Counts'],
               color = 'r',label = 'Appeals Denied')

plt.title('Appeals by Courses (From Academic Years 18-9 through 20-21)')
plt.legend(loc='best')

for r3,r4 in zip(ax3,ax4):
    h3 = r3.get_width()
    h4 = r4.get_width()
    plt.text(h3/2,  r3.get_y()+0.4,"%d" % h3, ha="left", va="center", color="black", fontsize=16, fontweight="bold")
    plt.text(h4+14,  r4.get_y()+0.4,"%d" % h4, ha="left", va="center", color="black", fontsize=16, fontweight="bold")

plt.show()

plt.pie(ApealClass['Counts'],labels=ApealClass['Course Requested by Appeal'],
        startangle=90,shadow=True,autopct='%1.2f%%')

plt.title('Courses most Appealed')
plt.show()


ApGrY = ApealsKids[ApealsKids['Appeal Granted? Y/N'] == 'Y']
ApGrY['Course Requested by Appeal'] = ApGrY['Course Requested by Appeal'].str.rstrip()
ApGrY1 = ApGrY[['Course Requested by Appeal', 'Final Grade Appealed/ Rejected Course']]

ApGrY1_1 = ApGrY1.groupby(['Course Requested by Appeal','Final Grade Appealed/ Rejected Course'])['Final Grade Appealed/ Rejected Course'].count()
ApGrY1_1 = ApGrY1_1.to_frame()
ApGrY1_1.rename(columns = {'Final Grade Appealed/ Rejected Course': 'Counts'},inplace=True)
ApGrY1_1 = ApGrY1_1.reset_index()

ApBA = ApGrY1_1[ApGrY1_1['Course Requested by Appeal'] == 'Biology Academic']
ApBH = ApGrY1_1[ApGrY1_1['Course Requested by Appeal'] == 'Biology Honors']
ApEH = ApGrY1_1[ApGrY1_1['Course Requested by Appeal'] == 'English 9 Honors']
ApGM = ApGrY1_1[ApGrY1_1['Course Requested by Appeal'] == 'Geometry Honors']

colors = ('orange','brown','cyan','magenta')
colors2 = ('mediumorchid','royalblue','sandybrown','mediumspringgreen')
fig, (px1,px2) = plt.subplots(1,2)
px1.pie(ApBA['Counts'],colors = colors, labels=ApBA['Final Grade Appealed/ Rejected Course'],
        startangle=90,shadow=True,autopct='%1.2f%%')
px2.pie(ApBH['Counts'],colors = colors, labels=ApBH['Final Grade Appealed/ Rejected Course'],
        startangle=90,shadow=True,autopct='%1.2f%%')

px1.title.set_text('Biology Academic')
px2.title.set_text('Biology Honors')

plt.show()

fig2, (px3,px4) = plt.subplots(1,2)
px3.pie(ApEH['Counts'],colors = colors2, labels=ApEH['Final Grade Appealed/ Rejected Course'],
        startangle=90,shadow=True,autopct='%1.2f%%')
px4.pie(ApGM['Counts'],colors = colors2, labels=ApGM['Final Grade Appealed/ Rejected Course'],
        startangle=45,shadow=True,autopct='%1.2f%%')

px3.title.set_text('English 9 Honors')
px4.title.set_text('Geometry Honors')
plt.show()
#########################################################################################################
###############################################################################################################
############################################################################################
ApYM = ApGrY[['Year of Appeal','Grad Cohort','Course Requested by Appeal','10th Grade Course Taken',
             '10th Tracked Up, Down, or Same', '11th Grade Course Taken',
             '11th Tracked up, down, or same?']]
ApYM1 = ApYM.groupby(['Course Requested by Appeal','10th Tracked Up, Down, or Same'])[
    '10th Tracked Up, Down, or Same'].count()
ApYM1 = ApYM1.to_frame()
ApYM1.rename(columns = {'10th Tracked Up, Down, or Same':'Counts'},inplace = True)
ApYM1.reset_index(inplace=True)
ApYM1_1 = ApYM1.groupby(['Course Requested by Appeal'])['Counts'].sum()
ApYM1F = pd.merge(ApYM1,ApYM1_1,on = 'Course Requested by Appeal')
ApYM1F['Percentage'] = ApYM1F['Counts_x'] / ApYM1F['Counts_y']
ApYM1F['Percentage'] = (round(ApYM1F['Percentage'] * 100))
ApYM1FF = ApYM1F[['Course Requested by Appeal', '10th Tracked Up, Down, or Same',
                  'Percentage']]
###############################################################################################
ApYM2 = ApYM.groupby(['Course Requested by Appeal','11th Tracked up, down, or same?'])[
    '11th Tracked up, down, or same?'].count()
ApYM2 = ApYM2.to_frame()
ApYM2.rename(columns = {'11th Tracked up, down, or same?':'Counts'},inplace = True)
ApYM2.reset_index(inplace=True)
ApYM2_2 = ApYM2.groupby(['Course Requested by Appeal'])['Counts'].sum()
ApYM2F = pd.merge(ApYM2,ApYM2_2,on = 'Course Requested by Appeal')
ApYM2F['Percentage'] = ApYM2F['Counts_x'] / ApYM2F['Counts_y']
ApYM2F['Percentage'] = (round(ApYM2F['Percentage']*100) )
ApYM2FF = ApYM2F[['Course Requested by Appeal', '11th Tracked up, down, or same?',
                  'Percentage']]
###########################################################################################
ApYA = ApYM[ApYM['Grad Cohort'] < 2024 ]
ApYA = ApYA[['Course Requested by Appeal','10th Tracked Up, Down, or Same','11th Tracked up, down, or same?']]
ApYA['10thPlus11thTracked'] = ApYA['10th Tracked Up, Down, or Same'] + ' + ' +ApYA['11th Tracked up, down, or same?']
ApYA2 = ApYA.groupby(['Course Requested by Appeal','10thPlus11thTracked'])[
    '10thPlus11thTracked'].count()
ApYA2 = ApYA2.to_frame()
ApYA2.rename(columns = {'10thPlus11thTracked':'Counts'},inplace = True)
ApYA2.reset_index(inplace=True)
ApYA2_2 = ApYA2.groupby(['Course Requested by Appeal'])['Counts'].sum()
ApYA2F = pd.merge(ApYA2,ApYA2_2,on = 'Course Requested by Appeal')
ApYA2F['Percentage'] = ApYA2F['Counts_x'] / ApYA2F['Counts_y']
ApYA2F['Percentage'] = (round(ApYA2F['Percentage']*100) )
ApYA2FF = ApYA2F[['Course Requested by Appeal', '10thPlus11thTracked',
                  'Percentage']]








