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

filename = "graph.txt"
graph_from_file = Graph.Graph.create_graph_from_file(filename)
print("Graphe depuis fichier: ")
print("Sommets:", graph_from_file.V)
print("Aretes:", graph_from_file.E)


# Mesure de Nmax_vertex
#graph_v6 = Graph.Graph.random_graph(30000, 0.3) 
# Mon terminal est killed lors de la creation d'un graphe comme ca, je vois pas pourquoi
# Sinon couplage plus rapide dans le cas de sommets
# Je ne peux pas trouver Nmax(sommets) pour couplage car terminal killed quand je cree un graphe avec un grand nombre des sommets

"""
Nmax_vertex = 350
graph_v5 = Graph.Graph.random_graph(Nmax_vertex, 0.3)

temps_couplage = Graph.Graph.measure_time(graph_v5, "couplage")
print("Temps couplage: ", temps_couplage, " secondes", " pour Nmax(sommets) = ", Nmax_vertex)

temps_glouton = Graph.Graph.measure_time(graph_v5, "glouton")
print("Temps glouton: ", temps_glouton, " secondes", " pour Nmax(sommets) = ", Nmax_vertex)
"""

# Il faut aussi mesurer Nmax_proba, mais ca depend sourtout du nombre de sommets ... a voir (proba 0.3 a 0.99 avec 350 sommets augmente de 3 sec a 9.8 sec pour glouton)
Nmax_proba = 0.99
graph_v7 = Graph.Graph.random_graph(350, Nmax_proba)

temps_couplage_proba = Graph.Graph.measure_time(graph_v7, "couplage")
print("Temps couplage: ", temps_couplage_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)

temps_glouton_proba = Graph.Graph.measure_time(graph_v7, "glouton")
print("Temps glouton: ", temps_glouton_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)

# Courbes temps / instance

#Graph.Graph.measure_execution_time_vertex("glouton", 10, Nmax_vertex, 0.3) # Deja teste, capture ecran vm
#Graph.Graph.measure_execution_time_vertex("couplage", 10, Nmax_vertex, 0.3) # Deja teste, capture ecran vm

#Graph.Graph.measure_execution_time_proba("glouton", 10, 50, Nmax_proba)     a tester
#Graph.Graph.measure_execution_time_vertex("couplage", 10, 50, Nmax_proba)   a tester
