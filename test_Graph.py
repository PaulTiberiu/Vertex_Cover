import Graph

vertices = [0, 3, 6, 8]
adjacents = {0 : {6, 3}, 3 : {0}, 6 : {8, 0}, 8 : {6}}
graph = Graph.Graph(vertices, adjacents)
print("Graphe: ")
print("Sommets:", graph.V)
print("Aretes:", graph.E)

graph_v2 = Graph.Graph.remove_vertex(graph, 3)

print("Graphe_v2: ")
print("Sommets:", graph_v2.V)
print("Aretes:", graph_v2.E)

vertex_remove = {3,6}
graph_v3 = Graph.Graph.remove_many_vertex(graph, vertex_remove)

print("Graphe_v3: ")
print("Sommets:", graph_v3.V)
print("Aretes:", graph_v3.E)

dico = graph.vertex_degrees()
print("Degrees des sommets: ", dico)

print("Degree max d'un sommet du Graph: ", Graph.Graph.max_degree(graph))

n = 4
p = 0.5

graph_v4 = Graph.random_graph(n, p) # fonctionne pas
print("Graphe avec 4 sommets, avec des aretes cree avec une probabilite 0.5", graph_v4)
