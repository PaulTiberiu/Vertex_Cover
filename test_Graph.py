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
p = 0.1

graph_v4 = Graph.Graph.random_graph(n, p)
print("Graphe avec n sommets, avec des aretes crees avec une probabilite p: ","sommets: ", graph_v4.V, "aretes: ", graph_v4.E)

couverture = graph.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)

print(f'La liste après l algo glouton est : {graph.algo_glouton()}')

# Mesure de Nmax
#graph_v6 = Graph.Graph.random_graph(30000, 0.3) 
# Mon terminal est killed lors de la creation d'un graphe comme ca, je vois pas pourquoi
# Sinon couplage plus rapide dans le cas de sommets
# Je ne peux pas trouver Nmax(sommets) pour couplage car terminal killed quand je cree un graphe avec un grand nombre des sommets

Nmax = 350
graph_v5 = Graph.Graph.random_graph(Nmax, 0.3)

temps_couplage = Graph.Graph.measure_time(graph_v5, "couplage")
print("Temps couplage: ", temps_couplage, " secondes", " pour Nmax(sommets) = ", Nmax)

temps_glouton = Graph.Graph.measure_time(graph_v5, "glouton")
print("Temps glouton: ", temps_glouton, " secondes", " pour Nmax(sommets) = ", Nmax)






