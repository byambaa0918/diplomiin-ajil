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
k=[50,75,100,150
,50,80,140,200,50,110,150,200,70,125,200,265]
gs=[]
def readGraph(filename):
	f=open(filename)
	n=f.readline()
	G=nk.Graph(int(n))
	gs.append(int(n))
	for line in f.readlines():
		arr=line.split(": ")
		edge=arr[1].split(" ")
		edge.pop()#мөр бүрийн төгсгөлийн \n-ийг хасна
		for i in edge:
			G.addEdge(int(arr[0]),int(i))
	f.close()
	return G		
def convert(u, v, wei, edgeId):#nk-аас үүссэн графын ирмэгүүдээр гүйж nx-ийн жинтэй графыг үүсгэнэ.
	B.add_edge(u,v)
	aa=maxValue-scores[u]
	bb=maxValue-scores[v]
	weight=maxValue-((scores[u]+scores[v])/2)        #(aa+bb)/2
#	print("wight",weight,weight1)
	B.edges[u,v]['weight'] = weight	
def maxbc(bc):
	maxe=-1
	index=-1
	for y in range(gs[0]):#хамгийн их bc-тэй оройг олно!!!!!!!!!!!!!!!!
		try:
			if(maxe<bc[y]):
				maxe=bc[y]
				index=y		
		except KeyError:#тухайн компонентод y орой байхгүй үед үүснэ
			continue		
	return index	
def H(G):
	com=nk.components.ConnectedComponents(G)
	com.run()
	a=com.getComponents()
	h=0
	for i in range(len(a)):
		h=h+len(a[i])*(len(a[i])-1)/2
	return h	
def findMinH(G,S):# G графаас S олонлогын элементүүдийн хувьд Н олж array буцаана  
	minH=[]#
	for x in range(len(S)):
		G1=readGraph(file[j])
		for y in range(len(S)):#х орой хасаагүй үед
			if x!=y:			
				G1.removeNode(S[y])	
		minH.append(H(G1)-H(G))
	return minH	
def minPos(arr):
	minelement=numpy.min(arr)
	minElementIndex=arr.index(minelement)
	return minElementIndex					
scores=[]   
B= nx.Graph()
S=[]
maxValue=0
for j in range(len(file)):#len(file)	
	S.clear()
	gs.clear()	
	G=readGraph(file[j])#
	G2=nk.Graph(G)
	while True:
		largeComponent=nk.components.ConnectedComponents.extractLargestConnectedComponent(G)		
		bc=nk.centrality.Betweenness(largeComponent)#хамгийн том компонентийн bc
		bc.run()
		scores=bc.scores()
		B.clear()#nx-ийн жинтэй граф convert функцээр үүснэ
		maxValue=max(scores)
		largeComponent.forEdges(convert)
		size=largeComponent.numberOfNodes()
		bcw=nx.betweenness_centrality(B,weight='weight')#жинтэй графын bc
		for x in range(math.floor(math.sqrt(size))):#bc dotoroos yzguur n shirheg oroig hasna			
			maxbcindex=maxbc(bcw)#bc hamgiin ih oroi butsaana					
			S.append(maxbcindex)#хасах оройн дугаарыг S рүү нэмнэ
			bcw[maxbcindex]=-1
			G.removeNode(maxbcindex)
			B.remove_node(maxbcindex)#хамгийн их bc-тэй оройг хасна
		if(len(S)>=k[j]):
			break					
	for d in range(len(S)-k[j]):
		G3=nk.Graph(G2)
		arr=findMinH(G,S)
		pos=minPos(arr)
		S.pop(pos)
		for a in range(len(S)):		
			G3.removeNode(S[a])
		G=G3
	print(file[j],H(G))