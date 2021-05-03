import networkit as nk
import networkx as nx
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
node=[500,1000,2500,5000,250,500,1000,2500,250,500,1000,2000,250,500,1000,1500]
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
#	print("n=",n)
	G=nk.Graph(int(n))
	for line in f.readlines():
		arr=line.split(": ")
		edge=arr[1].split(" ")
		edge.pop()#мөр бүрийн төгсгөлийн \n-ийг хасна
		for i in edge:
			G.addEdge(int(arr[0]),int(i))
	f.close()
	return G
maxH=[]
for j in range(1):#len(file)	
	print(file[15])
	j=15
	S=[]
	G=readGraph(file[j])
	Gg=nk.Graph(G)
	print("hh=",H(G),G)
#	print("nodeeee",node[j])
	while len(S)<k[j]:
		maxH=-1
		maxHPos=-1
		for i in range(node[j]):		
			G1=nk.Graph(G)
			if G1.hasNode(i):		
				h1=H(G1)
				G1.removeNode(i)
				h2=H(G1)
				myh=h1-h2
#				print(myh,"  aaaaa")
				if maxH<myh:
#					print(h1-h2)
					maxH=myh
					maxHPos=i
#					print(i,"     ii")
#		print(maxH,maxHPos,"--------haslaa",len(S))				
		G.removeNode(maxHPos)	
		S.append(maxHPos)
	print(file[j],G,H(G),len(S))