import pandas as pd
disease = 'Tuberculosis'
disease_details = pd.read_csv('diseases_details.csv')
x = list(disease_details.iloc[:,0])
index = x.index(disease)
about = disease_details.iloc[:,1][index]
spread = disease_details.iloc[:,2][index]
treatment = disease_details.iloc[:,3][index]
doctors = disease_details.iloc[:,4][index]
