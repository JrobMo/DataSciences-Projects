""" 
a1_Robbins_000371194.py
I, Jacob Robbins, student number 000371194, certify that this material is my original work.
No other person's work has been used withoutdue acknowledgment and I have not made my work
available to anyone else.
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patheffects

color_chart =  ['#FFFF00','#7CFC00', '#C4C3D0', '#BF94E4', '#FDDDE6' , '#F4C430', '#00ffff', '#f0f8ff', '#abcdef']
labels_chart=['','CSS', 'C#' ,'JavaScript','HTML','Visual Studio','Python','AngularJS','TypeScript','SQL','Docker','Azure','Zoho','WordPress','ReactJS','Java','.NET','PHP','Nodejs','Jira','Drupal','ASP.NET']

# Read data from CSV file
df = pd.read_csv("a2_2024f_coop_tech.csv", header=None, names=['Technology'])

# Convert data to lowercase
df['Technology'] = df['Technology'].str.lower()

# Count occurrences of each technology
technology_counts = df['Technology'].value_counts()

# Identify technologies occurring only once
single_occurrence = technology_counts[technology_counts == 1]

# Replace single occurrence technologies with 'other'
df['Technology'] = df['Technology'].apply(lambda x: 'other' if x in single_occurrence else x)

explode_spc=(0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)

my_dpi = 100
#function for autopct 
def pct2(pct) :
    if pct > 2.9:
        return "{:.0f}%".format(pct)

# Plot pie chart
plt.figure(figsize=(8,6), dpi=100)
ax1 = df['Technology'].value_counts().plot.pie(explode=explode_spc, autopct=lambda pct: pct2(pct),pctdistance=0.85, counterclock=False, startangle=143,rotatelabels=30, labels=labels_chart, colors=color_chart)
plt.suptitle('Technologies Used by COOPs in Fall 2021',weight='bold', fontsize=20, y=0.93).set_path_effects([patheffects.withSimplePatchShadow()])
plt.title('Other \n\n\n\n\n\n Many Specialized Technologies \n Were Reported Only Once', loc='center',fontsize=10, y=0.7)
plt.ylabel('')
plt.show()