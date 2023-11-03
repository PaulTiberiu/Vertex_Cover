# Virginie CHEN        Paul-Tiberiu IORDACHE

import copy
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import math
from scipy.stats import linregress

class Graph:
    V = set # Ensemble de sommets (la liste de sommets) 
    E = dict # Dictionnaire de aretes (la liste d'arretes)


    def __init__(self, V, E=None):
        """
        Permet de creer le graphe avec les valeurs V et E pasees en parametre
        """
        
        self.V = V

        if(E == None):
            self.E = {i : set() for i in V} # Creer le dictionnaire qui relie le sommet i a vide
        else:
            self.E = E

    def insert_edge(self, v1, v2): 
        """
        Permet d'ajouter une arrete
        """

        self.E[v1].add(v2)          # On ajoute v1 a v2 et
        self.E[v2].add(v1)          # v2 a v1 car le graphe est non oriente


    def remove_vertex(self, v):     
        """
        Retourne un nouveau graphe G_cpy sans le sommet v
        """

        G_cpy = copy.deepcopy(self)   # On cree une copie independante de notre Graphe pour pouvoir renvoyer un nouveau Graphe G' 

        if v not in G_cpy.V :         # S'il n'est pas dans l'ensemble de sommets, on quitte de la fonction
            return
        
        for vertex in G_cpy.E[v]:    # Apres avoir supprimme toutes les aretes du sommet v 
            G_cpy.E[vertex].remove(v)

        del G_cpy.E[v]               # On supprime le sommet dans le dictionnaire d'arretes
        G_cpy.V.remove(v)            # On supprime le sommet dans l'ensemble des sommets
        
        return G_cpy

    
    def remove_many_vertex(self, set_delete) :
        """
        Retourne un nouveau graphe G_cpy sans les sommets de l'ensemble set_delete
        """

        G_cpy = copy.deepcopy(self)   # On cree une copie independante de notre Graphe pour pouvoir renvoyer un nouveau Graphe G' 

        for i in set_delete: # On reeutilise l'algorithme de la fonction remove_vertex en faisant une boucle sur les valeurs de set_delete

            if i not in G_cpy.V :         
                return                 
            
            for vertex in G_cpy.E[i]:    
                G_cpy.E[vertex].remove(i)

            del G_cpy.E[i]               
            G_cpy.V.remove(i)            
            
        return G_cpy


    """
    def ens_to_tab(Ens):
        T = np.array(list(Ens))  # Convertissez l'ensemble dans une liste, puis en un tableau numpy
        return T
    """

    def vertex_degrees(self) :        
        """
        Renvoie un nouveau dictionnaire qui associe chaque sommet (clé) à son degré (valeur)
        """

        deg = dict()

        for i in self.E :
            deg[i] = len(self.E[i]) 

        return deg

    def max_degree(self) :           
        """
        Cherche le degré maximum dans le dictionnaire { sommet : degré } et renvoie la cle
        """

        dico_deg = self.vertex_degrees()
        candMax = -1
        s = -1

        for e in dico_deg :
            if dico_deg[e] > candMax :
                candMax = dico_deg[e]
                s = e

        return s 

    def random_graph(n, p):
        """
        Cree un graphe de n sommets ou chaque arete (i,j) est presente avec la probabilite p
        """

        if n < 0:
            raise ValueError("Le parametre n doit etre superieur a 0")

        if p < 0 or p > 1:
            raise ValueError("Le parametre p doit etre entre 0 et 1")

        adjacents = None 
        vertices = set()

        for i in range(n):
            vertices.add(i)
            
        graph = Graph(vertices, adjacents)
    
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    graph.insert_edge(i, j)

        return graph
    

    def algo_couplage(self) : 
        C = set()  # Crée un ensemble vide pour stocker la couverture

        for u in self.V:  # Parcours de chaque sommet u dans V
            for v in self.E[u]:  # Parcours des arêtes adjacentes à u
                # Vérifie si aucune des deux extrémités n'est déjà dans C
                if u not in C and v not in C:
                    C.add(u)  # Ajoute u à la couverture
                    C.add(v)  # Ajoute v à la couverture

        return C  # Renvoie la couverture


    def algo_glouton(self):
        """
        Renvoie une liste des sommets classés par degré décroissant sachant que lorsqu'on a saisi un sommet, 
        on compare les derniers sommets entre eux, sans les aretes liés au sommet saisi
        """
        
        C = set() #plutôt liste? car dans la question c écrit "emptyset" mais si c'est un ensemble ce n'est pas dans l'odre
        graph_cpy = copy.deepcopy(self) 

        while ( graph_cpy.E != {}) :
  
            Smax = graph_cpy.max_degree()   #récupère le sommet avec le degre max du dictionnaire
            if len(graph_cpy.E[Smax]) == 0 :
                graph_cpy = graph_cpy.remove_vertex(Smax)
            else :
                C.add(Smax)                  #ajoute le sommet Smax à la liste C                    
                graph_cpy = graph_cpy.remove_vertex(Smax)   #Supprime Smax du dictionnaire
        return C
        

    def measure_time(graph, algorithm):
        
        start_time = time.time()

        if algorithm == "couplage":
            solution = graph.algo_couplage()

        elif algorithm == "glouton":
            solution = graph.algo_glouton()

        end_time = time.time()
        execution_time = end_time - start_time

        return execution_time
    
    def measure_execution_time_vertex(algorithm, num_graphs_per_size, Nmax, p):
        
        execution_times = []
        sizes = [Nmax // 10 * i for i in range(1, 11)]

        for nmax in sizes:
            total_execution_time = 0

            for _ in range(num_graphs_per_size):
                graph = Graph.random_graph(nmax, p)

                start_time = time.time()
                if algorithm == "glouton":
                    solution = graph.algo_glouton()

                elif algorithm == "couplage":
                    solution = graph.algo_couplage()

                end_time = time.time()
                execution_time = end_time - start_time

                total_execution_time += execution_time

            average_execution_time = total_execution_time / num_graphs_per_size
            execution_times.append(average_execution_time)

        # Tracer la courbe du temps en fonction de la taille de l'instance
        # A transformer les trucs en log
        # Puis plot de nouveau en echelle log => lineaire voir pente pour degree polynome
        plt.plot(sizes, execution_times, marker='o')
        plt.xlabel("Taille de l'instance (nombre de sommets)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title(f"Temps d'exécution de l'algorithme {algorithm}")

        # Tracer la courbe en échelle logarithmique
        plt.figure()
        plt.plot(sizes, execution_times, marker='o', label="Temps réel")
        plt.yscale('log')
        plt.xlabel("Taille de l'instance (nombre de sommets)")
        plt.ylabel("Temps d'exécution moyen (log secondes)")
        plt.title(f"Temps d'exécution de l'algorithme {algorithm} (log(y) scale)")

        # Tracer la courbe en échelle log - log
        plt.figure()
        plt.plot(sizes, execution_times, marker='o', label="Temps réel")
        plt.yscale('log')
        plt.xscale('log')
        plt.xlabel("Taille de l'instance (nombre de sommets) en log")
        plt.ylabel("Temps d'exécution moyen (log secondes)")
        plt.title(f"Temps d'exécution de l'algorithme {algorithm} (log-log scale)")

        # Calculer la pente (coefficient directeur) de la régression linéaire en utilisant NumPy
        log_sizes = np.log(sizes)
        log_times = np.log(execution_times)
        slope, intercept = np.polyfit(log_sizes, log_times, 1)
        plt.plot(sizes, np.exp(slope * log_sizes + intercept), 'r--', label="Régression linéaire")
        print(f"Pente de la régression linéaire (log log): {slope:.2f}")
        plt.legend()
        plt.show()


    def measure_execution_time_proba(algorithm, num_graphs_per_size, Nmax, nb_vertices):
        
        execution_times = []
        sizes = [Nmax / 10 * i for i in range(1, 11)]
        print(sizes)

        for nmax in sizes:
            total_execution_time = 0

            for _ in range(num_graphs_per_size):
                graph = Graph.random_graph(nb_vertices, nmax)

                start_time = time.time()
                if algorithm == "glouton":
                    solution = graph.algo_glouton()

                elif algorithm == "couplage":
                    solution = graph.algo_couplage()

                end_time = time.time()
                execution_time = end_time - start_time

                total_execution_time += execution_time

            average_execution_time = total_execution_time / num_graphs_per_size
            execution_times.append(average_execution_time)

        # Tracer la courbe du temps en fonction de la taille de l'instance
        plt.plot(sizes, execution_times, marker='o')
        plt.xlabel("Taille de l'instance (nombre de probabilites)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title(f"Temps d'exécution de l'algorithme {algorithm}")
        plt.show()

        
    def create_graph_from_file(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Initialisation des variables
        vertices = set()
        edges = []

        # Parcourir les lignes du fichier
        for line in lines:
            line = line.strip()

            if line == "Nombre de sommets":
                read_vertices = False
                read_edges = False
            elif line == "Sommets":
                read_vertices = True
                read_edges = False
            elif line == "Nombre d aretes":
                read_vertices = False
            elif line == "Aretes":
                read_vertices = False
                read_edges = True
            elif read_vertices and line.isdigit():
                vertices.add(int(line))
            elif read_edges:
                v1, v2 = map(int, line.split())
                # Vérifier que v1 et v2 sont dans la liste des sommets
                if v1 in vertices and v2 in vertices:
                    edges.append((v1, v2))

        # Créer un objet Graphe
        graph = Graph(vertices)

        # Ajouter les arêtes au graphe en utilisant insert_edge
        for v1, v2 in edges:
            graph.insert_edge(v1, v2)

        return graph
    
    def optimal_couplage_glouton(): 
        n = 2
        graph = Graph.random_graph(n, 0.5) # Creer un graphe aleatoire
        print(graph.V)
        print(graph.E)
        glouton = graph.algo_glouton()
        couplage = graph.algo_couplage()

        while len(glouton) <= len(couplage) : # Tant que glouton trouve une solution plus optimale que couplage
            n += 1
            print(n)
            graph = Graph.random_graph(n,0.3)
            glouton = graph.algo_glouton()
            couplage = graph.algo_couplage()
            
        print("Sommets :", graph.V)
        print("Aretes: ", graph.E)
        print("Solution couplage: ", couplage)
        print("Solution glouton: ", glouton)
        print("n")
        return n        
    

    def branch_simple(self):
        best_solution = None
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            # Recherche d'un sommet u de l'arête à brancher
            u = -1
            v = -1

            for vertex, edges in graph.E.items():
                if len(edges) != 0:
                    u = vertex
                    for v in edges:
                        break  # On récupère le premier sommet v avec une arête
                    if u != -1:
                        break

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if u != -1 and v != -1:
                # Branchement en ajoutant u dans la couverture
                new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                new_graph = new_graph.remove_vertex(u)  # Suppression de u du graphe
                new_cover = cover.copy()  # Copie de la solution actuelle
                new_cover.add(u)  # Ajout de u à la couverture
                stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

                # Branchement en ajoutant v dans la couverture
                new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                new_graph = new_graph.remove_vertex(v)  # Suppression de v du graphe
                new_cover = cover.copy()  # Copie de la solution actuelle
                new_cover.add(v)  # Ajout de v à la couverture
                stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

        return best_solution  # Retourne la meilleure solution trouvée
    
    
    def get_couplage(self) :
        """ retourne un couplage du graph en entrée"""
        couplage = set()
        covered = set()

        for vertex in self.V : 
            if vertex in covered :
                continue

            for neighbour in self.E[vertex] :
                if neighbour not in covered :
                    couplage.add( (vertex,neighbour) )
                    covered.add(neighbour)
                    covered.add(vertex)
                    break

        return couplage


    def calculate_lower_bound(self):
        """
        Calcul de la borne inferieure
        """

        n = len(self.V) # Nombre de sommets
        m = sum (len(v) for v in self.E.values()) / 2 # Nombre d'arêtes

        # calcul des bornes
        delta = len(self.E[self.max_degree()]) # Degré maximum des sommets du graphe

        b1 = math.ceil(m / delta) if delta else 0
        
        M = self.get_couplage()
        b2 = len(M)
        
        b3 = ( 2*n - 1 - math.sqrt((2*n - 1)**2 - 8*m) ) / 2

        return max(b1, b2, b3)


    def branch_and_bound(self):
        """
        Calcul de branch and bound en prenant en compte les bornes de la partie 4.2
        """

        best_solution = self.algo_couplage() # On initialise la meilleure solution avec une couverture aleatoire
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            upper_bound = graph.algo_couplage()

            # Vérification de la réalisabilité
            if (lower_bound + len(cover) >= len(best_solution)) :
                continue # On élague

            if upper_bound and len(upper_bound) == lower_bound : # Si on a une solution optimale
                if len(upper_bound | cover) <= len(best_solution): # on vérifie si la solution avec la couverture actuelle fonctionne
                    best_solution = upper_bound | cover
                continue # On élague

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution


            if len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                for vertex, edges in graph.E.items():
                    if len(edges) != 0:
                        u = vertex
                        for v in edges:
                            break  # On récupère le premier sommet v avec une arête
                        if u != -1:
                            break

                # Si les sommets u,v ont été trouvés, on effectue les branchements
                if u != -1 and v != -1:
                    # Branchement en ajoutant u dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_graph = new_graph.remove_vertex(u)  # Suppression de u du graphe
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(u)  # Ajout de u à la couverture
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

                    # Branchement en ajoutant v dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_graph = new_graph.remove_vertex(v)  # Suppression de v du graphe
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(v)  # Ajout de v à la couverture
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

        return best_solution  # Retourne la meilleure solution trouvée
    

    def improved_branch_and_bound(self):
        """
        Calcul de branch and bound ameliore
        """

        best_solution = self.algo_couplage() # On initialise la meilleure solution avec une couverture aleatoire
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            upper_bound = self.algo_couplage()

            # Vérification de la réalisabilité
            if (lower_bound + len(cover) >= len(best_solution)) :
                continue

            if upper_bound and len(upper_bound) == lower_bound : # Si on a une solution optimale
                if len(upper_bound | cover) <= len(best_solution): # on vérifie si la solution avec la couverture actuelle fonctionne
                    best_solution = upper_bound | cover
                continue # on élague

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            if len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                for vertex, edges in graph.E.items():
                    if len(edges) != 0:
                        u = vertex
                        for v in edges:
                            break  # On récupère le premier sommet v avec une arête
                        if u != -1:
                            break

                # Si les sommets u,v ont été trouvés, on effectue les branchements
                if u != -1 and v != -1:
                    # Branchement en ajoutant u dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_graph = new_graph.remove_vertex(u)  # Suppression de u du graphe
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(u)  # Ajout de u à la couverture
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

                    # Branchement en ajoutant v dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(v)  # Ajout de v à la couverture
                    for neighbour in graph.E[u]: # Ajouter à la couverture les voisins de u en les supprimant du graphe
                        new_cover.add(neighbour)
                        new_graph = new_graph.remove_vertex(neighbour)
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

        return best_solution  # Retourne la meilleure solution trouvée

    
    def improved_branch_and_bound_degmax(self):
    
        #Calcul de branch and bound ameliore en prenant le degree max du sommet
    

        best_solution = self.algo_couplage() # On initialise la meilleure solution avec une couverture aleatoire 
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            upper_bound = self.algo_couplage()

            # Vérification de la réalisabilité
            if (lower_bound + len(cover) >= len(best_solution)) :
                continue

            if upper_bound and len(upper_bound) == lower_bound : # Si on a une solution optimale
                if len(upper_bound | cover) <= len(best_solution): # on vérifie si la solution avec la couverture actuelle fonctionne
                    best_solution = upper_bound | cover
                continue # on élague

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            if len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                # Prendre le sommet u avec le plus grand degre
                max_degree = graph.max_degree()

                if(max_degree != None):
                    u = max_degree
                    if len(graph.E[u]) != 0:
                        for v in graph.E[u]:
                            break  # On récupère le premier sommet v avec une arête
                        

                # Si les sommets u,v ont été trouvés, on effectue les branchements
                if u != -1 and v != -1:
                    # Branchement en ajoutant u dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_graph = new_graph.remove_vertex(u)  # Suppression de u du graphe
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(u)  # Ajout de u à la couverture
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

                    # Branchement en ajoutant v dans la couverture
                    new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                    new_cover = cover.copy()  # Copie de la solution actuelle
                    new_cover.add(v)  # Ajout de v à la couverture
                    for neighbour in graph.E[u]: # Ajouter à la couverture les voisins de u en les supprimant du graphe
                        new_cover.add(neighbour)
                        new_graph = new_graph.remove_vertex(neighbour)
                    stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

        return best_solution  # Retourne la meilleure solution trouvée
    
    
    def measure_execution_time_branch_mean(algorithm, num_graphs_per_size, Nmax, p):
        execution_times = []

        for n in range(1, Nmax + 1):
            total_execution_time = 0

            for _ in range(num_graphs_per_size):
                graph = Graph.random_graph(n, p)
                
                start_time = time.time()

                if(algorithm == "branch_simple"):
                    cover = graph.branch_simple()
                elif(algorithm == "branch_and_bound"):
                    cover = graph.branch_and_bound()
                elif(algorithm == "improved_branch_and_bound"):
                    cover = graph.improved_branch_and_bound()
                elif(algorithm == "improved_branch_and_bound_degmax"):
                    cover = graph.improved_branch_and_bound_degmax()

                end_time = time.time()

                execution_time = end_time - start_time
                total_execution_time += execution_time

            average_execution_time = total_execution_time / num_graphs_per_size
            execution_times.append(average_execution_time)

        print(execution_times)

        # Tracé du temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), execution_times, marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title("Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times), marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times), marker='o')
        plt.xlabel("Log Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction du log taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times), marker='o')
        plt.xlabel("Log Taille du graphe (n)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.xscale("log")
        plt.title("Temps d'exécution moyen du Branchement en fonction du log taille du graphe")
        plt.show()
        
        # Calculer la pente (base de l'exponentielle)
        for i in range(len(execution_times)): # Boucle qui permet de trouver l'indice du dernier element a 0
            if(execution_times[i] == 0): # Car quand l'algo s'execute tres vite, 3e-07 par exemple, on aura un 0 qui s'affiche
                last0 = i

        last0 = last0 + 1 # Vu que la liste commence a 0, ajouter 1
        #print("last0 ",last0)
    
        exec_times_no0 = []
        for i in range(last0, len(execution_times)):
            exec_times_no0.append(execution_times[i]) # Creer la liste de temps d'execution sans les valeurs a 0

        #print("exec_times_no0 ", exec_times_no0)

        N = np.array(range(1, Nmax + 1))
        #print("N ",N)
        exec_times_log = np.log(exec_times_no0) # Passer en log
        #print("exec_times_log ", exec_times_log)

        new_N = []
        
        for i in range(last0, len(execution_times)): # Construire la liste de sommets de longueur egale a celle de log temps d'execution
            new_N.append(N[i]) # Car il faut avoir 2 listes de longueur egale pour calculer la pente

        #print("new_N ", new_N)

        if N is not None and exec_times_log is not None:
            slope = linregress(new_N, exec_times_log)
            exp_base = np.exp(slope.slope)
            print("Slope: ", slope.slope)
            print("Base exponentielle: ", exp_base)
        else:
            print("Pas assez des donnees.")
        
                

    def measure_execution_time_branch(algorithm ,Nmax, p):
        execution_times = []

        for n in range(1, Nmax + 1):
            graph = Graph.random_graph(n, p)
            start_time = time.time()

            if(algorithm == "branch_simple"):
                cover = graph.branch_simple()
            elif(algorithm == "branch_and_bound"):
                cover = graph.branch_and_bound()
            elif(algorithm == "improved_branch_and_bound"):
                cover = graph.improved_branch_and_bound()
            elif(algorithm == "improved_branch_and_bound_degmax"):
                cover = graph.improved_branch_and_bound_degmax()

            end_time = time.time()

            execution_time = end_time - start_time
            execution_times.append(execution_time)

            if n % 5 == 0:
                print(f"Processed {n} graphs. Total time: {sum(execution_times):.2f} seconds.")

        # Tracé du temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), execution_times, marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Temps d'exécution (secondes)")
        plt.title("Temps d'exécution du Branchement simple en fonction de la taille du graphe")
        plt.show()

        # Tracé du temps d'exécution en fonction du log de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), np.log(execution_times), marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Temps d'exécution (secondes)")
        plt.title("Temps d'exécution du Branchement en fonction de la taille du graphe")
        plt.show()

    def approx_ratio(algorithm, Nmax, p):
        """
        Calcule le rapport d'approximation
        """

        worst_ratio = 0

        for n in range(3, Nmax + 1):
            graph = Graph.random_graph(n, p)
    
            glouton = graph.algo_glouton()
            cover = graph.algo_couplage()
            
            if(algorithm == "branch_simple"):
                branch = graph.branch_simple()
            elif(algorithm == "branch_and_bound"):
                branch = graph.branch_and_bound()
            elif(algorithm == "improved_branch_and_bound"):
                branch = graph.improved_branch_and_bound()
            elif(algorithm == "improved_branch_and_bound_degmax"):
                branch = graph.improved_branch_and_bound_degmax()

            ratio_glouton = len(glouton) / len(branch)
            ratio_cover = len(cover) / len(branch)

            print("Pour n =", n)
            print("Longueur du glouton:", len(glouton))
            print("Longueur du couplage:", len(cover))
            print("Longueur du branch:", len(branch))
            print("Rapport d'approximation Glouton:", ratio_glouton)
            print("Rapport d'approximation Couplage:", ratio_cover)
            

            worst_ratio = max(worst_ratio, ratio_glouton, ratio_cover)

        print("Plus mauvais rapport d'approximation:", worst_ratio)

    

    def measure_execution_time_improved_degmax_mean(num_graphs_per_size, Nmax, p):
        execution_times_imp = []
        execution_times_degmax = []

        for n in range(1, Nmax + 1):
            total_execution_time_imp = 0
            total_execution_time_degmax = 0

            for _ in range(num_graphs_per_size):
                graph = Graph.random_graph(n, p)
                
                start_time = time.time()
                cover_imp = graph.improved_branch_and_bound()
                end_time = time.time()
                execution_time_imp = end_time - start_time
                total_execution_time_imp += execution_time_imp


                start_time_degmax = time.time()
                cover_degmax = graph.improved_branch_and_bound_degmax()
                end_time_degmax = time.time()
                execution_time_degmax = end_time_degmax - start_time_degmax
                total_execution_time_degmax += execution_time_degmax

            average_execution_time_imp = total_execution_time_imp / num_graphs_per_size
            execution_times_imp.append(average_execution_time_imp)

            average_execution_time_degmax = total_execution_time_degmax / num_graphs_per_size
            execution_times_degmax.append(average_execution_time_degmax)

        print(execution_times_imp)
        print(execution_times_degmax)

        # Tracé du temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), execution_times_imp, marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title("Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times_imp), marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times_imp), marker='o')
        plt.xlabel("Log Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction du log taille du graphe")
        plt.show()

        # Tracé du temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), execution_times_degmax, marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title("Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times_degmax), marker='o')
        plt.xlabel("Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction de la taille du graphe")
        plt.show()

        # Tracé du log de temps d'exécution en fonction de la taille du graphe (n)
        plt.plot(range(1, Nmax + 1), (execution_times_degmax), marker='o')
        plt.xlabel("Log Taille du graphe (n)")
        plt.ylabel("Log Temps d'exécution moyen (secondes)")
        plt.yscale("log")
        plt.xscale("log")
        plt.title("Log du Temps d'exécution moyen du Branchement en fonction du log taille du graphe")
        plt.show()

        # Calculer la pente (base de l'exponentielle)
        for i in range(len(execution_times_imp)): # Boucle qui permet de trouver l'indice du dernier element a 0
            if(execution_times_imp[i] == 0): # Car quand l'algo s'execute tres vite, 3e-07 par exemple, on aura un 0 qui s'affiche
                last0 = i

        last0 = last0 + 1 # Vu que la liste commence a 0, ajouter 1
        #print("last0 ",last0)
    
        exec_times_no0 = []
        for i in range(last0, len(execution_times_imp)):
            exec_times_no0.append(execution_times_imp[i]) # Creer la liste de temps d'execution sans les valeurs a 0

        #print("exec_times_no0 ", exec_times_no0)

        N = np.array(range(1, Nmax + 1))
        #print("N ",N)
        exec_times_log = np.log(exec_times_no0) # Passer en log
        #print("exec_times_log ", exec_times_log)

        new_N = []
        
        for i in range(last0, len(execution_times_imp)): # Construire la liste de sommets de longueur egale a celle de log temps d'execution
            new_N.append(N[i]) # Car il faut avoir 2 listes de longueur egale pour calculer la pente

        #print("new_N ", new_N)

        if N is not None and exec_times_log is not None:
            slope = linregress(new_N, exec_times_log)
            exp_base = np.exp(slope.slope)
            print("Slope: ", slope.slope)
            print("Base exponentielle: ", exp_base)
        else:
            print("Pas assez des donnees.")
        
        # Calculer la pente (base de l'exponentielle)
        for i in range(len(execution_times_degmax)): # Boucle qui permet de trouver l'indice du dernier element a 0
            if(execution_times_imp[i] == 0): # Car quand l'algo s'execute tres vite, 3e-07 par exemple, on aura un 0 qui s'affiche
                last0_degmax = i

        last0_degmax = last0_degmax + 1 # Vu que la liste commence a 0, ajouter 1
        #print("last0 ",last0)
    
        exec_times_no0_degmax = []
        for i in range(last0_degmax, len(execution_times_degmax)):
            exec_times_no0_degmax.append(execution_times_degmax[i]) # Creer la liste de temps d'execution sans les valeurs a 0

        print("exec_times_no0 ", exec_times_no0)

        N_degmax = np.array(range(1, Nmax + 1))
        print("N ",N)
        exec_times_log_degmax = np.log(exec_times_no0_degmax) # Passer en log
        print("exec_times_log ", exec_times_log)

        new_N_degmax = []
        
        for i in range(last0_degmax, len(execution_times_degmax)): # Construire la liste de sommets de longueur egale a celle de log temps d'execution
            new_N_degmax.append(N_degmax[i]) # Car il faut avoir 2 listes de longueur egale pour calculer la pente


        if N_degmax is not None and exec_times_log_degmax is not None:
            slope_degmax = linregress(new_N_degmax, exec_times_log_degmax)
            exp_base_degmax = np.exp(slope_degmax.slope)
            print("Slope degmax: ", slope_degmax.slope)
            print("Base exponentielle degmax: ", exp_base_degmax)
        else:
            print("Pas assez des donnees.")
