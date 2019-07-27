import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# Values of each group
#storing false bottom in d0
d0 = [0,0,0,0,0,0,0]
#d1 is the first disease and the list is count of disease date wise
import csv

file_contents=[]

with open('disease_count.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for disease in readCSV:
        file_contents.append(disease)

Tuberculosis = file_contents[1][1:]
Tuberculosis = [int(x) for x in Tuberculosis]
Malaria = file_contents[2][1:]
Malaria = [int(x) for x in Malaria]
AIDS = file_contents[3][1:]
AIDS = [int(x) for x in AIDS]
Measles = file_contents[4][1:]
Measles = [int(x) for x in Measles]
Dengue = file_contents[5][1:]
Dengue = [int(x) for x in Dengue]
Tonsilitis = file_contents[6][1:]
Tonsilitis = [int(x) for x in Tonsilitis]
Typhoid = file_contents[7][1:]
Typhoid = [int(x) for x in Typhoid]
Jaundice = file_contents[8][1:]
Jaundice = [int(x) for x in Jaundice]
Leukemia = file_contents[9][1:]
Leukemia = [int(x) for x in Leukemia]
Amoebiasis = file_contents[10][1:]
Amoebiasis = [int(x) for x in Amoebiasis]

diseases = [d0,Tuberculosis,Malaria,AIDS,
            Measles,Dengue,Tonsilitis,Typhoid,
            Jaundice,Leukemia,Amoebiasis]

rc('font', weight='bold')

# Heights of bars1 + bars2
#bars = np.add(bars1, bars2).tolist()
bottom_bars = []
bottom_Tuberculosis = d0
bottom_bars.append(bottom_Tuberculosis)
bars = np.add(bottom_Tuberculosis,bottom_Tuberculosis)
for i in range(1,11):
    bars = np.add(bars,diseases[i]).tolist()
    bottom_bars.append(bars)
    
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6]

# Names of group and bar width
names = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
barWidth = 0.45

# Create brown bars
plt.bar(r, Tuberculosis, bottom=bottom_bars[0],edgecolor='white', width=barWidth,color='blue')
# Create green bars (middle), on top of the firs ones
plt.bar(r, Malaria, bottom=bottom_bars[1],edgecolor='white', width=barWidth,color='red')
# Create green bars (top)
plt.bar(r, AIDS, bottom=bottom_bars[2],edgecolor='white', width=barWidth,color='green')
plt.bar(r, Measles, bottom=bottom_bars[3],edgecolor='white', width=barWidth,color='yellow')
plt.bar(r, Dengue, bottom=bottom_bars[4],edgecolor='white', width=barWidth,color='black')
plt.bar(r, Tonsilitis, bottom=bottom_bars[5],edgecolor='white', width=barWidth,color='violet')
plt.bar(r, Typhoid, bottom=bottom_bars[6],edgecolor='white', width=barWidth,color='brown')
plt.bar(r, Jaundice, bottom=bottom_bars[7],edgecolor='white', width=barWidth,color='pink')
plt.bar(r, Leukemia, bottom=bottom_bars[8],edgecolor='white', width=barWidth,color='gold')
plt.bar(r, Amoebiasis, bottom=bottom_bars[9],edgecolor='white', width=barWidth,color='purple')

# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")

# Show graphic
plt.show()


#pie char analysis for a specific date

# Data to plot
dataset=pd.read_csv('disease_count.csv');
print(dataset)
date='29-03-2019'
datee=dataset.columns
for i in range (0,len(datee)):
    if(datee[i]==date):
        index=i
        break;
print(index)        
labels = dataset.iloc[:,0]
print(labels)
sizes = dataset.iloc[:,index]
print(sizes)
 
# Plot
plt.pie(sizes,labels=labels,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

