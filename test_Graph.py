import Graph
import numpy as np
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

#print(f'La liste après l algo glouton est : {graph.algo_glouton()}')
#print("")

filename = "graph.txt"
graph_from_file = Graph.Graph.create_graph_from_file(filename)
print("Graphe depuis fichier: ")
print("Sommets:", graph_from_file.V)
print("Aretes:", graph_from_file.E)
print("")
couverture = graph_from_file.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)
print("")

# Test branch and bound sans bornes
solution = Graph.Graph.branch_simple(graph_from_file)
print("Solution du branchement simple: ", solution)
print("")

solution1 = Graph.Graph.branch_and_bound(graph_from_file)
print("Solution de branch and bound: ", solution1)
print("")

solution2 = Graph.Graph.improved_branch_and_bound(graph_from_file)
print("Solution de branch and bound ameliore: ", solution2)
print("") # A FAIRE LES TESTS __________________________________________________________________________________________________

solution3 = Graph.Graph.improved_branch_and_bound_degmax(graph_from_file)
print("Solution de branch and bound ameliore en prenant le degree max de u: ", solution3)
print("") # A FAIRE LES TESTS __________________________________________________________________________________________________


# Test algo glouton pas optimal
#n = Graph.Graph.optimal_couplage_glouton()

# Mesure de Nmax_vertex
# Couplage plus rapide dans le cas de sommets
# random_graph prends beaucoup de temps lorsqu'on augmente les nombres des sommets (50.000 par exemple)

"""
Nmax_vertex_couplage = 3500
graph_v6 = Graph.Graph.random_graph(Nmax_vertex_couplage, 0.3) # ca prend beaucoup plus de temps que l'execution de l'algo couplage
temps_couplage = Graph.Graph.measure_time(graph_v6, "couplage")
print("Temps couplage: ", temps_couplage, " secondes", " pour Nmax(sommets) = ", Nmax_vertex_couplage)
print("")
# Temps couplage:  2.7588300704956055  secondes  pour Nmax(sommets) =  3500
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

"""
Nmax_proba_glouton = 0.95
graph_v7 = Graph.Graph.random_graph(250, Nmax_proba_glouton)
temps_couplage_proba_glouton = Graph.Graph.measure_time(graph_v7, "glouton")
print("Temps glouton: ", temps_couplage_proba_glouton, " secondes", " pour Nmax(proba) = ", Nmax_proba_glouton)
print("")
# Temps glouton:  2.07  secondes  pour Nmax(proba) =  0.95 et 250 sommets
"""

"""
Nmax_proba_couplage = 0.95
graph_v8 = Graph.Graph.random_graph(6500, Nmax_proba_couplage)
temps_couplage_proba = Graph.Graph.measure_time(graph_v8, "couplage")
print("Temps couplage: ", temps_couplage_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba_couplage)
print("")
#Temps couplage:  1.9830338954925537  secondes  pour Nmax(proba) =  0.95 et 3000 ~ 2800 sommets
"""

# Courbes temps / instance pour les execution des algos glouton et couplage
# Nmax_vertex_glouton = 350
# Graph.Graph.measure_execution_time_vertex("glouton", 10, Nmax_vertex_glouton, 0.3) #Pente de la régression linéaire: 2.66, 2.71
# Nmax_vertex_couplage = 3500
# Graph.Graph.measure_execution_time_vertex("couplage", 10, Nmax_vertex_couplage, 0.3) #Pente de la régression linéaire: 1.97, 2.5

# Nmax_proba_glouton = 0.95 #pour 250 sommets
# Graph.Graph.measure_execution_time_proba("glouton", 10, Nmax_proba_glouton, 250)
# Nmax_proba_couplage = 0.95 #pour 2800 sommets
# Graph.Graph.measure_execution_time_proba("couplage", 10, Nmax_proba_couplage, 6500)

# Courbes Courbes temps / nbsommets pour les execution de l'algo branch_and_bound_simple
Nmax_bab_simple = 20
# Graph.Graph.measure_execution_time_branch_simple(Nmax_bab_simple, 0.3)
# Graph.Graph.measure_execution_time_branch_simple(Nmax_bab_simple, 0.7)
# Graph.Graph.measure_execution_time_branch_simple(Nmax_bab_simple, 1/np.sqrt(Nmax_bab_simple))

Nmax_bab_bounds = 40
# Graph.Graph.measure_execution_time_branch_and_bound(Nmax_bab_bounds, 0.3)
# Graph.Graph.measure_execution_time_branch_and_bound(Nmax_bab_bounds, 0.7)
# Graph.Graph.measure_execution_time_branch_and_bound(Nmax_bab_bounds, 1/np.sqrt(Nmax_bab_bounds))


