#Write into File
import names
import csv
import random as rand

w=100
h=3

activity = [[rand.uniform(0,5) for x in range(h)] for y in range(w)]
attendance = [[rand.uniform(20,100) for x in range(h)] for y in range(w)]
clubs = [[rand.uniform(0,5) for x in range(h)] for y in range(w)]
CGPA=[[rand.uniform(3,10) for x in range(h)] for y in range(w)]
regno=[]
name=[]
for i in range (100):
	Nam=names.get_full_name()
	name.append(Nam)
	#name.append(' ')
	#name.append(' ')

for i in range(100):
	reg=int(rand.uniform(1000,9999))
	regno.append(reg)
	#regno.append(' ')
	#regno.append(' ')


rows=zip(name,regno,CGPA,attendance,activity,clubs)
with open('Raw_Data.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in rows:
    	writer.writerow(val)


   
        
