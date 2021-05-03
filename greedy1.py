import networkit as nk
import math 
import numpy
file=[	
	"BarabasiAlbert_n500m1.txt",
	"BarabasiAlbert_n1000m1.txt",
	"BarabasiAlbert_n2500m1.txt",
	"BarabasiAlbert_n5000m1.txt",
	"ErdosRenyi_n250.txt",
	"ErdosRenyi_n500.txt",
	"ErdosRenyi_n1000.txt",
	"ErdosRenyi_n2500.txt",
	"ForestFire_n250.txt",
	"ForestFire_n500.txt",
	"ForestFire_n1000.txt",
	"ForestFire_n2000.txt",
	"WattsStrogatz_n250.txt",
	"WattsStrogatz_n500.txt",
	"WattsStrogatz_n1000.txt",
	"WattsStrogatz_n1500.txt"]
k=[50,75,100,150,50,80,140,200,50,110,150,200,70,125,200,265]
def H(G):
	com=nk.components.ConnectedComponents(G)
	com.run()
	a=com.getComponents()
	h=0
	for i in range(len(a)):
		h=h+len(a[i])*(len(a[i])-1)/2
	return h
def readGraph(filename):
	f=open(filename)
	n=f.readline()
	G=nk.Graph(int(n))
	for line in f.readlines():
		arr=line.split(": ")
		edge=arr[1].split(" ")
		edge.pop()#мөр бүрийн төгсгөлийн \n-ийг хасна
		for i in edge:
			#print(arr[0]+"a "+i)
			G.addEdge(int(arr[0]),int(i))
	return G
def cover(u,v,wei,edgeid):
#	print(u)
	aa=False
	for i in range(len(S)):
		if int(S[i])==u or int(S[i]==v):
			aa=True
			break
	if(aa==False):			
		S.append(u)
def minPos(arr):
	minelement=numpy.min(arr)
	minElementIndex=arr.index(minelement)
	return minElementIndex	
def findMinH(G,S):# G графаас S олонлогын элементүүдийн хувьд Н олж array буцаана  ирмэг
	minH=[]#
	for x in range(len(S)):
		G1=nk.Graph(G)
		G2=nk.Graph(G)
#		print("H=",H(G))
		for y in range(len(S)):#х орой хасаагүй үед
			G1.removeNode(y)
			if x!=y:		
				G2.removeNode(S[y])	
		minH.append(H(G2)-H(G1))
	return minH		
S=[]				
for j in range(1):#len(file)
	j=3
	S.clear()	
	G=readGraph(file[j])	
	G1=nk.Graph(G)
	G.forEdges(cover)
	#S
	for d in range(len(S)-k[j]):
		arr=findMinH(G,S)
		print(k[j],len(S))
		pos=minPos(arr)
		S.pop(pos)
	for i in range(len(S)):
		G1.removeNode(S[i])
	print(file[j],G1,H(G1),len(S))	
