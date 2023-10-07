import copy
import numpy as np
import random

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
        Retourne le sommet avec le degré maximum dans le dictionnaire { sommet : degré }
        """

        dico_deg = self.vertex_degrees()
        candMax = -1
        s = -1

        for e in dico_deg :
            if dico_deg[e] > candMax :
                candMax = dico_deg[e]
                s = e
        return s #je renvoie plutôt la clé du sommet car c'est ce qui est demandé dans l'énoncé

#Question 2.2

    def random_graph(n, p):
        """
        Cree un graphe de n sommets ou chaque arete (i,j) est presente avec la probabilite p
        """


        if n <= 0:
            raise ValueError("Le parametre n doit etre superieur a 0")

        if p <= 0 or p >= 1:
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


#Question 3.2.2

    def algo_glouton(self) :
        """ Renvoie une liste des sommets classés par degré décroissant sachant que lorsqu'on a saisi un sommet, 
        on compare les derniers sommets entre eux, sans les aretes liés au sommet saisi"""
        C = [] #plutôt liste? car dans la question c écrit "emptyset" mais si c'est un ensemble ce n'est pas dans l'odre
        graph_cpy = copy.deepcopy(self) 

        while ( graph_cpy.E != {}) :
            Smax = graph_cpy.max_degree()   #récupère le sommet avec le degre max du dictionnaire
            C.append(Smax)                  #ajoute le sommet Smax à la liste C                    
            graph_cpy = graph_cpy.remove_vertex(Smax)   #Supprime Smax du dictionnaire
        return C
     

    def algo_couplage(self):
        """
        Couplage = ensemble d'aretes n'ayant pas d'exremite en commun
        """

        C = set()
        covered = set()

        # Parcourir toutes les arêtes dans le graphe
        for vertex in self.V:
            # Si le sommet n'est pas déjà couvert
            if vertex not in covered:
                for neighbour in self.E[vertex]:
                    # Si le voisin n'est pas déjà couvert
                    if neighbour not in covered:
                        # Ajouter le sommet et son voisin à C
                        C.add(vertex)
                        C.add(neighbour)
                        # Marquer les deux sommets comme couverts
                        covered.add(vertex)
                        covered.add(neighbour)

        return C
