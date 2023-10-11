import Graph
import time

vertices = [0, 3, 6, 8]
adjacents = {0 : {6, 3}, 3 : {0}, 6 : {8, 0}, 8 : {6}}
graph = Graph.Graph(vertices, adjacents)
print("Graphe: ")
print("Sommets:", graph.V)
print("Aretes:", graph.E)
print("")

graph_v2 = Graph.Graph.remove_vertex(graph, 3)

print("Graphe_v2: ")
print("Sommets:", graph_v2.V)
print("Aretes:", graph_v2.E)
print("")

vertex_remove = {3,6}
graph_v3 = Graph.Graph.remove_many_vertex(graph, vertex_remove)

print("Graphe_v3: ")
print("Sommets:", graph_v3.V)
print("Aretes:", graph_v3.E)
print("")

dico = graph.vertex_degrees()
print("Degrees des sommets: ", dico)
print("")

print("Degree max d'un sommet du Graph: ", Graph.Graph.max_degree(graph))
print("")

n = 4
p = 0.1

graph_v4 = Graph.Graph.random_graph(n, p)
print("Graphe avec n sommets, avec des aretes crees avec une probabilite p: ","sommets: ", graph_v4.V, "aretes: ", graph_v4.E)
print("")

couverture = graph.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)
print("")

print(f'La liste après l algo glouton est : {graph.algo_glouton()}')
print("")

filename = "graph.txt"
graph_from_file = Graph.Graph.create_graph_from_file(filename)
print("Graphe depuis fichier: ")
print("Sommets:", graph_from_file.V)
print("Aretes:", graph_from_file.E)
print("")


# Mesure de Nmax_vertex
# Couplage plus rapide dans le cas de sommets
# random_graph prends beaucoup de temps lorsqu'on augmente les nombres des sommets (50.000 par exemple)

"""
Nmax_vertex_couplage = 10000
graph_v6 = Graph.Graph.random_graph(Nmax_vertex_couplage, 0.3) # ca prend beaucoup plus de temps que l'execution de l'algo couplage
temps_couplage = Graph.Graph.measure_time(graph_v6, "couplage")
print("Temps couplage: ", temps_couplage, " secondes", " pour Nmax(sommets) = ", Nmax_vertex_couplage)
print("")
# Temps couplage:  0.02478313446044922  secondes  pour Nmax(sommets) =  10000, si on augmente le nombre de sommets ca prends trop de temps pour generer un graph aleatoire
"""
"""
Nmax_vertex_glouton = 350
graph_v5 = Graph.Graph.random_graph(Nmax_vertex_glouton, 0.3)
temps_glouton = Graph.Graph.measure_time(graph_v5, "glouton")
print("Temps glouton: ", temps_glouton, " secondes", " pour Nmax(sommets) = ", Nmax_vertex_glouton)
print("")
# Temps glouton:  2.0698513984680176  secondes  pour Nmax(sommets) =  350
"""

# Mesure Nmax_proba
# (proba 0.3 a 0.99 avec 350 sommets augmente de 3 sec a 9.8 sec pour glouton)
"""
Nmax_proba_glouton = 0.99
graph_v7 = Graph.Graph.random_graph(100, Nmax_proba_glouton)
temps_couplage_proba_glouton = Graph.Graph.measure_time(graph_v7, "couplage")
print("Temps couplage: ", temps_couplage_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)

temps_glouton_proba = Graph.Graph.measure_time(graph_v7, "glouton")
print("Temps glouton: ", temps_glouton_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)
"""

# Courbes temps / instance

Nmax_vertex_glouton = 350
Graph.Graph.measure_execution_time_vertex("glouton", 10, Nmax_vertex_glouton, 0.3) # Deja teste, capture ecran vm
#Graph.Graph.measure_execution_time_vertex("couplage", 10, Nmax_vertex_glouton, 0.3) # Deja teste, capture ecran vm

#Graph.Graph.measure_execution_time_proba("glouton", 10, 50, Nmax_proba)     a tester
#Graph.Graph.measure_execution_time_vertex("couplage", 10, 50, Nmax_proba)   a tester
