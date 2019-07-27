def main(reply_from_user):
	import write
	import numpy as np    
	#import matplotlib.pyplot as plt   
	import pandas as pd  
	from sklearn.neural_network import MLPClassifier
	from sklearn import preprocessing
	import csv
	import datetime
	date_temp = str(datetime.datetime.now().date())
	date=""
	date=date_temp[8:]+"-"+date_temp[5:7]+"-"+date_temp[0:4]
	data=pd.read_csv('final_dataset.csv')
	data1=data.iloc[:,[1,2,3,4,5,6,7,8,9,10]]

	dataset=[]
	y1=[]
	y2=[]

	for row in data1.iterrows():
		index, df = row
		dataset.append(df.tolist())


	y=data.iloc[:,[0]]
	print(y)

	for row in y.iterrows():
		index, df = row
		y1.append(df.tolist())


	le = preprocessing.LabelEncoder()
	y = y.apply(le.fit_transform)

	for row in y.iterrows():
		index, df = row
		y2.append(df.tolist())


	k=1
	arr=[]
	x=[]
	temp=[]
	x_train=[]
	x_test=[]
	disease=[]

	# reply_from_user=[]
	# questions_list=["Do you experience coughing? 0.No 1.Yes","Do you experience chest pain?   0.No 1.Yes","Do you experience Weight Loss?   0.No 1.Yes","Do you experience Fatigue?   0.No 1.Yes","Do you have Fever?   0.No 1.Yes 2.Severe","Do you experience Chills?   0.No 1.Yes","Do you experience Loss of Appetite?   0.No 1.Yes","Do you experience Vomiting?   0.No 1.Yes","Do you experience Muscle Pain?   0.No 1.Yes","Do you experience Sore Throat?  0.No 1.Yes"]

	# for i in range(len(questions_list)):
	# 	print(questions_list[i])
	# 	user_answer=input()
	# 	reply_from_user.append(user_answer)

	def disease_prediction(k):
		for i in range(0,len(dataset)): 
			for j in range(0,k):
				arr.insert(j,dataset[i][j])
			temp=arr.copy()    
			x.insert(i,temp)
			arr.clear()


		if(k==1):
		#print("Do you experience coughing? \n 0.No\n 1.Yes\n")
		# reply="Do you experience coughing? \n 0.No\n 1.Yes"
		# chat.print_bot_reply(reply)
		# print(reply)
		# ip=input()
			ip=reply_from_user[k-1]
			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==2):
		# reply="Do you experience chest pain?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==3):
		# reply="Do you experience Weight Loss?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()
			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==4):
		# reply="Do you experience Fatigue?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==5):
		# reply="Do you have Fever?  \n 0.No\n 1.Yes\n 2.Severe"
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="mild"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="severe"):
				ip=2 
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(1)
				return k
		#continue   
		if(k==6):
		# reply="Do you experience Chills?  \n 0.No\n 1.Yes"   
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k

		#continue
		if(k==7):
		# reply="Do you experience Loss of Appetite?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k

		#continue
		if(k==8):
		# reply="Do you experience Vomiting?  \n 0.No\n 1.Yes" 
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==9):
		# reply="Do you experience Muscle Pain?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()
			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		if(k==10):
		# reply="Do you experience Sore Throat?  \n 0.No\n 1.Yes"
		# print(reply)
		# ip=input()

			ip=reply_from_user[k-1]

			if(ip=="yes"):
				ip=1
			if(ip=="no"):
				ip=0
			if(ip=="not sure"):
				k=k+1
				x.clear()
				x_test.append(0.5)
				return k
		#continue
		x_train=x.copy()
		x.clear()
		x_train=np.array(x_train)  
		mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000)  
		mlp.fit(x_train,y)   
		ip=int(ip)
		x_test.append(ip)
		y_pred=mlp.predict([x_test])
		print("Possible Diagnosis",end=" ")
		disease.append(y_pred)
		print(y1[y2.index(disease[len(disease)-1])])
		k=k+1
		return k
	for i in range(10):
		print(i)
		k=disease_prediction(k)
	print("Final Diagnosis",end=" ")
	print(y1[y2.index(disease[len(disease)-1])])

	diagnosed_disease=y1[y2.index(disease[len(disease)-1])]
	write.write_to_csv(diagnosed_disease[0],date)
	return diagnosed_disease