
import networkit as nk
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
def SCollection(G,i):#s olonlogiig olno i heden shirhegiig zaana
	S=[]
	bc=nk.centrality.Betweenness(G)	
	bc.run()
	scores=bc.scores()
	for i in range(i):#s_too udaa dawtana
		maxelement=max(scores)
		maxElementIndex=scores.index(maxelement)
		S.append(maxElementIndex)
		scores[maxElementIndex]=-1
	return S
def H(G):
	com=nk.components.ConnectedComponents(G)
	com.run()
	a=com.getComponents()
	h=0
	for i in range(len(a)):
		h=h+len(a[i])*(len(a[i])-1)/2
	return h
for j in range(len(file)):
	print(file[j])
	print(k[j])		
	G=readGraph(file[j])
	S=SCollection(G,k[j])
	for i in range(len(S)):
		G.removeNode(S[i])
	print(H(G))

