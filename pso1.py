#PSO Implementation
import numpy
import random as rand
import csv
from kmeans123 import MEANS

def calculateScore(a,impa,att,impatt,c,impc):

	acti=a*impa
	atti=(att/20)*impatt
	clu=c*impc
	#Normalize the data
	a=acti+atti+clu
	

	return a 



def normalization(scale,gbest,data):

	a=(data/gbest)*scale

	return a


def calculateDistance(number,centroid):
	pbest=0
	for i in range(len(centroid)):
		best=abs(centroid[i]-number)
		if(best>pbest):
			pbest=best
			pos=i
	#print "returning"+ str(pos)
	return pos

w=100
h=3
clusters=input("Clusters? \n ")
ImportanceActivity=input("importance of Activities (scale of 1-10) \n")
ImportanceAttendance=input("Importance of Attendance (Scale of 1-10) \n ")
ImportanceClubs=input("Importance of Clubs (Scale of 1-10) ? \n " )



activity = [[rand.uniform(0,5) for x in range(h)] for y in range(w)]
attendance = [[rand.uniform(20,100) for x in range(h)] for y in range(w)]
clubs = [[rand.uniform(0,5) for x in range(h)] for y in range(w)]
CGPA = [rand.uniform(3,10) for x in range(w)]
#CGPAFile1=[[[0 for x in range(h)] for y in range(w)]]
CGPAFile1=[]
CGPAFile=[]

TotalActivity=[]
TotalAttendance=[]
TotalClubs=[]
TotalCGPA=[]

with open ('Raw_Data.csv','rb') as csvfile:
	# get number of columns
    for line in csvfile.readlines():
        array = line.split(',')
        CGPA1 = array[2]
        TotalCGPA.append(CGPA)       
        Attendance=array[3]
        TotalAttendance.append(Attendance.split(','))
        Activity=array[4]
        TotalActivity.append(Activity.split(','))
        Clubs=array[5]
        TotalClubs.append(Clubs.split(','))

'''
    num_columns = len(array)
    csvfile.seek(0)

    reader = csv.reader(csvfile, delimiter=' ')
    included_cols = [1, 2,3]

    for row in reader:
    	content = list(row[0].split('\n'))# for i in included_cols)
    	for i in content:
        	print i
        	print "Done1"



AttendanceData=[]
k=0
for i in TotalAttendance:
	print i
	AD=i.split('|')
	AttendanceData[k].append(AD)
	k+=1

print AttendanceData[1][1]
'''


print "\n Activity  \n"
print TotalActivity
print "\n Attendance \n"
print TotalAttendance
print "\n Clubs  \n"
print TotalClubs
gbest=0

Data=w
Years=h
pbest1=[0 for i in range(Data)]
pbest2=[]
for i in range (Data):
	
	for j in range(Years):
		maxtemp=calculateScore(activity[i][j],ImportanceActivity,attendance[i][j],ImportanceAttendance,clubs[i][j],ImportanceClubs)
		if maxtemp>pbest1[i]:
			pbest1[i]=maxtemp
			if (pbest1[i]>gbest):
				gbest=pbest1[i]

print "Pbests are " + str(pbest1)
print "Gbest is " + str(gbest)

scale=10
scale = input(" Enter the normalization Scale default=10 \n ")
ngbest=0
ndata=[]
print ("Normalized Data ")
for a in pbest1:
	ndata=normalization(scale,gbest,a)
	if ndata>ngbest:
		ngbest=ndata
	pbest2.append(ndata)
print pbest2

print "Normalized Gbest = " + str(ngbest)

#Clustering

centroid=[0 for i in range(clusters)]

noOfPoints=clusters
x=noOfPoints
initial=(scale/x)
temp1=initial
for i in range(noOfPoints):
	centroid[i]=temp1	
	temp1+=initial

print ("First set of Centroids are:- ")
print centroid	
clusterOf=[0.0 for i in range (Data)]

for i in range(Data):
	clusterOf[i]=calculateDistance(pbest2[i],centroid)
	print str(pbest2[i]) + " Currently Belongs to Centroid " + str(clusterOf[i]) + " That is " + str(centroid[clusterOf[i]])


print str(centroid[clusterOf[1]]) 
fo=open("Data.txt",'w')
for i in range(1,len(CGPA)):
	#print CGPA[i]
	item=str(CGPA[i])+' '+str(pbest2[i])+'\n'
	fo.write(item)



fo.close()
a=raw_input("Start Kmeans? ")

MEANS()