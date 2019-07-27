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