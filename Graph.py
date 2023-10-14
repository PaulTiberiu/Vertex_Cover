import copy
import numpy as np
import random
import matplotlib.pyplot as plt
import time


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

#Question 2.1.1

    def remove_vertex(self, v):     
        """
        Retourne un nouveau graphe G_cpy sans le sommet v
        """

        G_cpy = copy.deepcopy(self)   # On cree une copie independante de notre Graphe pour pouvoir renvoyer un nouveau Graphe G' 

        if v not in G_cpy.V :         # S'il n'est pas dans l'ensemble de sommets, on quitte de la fonction
            return
        
        for vertex in G_cpy.E[v]:    # Apres avoir supprimme toutes les areetes du sommet v
            G_cpy.E[vertex].remove(v)

        del G_cpy.E[v]               # On supprime le sommet dans le dictionnaire d'arretes
        G_cpy.V.remove(v)            # On supprime le sommet dans l'ensemble des sommets
        
        return G_cpy


#Question 2.1.2
    
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

#Question 2.1.3

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

#Question 2.2

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
    

#Question 3.1

    def optimal(self):
        n = 2
        glouton = self.algo_glouton()
        couplage = self.algo_couplage()
        while len(glouton) < len(couplage) :
            n += 1
            self = Graph.random_graph(n,0.6)
            glouton = self.algo_glouton()
            couplage = self.algo_couplage()

        return n


#Question 3.2.2

    def algo_glouton(self) :
        """ ..."""
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
     

    def get_edges(self):
        """
        Cette méthode retourne une liste de toutes les arêtes sous forme de couples (v1, v2). Elle est utile pour pouvoir implementer l'algo couplage
        """
        edges = set()
        for v1, connected_vertices in self.E.items():
            for v2 in connected_vertices:
                if (v1, v2) not in edges and (v2, v1) not in edges:
                    edges.add((v1, v2))
        return edges

    def algo_couplage(self):
        """
        Couplage = ensemble d'aretes n'ayant pas d'exremite en commun
        """
        C = set()  # L'ensemble résultant
        covered = set()  # Les sommets déjà couverts

        edges = self.get_edges()

        for v1, v2 in edges:
            # Si aucune des extrémités de l'arête n'est dans C
            if v1 not in covered and v2 not in covered:
                C.add(v1)
                C.add(v2)
                covered.add(v1)
                covered.add(v2)

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
        sizes = [Nmax // 10 * i for i in range(1, 11)]   # la multiplication de i mauvaise ?

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
        plt.show()

        # Tracer la courbe en échelle logarithmique
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

        print(f"Pente de la régression linéaire: {slope:.2f}")

        plt.legend()
        plt.show()

        """
        plt.plot(np.log(sizes), np.log(execution_times), marker='o')
        plt.xlabel("Taille de l'instance (nombre de sommets)")
        plt.ylabel("Temps d'exécution moyen (secondes)")
        plt.title(f"Temps d'exécution de l'algorithme {algorithm}")
        plt.show()
        """


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



#Question 4.1.1 


def algo_branchement(self) :
    C = set()

    for s in self.V : 
        C.add(s)
        self = Graph.remove_vertex(self, s)
    

        
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

        # Ajoute les arêtes au graphe en utilisant insert_edge
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
