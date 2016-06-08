import sklearn.cluster
import sklearn.decomposition
import random
import matplotlib.pyplot as plt

def g(v,s):
    return [ random.gauss(x, s) for x in v ]

def gen(d,n,k):
    boot = [ 0.0 for i in range(d) ]
    centers = [ g(boot, 1.0) for i in range(k) ]
    points = []
    for c in centers:
        for i in range(n):
            points.append(g(c,0.1))
    return points

# print "\n".join(map(str, gen(2,3,3)))

random.seed(0)

d = 100
n = 100
k = 10
data = gen(d, n, k)

pca = sklearn.decomposition.RandomizedPCA(n_components=2, whiten=True, random_state=0)
lowDim = pca.fit_transform(data)

km = sklearn.cluster.KMeans(n_clusters=k, random_state=0)

km.fit(data)
labels = km.labels_

data = lowDim

plt.scatter( [ p[0] for p in data ], [ p[1] for p in data ], c=labels )
plt.show()