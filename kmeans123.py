import math
import plotly as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot


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
	print "OPENED DATA"

	data=[]
	for line in fo:
	    data.append([float(x) for x in line.split()])

	k1= min(data)
	k2= max(data)
	Cluster1.append(k1)
	Cluster2.append(k2)

	print data
	data.remove(k1)
	data.remove(k2)

	assign(data,k1,k2)

	k1=calMean(Cluster1)
	k2=calMean(Cluster2)

	while (check(data,k1,k2)):
		print ''

	print " \n Data in Cluster 1 Are : - \n "
	print Cluster1
	print " \n 	Data in Cluster 2 Are : - \n "
	print Cluster2


	def oneD(Cluster,n):

		m=list()
		for i in Cluster:
			m.append(i[n])

		return m

	x0=oneD(Cluster1,0)
	y0=oneD(Cluster1,1)
	x1=oneD(Cluster2,0)
	y1=oneD(Cluster2,1)

	



		#plotClusters(Cluster1)

		
	def plotClusters():

		trace0 = go.Scatter(
		x=x0,
		y=y0,
		mode='markers',
		)
		trace1 = go.Scatter(
		x=x1,
		y=y1,
		mode='markers'
		)

		py.offline.plot({
			"data": [trace0,trace1],
		"layout": go.Layout(
		title="Student Distribution",
		shapes=[
		    {
		        'type': 'circle',
		        'xref': 'x',
		        'yref': 'y',
		        'x0': min(x0),
		        'y0': min(y0),
		        'x1': max(x0),
		        'y1': max(y0),
		        'opacity': 0.2,
		        'fillcolor': 'blue',
		        'line': {
		            'color': 'blue',
		        },
		    },
		    {
		        'type': 'circle',
		        'xref': 'x',
		        'yref': 'y',
		        'x0': min(x1),
		        'y0': min(y1),
		        'x1': max(x1),
		        'y1': max(y1),
		        'opacity': 0.2,
		        'fillcolor': 'orange',
		        'line': {
		            'color': 'orange',
		        },
		    }],
		     height= 600,
		width= 600,
		showlegend=False,

		)
		})


	plotClusters()

#		print "Called1"
   