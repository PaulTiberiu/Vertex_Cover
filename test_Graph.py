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

print("Sommet avec le degre max: ", Graph.Graph.max_degree(graph))

n = 6
p = 0.6

graph_v4 = Graph.Graph.random_graph(n, p)

print(f'Graphe avec {n} sommets et des aretes creees avec une probabilite {p}\n sommets : {graph_v4.V}\n aretes : {graph_v4.E}')
print(f'La liste après l algo glouton est : {graph_v4.algo_glouton()}')
couverture = graph.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)

