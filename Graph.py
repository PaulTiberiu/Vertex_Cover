import copy
import numpy as np
import random
import matplotlib.pyplot as plt
import time

# V = ca doit etre un tableau?

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
        
        for vertex in G_cpy.E[v]:    # Apres avoir supprimme toutes les aretes du sommet v 
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

        # Tracer la courbe y et log(x) pour avoir la base de l'exponentiel, mais c'est pas une droite....
        plt.figure()
        plt.plot(sizes, execution_times, marker='o', label="log(Temps réel)")
        plt.xscale('log')
        plt.xlabel("Taille de l'instance log(nombre de sommets)")
        plt.ylabel("Temps d'exécution moyen")
        plt.title(f"Logarithme du nombre de sommets de l'algorithme {algorithm}")

        # Calculer la pente (coefficient directeur) de la régression linéaire en utilisant NumPy
        slope2, intercept = np.polyfit(sizes, np.log(execution_times), 1)
        print(f"Pente = Base de la régression linéaire: {slope2:.2f}")
        #plt.plot(sizes, np.exp(slope * log_sizes + intercept), 'r--', label="Régression linéaire")

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
   

    def remove_vertex_self(self, v):
        """
        Modifie le graphe passe en parametre sans le sommet v, sans le renvoyer
        """

        if v not in self.V or v not in self.E: # S'il n'est pas dans l'ensemble de sommets, on quitte de la fonction
            return 
        
        for vertex in self.E[v]: # Apres avoir supprimme toutes les aretes du sommet v 
            self.E[vertex].remove(v)

        del self.E[v] # On supprime le sommet dans le dictionnaire d'arretes

        self.V.remove(v) # On supprime le sommet dans l'ensemble des sommets
        

    def branch_and_bound(self): # solution realisable, mais pas OPTIMALE!
        # Initialisation de la meilleure solution
        best_solution = set()

        # Initialisation de la pile (utiliser une liste pour simuler une pile)
        stack = [(self, set())]

        # Ouvrir un fichier pour écrire les informations, comme ca on evite de surcharger le terminal
        with open("branch_and_bound_log.txt", "w") as log_file:
            while stack:
                graph, current_solution = stack.pop() # Current solution c'est l'ensemble de sommets qu'on insere dans la pile lors d'un branchement

                log_file.write("La pile: \n")
                log_file.write(f"Graph: {graph.V}, {graph.E}\n")
                log_file.write(f"Current Solution: {current_solution}\n\n")

                # Mettre à jour la meilleure solution si nécessaire
                if len(current_solution) > len(best_solution):
                    best_solution = current_solution
                    log_file.write(f"Mise a jour meilleure solution: {best_solution}\n\n")

                if graph.E:  # S'il reste des arêtes dans le graphe
                    # Parcourir chaque sommet et ses arêtes adjacentes
                    for u in graph.V:
                        for v in graph.E[u]:
                            # Créer une copie du graphe sans l'arête (u, v)
                            new_graph_u = graph.remove_vertex_self(u)
                            log_file.write(f"Graphe sans le sommet: {u}, {new_graph_u.V}, {new_graph_u.E}\n")
                            new_graph_v = graph.remove_vertex_self(v)
                            log_file.write(f"Graphe sans le sommet: {v}, {new_graph_v.V}, {new_graph_v.E}\n\n")

                            # Brancher en ajoutant u dans la couverture
                            stack.append((new_graph_u, current_solution | {u}))
                            log_file.write(f"La pile update sans le sommet: {u}\n")
                            log_file.write(f"Graph: {new_graph_u.V}, {new_graph_u.E}\n")
                            log_file.write(f"Current Solution: {current_solution}\n\n")

                            # Brancher en ajoutant v dans la couverture
                            stack.append((new_graph_v, current_solution | {v}))
                            log_file.write(f"La pile update sans le sommet: {v}\n")
                            log_file.write(f"Graph: {new_graph_v.V}, {new_graph_v.E}\n")
                            log_file.write(f"Current Solution: {current_solution}\n\n")

        return best_solution


    def branch_and_bound_simple(self):
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

            # Si un sommet u a été trouvé, on effectue les branchements
            if u != -1:
                # Branchement en ajoutant u dans la couverture
                new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                new_graph.remove_vertex_self(u)  # Suppression de u du graphe
                new_cover = cover.copy()  # Copie de la solution actuelle
                new_cover.add(u)  # Ajout de u à la couverture
                stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

                # Branchement en ajoutant v dans la couverture
                new_graph = copy.deepcopy(graph)  # Création d'une copie du graphe actuel
                new_graph.remove_vertex_self(v)  # Suppression de v du graphe
                new_cover = cover.copy()  # Copie de la solution actuelle
                new_cover.add(v)  # Ajout de v à la couverture
                stack.append((new_graph, new_cover))  # Ajout de la nouvelle configuration à la pile

        return best_solution  # Retourne la meilleure solution trouvée


