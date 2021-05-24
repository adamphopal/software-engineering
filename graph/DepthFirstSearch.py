#output for this code: 
#A['B', 'E']  1/20
#B['A', 'F']  2/19
#C['G']  5/6
#D['E', 'H']  12/15
#E['A', 'D', 'H']  13/14
#F['B', 'G', 'I', 'J']  3/18
#G['C', 'F', 'J']  4/9
#H['D', 'E', 'I']  11/16
#I['F', 'H']  10/17
#['F', 'G']  7/8
#output for Discovery time for dfs? a list of vertex's, sorted by increasing discover time, it will be based on the discovery time for each vertex, starting with A 1/20.
#Discovery time for this program: A,B,F,G,C,J,I,H,D,E

#toplogical sort using finish decreasing times? sort with the hiighest finish times, starting with A 1/20
#toplogical sort for this program: A,B,F,I,H,D,E,G,J,C

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			# my YouTube video shows a silly for loop here, but this is a much faster way to do it
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return True
		else:
			return False
	

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.dfs(a)
g.print_graph()
