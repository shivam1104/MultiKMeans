import math


def MEANS():
	Cluster1=[]
	Cluster2=[]

	def euclideanDist(X,k):
		return math.sqrt(math.pow((k[0]-X[0]),2)+math.pow((k[1]-X[1]),2))

	def calMean(Cluster):
		x=0
		y=0
		for i in Cluster:
			x=x+i[0]
		for i in Cluster:
			y=y+i[1]	

		X=x/len(Cluster)
		Y=y/len(Cluster)

		mean=[X,Y]
		return mean


	def assign(data,k1,k2):
		for i in data:
			d1=euclideanDist(i,k1)
			d2=euclideanDist(i,k2)

			if d1<d2:
				Cluster1.append(i)
				k1=calMean(Cluster1)
			else:
				Cluster2.append(i)
				k2=calMean(Cluster2)
		
	def check(data,k1,k2):

		flag=False

		for i in data:
			d1=euclideanDist(i,k1)
			d2=euclideanDist(i,k2)

			if d1<d2:
				if i in Cluster2:
					Cluster2.remove(i)
					Cluster1.append(i)
					flag=True
			else:
				if i in Cluster1:
					Cluster1.remove(i)
					Cluster2.append(i)
					flag=True

		return flag

	fo=open("data.txt","r")

	data=[]
	for line in fo:
	    data.append([float(x) for x in line.split()])

	k1= min(data)
	k2= max(data)
	Cluster1.append(k1)
	Cluster2.append(k2)
	data.remove(k1)
	data.remove(k2)

	assign(data,k1,k2)

	k1=calMean(Cluster1)
	k2=calMean(Cluster2)

	while (check(data,k1,k2)):
		print ''

	print "Data in Cluster 1 Are : - \n "
	print Cluster1
	print "Data in Cluster 2 Are : - \n "
	print Cluster2
