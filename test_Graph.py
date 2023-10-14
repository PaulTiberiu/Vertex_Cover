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


print("Sommet avec le degre max: ", Graph.Graph.max_degree(graph))



n = 4
p = 0.5

graph_v4 = Graph.Graph.random_graph(n, p)


print(f'Graphe avec {n} sommets et des aretes creees avec une probabilite {p}\n sommets : {graph_v4.V}\n aretes : {graph_v4.E}')
# print(f'La couverture après l algo glouton est : {graph_v4.algo_glouton()}')

sommets = {0,1,2,3,4}
aretes = {0 : {1,3} , 1 : {0,2,4}, 2 : {1,3,4}, 3 : {0,2},4 :{1,2}}
graph_test = Graph.Graph(sommets,aretes)
couverture = graph_v4.algo_couplage()
print("La couverture obtenue après couplage est: ", couverture)
print(f'La couverture après l algo glouton est : {graph_v4.algo_glouton()}')





# print(f'La liste après l algo glouton est : {graph.algo_glouton()}')

print("Graphe avec n sommets, avec des aretes crees avec une probabilite p: ","sommets: ", graph_v4.V, "aretes: ", graph_v4.E)
print("")

couverture = graph.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)
print("")



filename = "graph.txt"
graph_from_file = Graph.Graph.create_graph_from_file(filename)
print("Graphe depuis fichier: ")
print("Sommets:", graph_from_file.V)
print("Aretes:", graph_from_file.E)
print("")
couverture = graph_from_file.algo_couplage()
print("La couverture obtenue a partir de graph est: ", couverture)
print("")

# Test algo glouton pas optimal
#n = Graph.Graph.optimal_couplage_glouton()


# Mesure de Nmax_vertex
# Couplage plus rapide dans le cas de sommets
# random_graph prends beaucoup de temps lorsqu'on augmente les nombres des sommets (50.000 par exemple)


# Nmax_vertex = 350
# graph_v5 = Graph.Graph.random_graph(Nmax_vertex, 0.9)

# temps_couplage = Graph.Graph.measure_time(graph_v5, "couplage")
# print("Temps couplage: ", temps_couplage, " secondes", " pour Nmax(sommets) = ", Nmax_vertex)

# temps_glouton = Graph.Graph.measure_time(graph_v5, "glouton")
# print("Temps glouton: ", temps_glouton, " secondes", " pour Nmax(sommets) = ", Nmax_vertex)

# Il faut aussi mesurer Nmax_proba, mais ca depend sourtout du nombre de sommets ... a voir (proba 0.3 a 0.99 avec 350 sommets augmente de 3 sec a 9.8 sec pour glouton)



# Nmax_proba = 0.99
# graph_v7 = Graph.Graph.random_graph(350, Nmax_proba)

# temps_couplage_proba = Graph.Graph.measure_time(graph_v7, "couplage")
# print("Temps couplage: ", temps_couplage_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)

# temps_glouton_proba = Graph.Graph.measure_time(graph_v7, "glouton")
# print("Temps glouton: ", temps_glouton_proba, " secondes", " pour Nmax(proba) = ", Nmax_proba)




# Courbes temps / instance

# Graph.Graph.measure_execution_time_vertex("glouton", 10, 350, 0.3) # Deja teste, capture ecran vm
#Graph.Graph.measure_execution_time_vertex("couplage", 10, Nmax_vertex, 0.3) # Deja teste, capture ecran vm

#Graph.Graph.measure_execution_time_proba("glouton", 10, 50, Nmax_proba)     a tester
#Graph.Graph.measure_execution_time_vertex("couplage", 10, 50, Nmax_proba)   a tester

G_init = Graph.Graph.random_graph(2, 0.5)
print(f'Le nombre de sommets nécessaires pour que couplage soit optimal est : {G_init.optimal()}')




"""
Nmax_vertex_couplage = 7000
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
#Temps couplage:  1.9830338954925537  secondes  pour Nmax(proba) =  0.95 et 6500 sommets
"""

# Courbes temps / instance

Nmax_vertex_glouton = 350
Graph.Graph.measure_execution_time_vertex("glouton", 10, Nmax_vertex_glouton, 0.3) #Pente de la régression linéaire: 2.66
#Nmax_vertex_couplage = 7000
#Graph.Graph.measure_execution_time_vertex("couplage", 10, Nmax_vertex_couplage, 0.3) #Pente de la régression linéaire: 1.97


#Nmax_proba_glouton = 0.95 #pour 250 sommets
#Graph.Graph.measure_execution_time_proba("glouton", 10, Nmax_proba_glouton, 250)
#Nmax_proba_couplage = 0.95 #pour 6500 sommets
#Graph.Graph.measure_execution_time_proba("couplage", 10, Nmax_proba_couplage, 6500)
