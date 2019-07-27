def write_to_csv(diagnosed_disease,date):
    
    import csv
    import datetime
    date_temp = str(datetime.datetime.now().date())
    date=""
    date=date_temp[8:]+"-"+date_temp[5:7]+"-"+date_temp[0:4]
    file_contents=[]
    with open('disease_count.csv') as csvfile:
    	readCSV = csv.reader(csvfile, delimiter=',')
    	for row in readCSV:
    		file_contents.append(row)
    column_index=file_contents[0].index(date)
    row_index=-1
    
    for row in file_contents:
    	if row[0] == diagnosed_disease:
    		row_index=file_contents.index(row)
    		break
    temp=int(file_contents[row_index][column_index])
    temp+=1
    
    file_contents[row_index][column_index]=str(temp)
    row = file_contents[row_index]
    
    with open('disease_count.csv', 'r') as readFile:
    	reader = csv.reader(readFile)
    	lines = list(reader)
    	lines[row_index] = row
    with open('disease_count.csv', 'w', newline='') as writeFile:
    	writer = csv.writer(writeFile)
    	writer.writerows(lines)
    readFile.close()
    writeFile.close()