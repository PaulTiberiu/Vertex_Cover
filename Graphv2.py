if best_solution is not None and (len(best_solution) <= lower_bound or len(cover) < lower_bound or len(cover) > higher_bound or lower_bound >= higher_bound):
                continue  # Élaguer cette branche

def improved_branch_and_bound_degmax(self):
        """
        Calcul de branch and bound ameliore en prenant le degree max du sommet
        """

        best_solution = None
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            higher_bound = len(self.algo_couplage())

            if best_solution is not None:
                if(len(best_solution) <= lower_bound):
                    continue # Elaguer la branche si la meilleure solution est plus petite que la borne inférieure du noeud actuel

                if(higher_bound is not None and higher_bound == lower_bound):
                    if(higher_bound <= len(best_solution)):
                        best_solution = higher_bound
                    continue
            """
            if best_solution is not None and (len(cover) < lower_bound or len(cover) > higher_bound or lower_bound >= higher_bound):
                continue  # Élaguer cette branche
            """

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            if best_solution is None or len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                # Prendre le sommet u avec le plus grand degre
                max_degree = graph.max_degree()

                if(max_degree != None):
                    print(u)
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


"""
def improved_branch_and_bound_degmax(self):
    
        #Calcul de branch and bound ameliore en prenant le degree max du sommet
    

        best_solution = None
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            higher_bound = len(self.algo_couplage())

            if best_solution is not None and (len(cover) < lower_bound or len(cover) > higher_bound or lower_bound >= higher_bound):
                continue  # Élaguer cette branche

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            if best_solution is None or len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                # Prendre le sommet u avec le plus grand degre
                max_degree = graph.max_degree()

                if(max_degree != None):
                    print(u)
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
"""

def improved_branch_and_bound_degmax(self):
        """
        Calcul de branch and bound ameliore en prenant le degree max du sommet
        """

        best_solution = None
        stack = []  # Initialisation d'une pile pour le parcours en profondeur
        initial_solution = set()  # Initialisation de la solution actuelle (vide)
        stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

        while stack:  # Boucle principale de l'algorithme
            graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

            # Calcul de la borne inférieure (2) dans l'énoncé
            lower_bound = Graph.calculate_lower_bound(graph)

            # Calcul de la borne supérieure (1) dans l'énoncé
            higher_bound = len(self.algo_couplage())

            if best_solution is not None:
                if(len(best_solution) <= lower_bound):
                    continue # Elaguer la branche si la meilleure solution est plus petite que la borne inférieure du noeud actuel

                if(higher_bound is not None and higher_bound == lower_bound):
                    if(higher_bound <= len(best_solution)):
                        best_solution = higher_bound
                    continue

            # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
            if not graph.V or all(len(value) == 0 for value in graph.E.values()):
                # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
                if best_solution is None or len(cover) < len(best_solution):
                    best_solution = cover  # Mettre à jour la meilleure solution

            if best_solution is None or len(cover) < len(best_solution):
                
                # Recherche d'un sommet u de l'arête à brancher
                u = -1
                v = -1

                # Prendre le sommet u avec le plus grand degre
                max_degree = graph.max_degree()

                if(max_degree != None):
                    u = max_degree
                    print(u)
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


def branch_and_bound(self):
    """
    Calcul de branch and bound en prenant en compte les bornes de la partie 4.2
    """

    best_solution = None
    stack = []  # Initialisation d'une pile pour le parcours en profondeur
    initial_solution = set()  # Initialisation de la solution actuelle (vide)
    stack.append((self, initial_solution))  # Ajout du graphe initial à la pile avec une solution vide

    while stack:  # Boucle principale de l'algorithme
        graph, cover = stack.pop()  # Récupération de l'état actuel du graphe et de la solution

        # Calcul de la borne supérieure (1) dans l'énoncé
        upper_bound = len(self.algo_couplage())

        # Calcul de la borne inférieure basée sur la fonction calculate_lower_bound
        lower_bound = graph.calculate_lower_bound()

        # Vérification de la réalisabilité par rapport à la borne inférieure
        if best_solution is not None and len(cover) >= lower_bound:
            continue  # Élaguer cette branche

        # Vérification de la réalisabilité par rapport à la borne supérieure
        if len(cover) > upper_bound:
            continue  # Élaguer cette branche

        # Vérification si tous les sommets sont couverts ou s'il n'y a plus d'arêtes dans le graphe
        if not graph.V or all(len(value) == 0 for value in graph.E.values()):
            # Si c'est le cas et que la solution actuelle est meilleure que la meilleure solution trouvée
            if best_solution is None or len(cover) < len(best_solution):
                best_solution = cover  # Mettre à jour la meilleure solution

        if best_solution is None or len(cover) < len(best_solution):
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

            # Si les sommets u, v ont été trouvés, on effectue les branchements
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


def branch_and_bound (self) : 
        """ Question 4.2.2 """
        best_solution = self.algo_couplage()
        borne_sup = len(best_solution)
        stack = []  # pile pour gérer les noeuds de l'arbre
        initial_solution = set()  # ensemble de sommets vide pour commencer

        # on commence par ajouter l'état initial (G, C) à la pile
        stack.append((self, initial_solution))
        while stack:
            graphe, couverture = stack.pop()
            borne_inf = graphe.find_borne_inf()
            borne_sup = graphe.algo_couplage()

            if (borne_inf + len(couverture) >= len(best_solution)) :
                continue

            if borne_sup and len(borne_sup) == borne_inf : # si solution optimal (borne_inf)
                if len(borne_sup | couverture) <= len(best_solution): # on vérifie si la solution avec la couverture actuelle fonctionne
                    best_solution = borne_sup | couverture
                continue # on élague

            # si tous les sommets sont couverts, on a une solution potentielle
            if not graphe.V or all(len(value) == 0 for value in graphe.E.values()):
                if best_solution is None or len(couverture) < len(best_solution):
                    best_solution = couverture

            if len(couverture) < len(best_solution):
                # choisir un sommet u et v de l'arête à brancher
                u = -1
                v = -1
                # acceder le premier element d'un somment qui n'est pas isolé
                for key, arets in graphe.E.items():
                    if len(arets) != 0:
                        u = key
                        v = next(iter(graphe.E[key]), None)
                        break

                if u != -1 and v != -1:
                    # branchement avec u dans la couverture
                    new_graphe = copy.deepcopy(graphe)  # créer une copie du graphe
                    new_graphe.remove_vertex(u)  # retirer u du graphe
                    new_couverture = couverture.copy()  # copier l'ensemble couverture
                    new_couverture.add(u)  # ajouter u à la couverture
                    stack.append((new_graphe, new_couverture))

                    # branchement avec v dans la couverture
                    new_graphe = copy.deepcopy(graphe)  # créer une copie du graphe
                    new_graphe.remove_vertex(v)  # retirer v du graphe
                    new_couverture = couverture.copy()  # copier l'ensemble couverture
                    new_couverture.add(v)  # ajouter v à la couverture
                    stack.append((new_graphe, new_couverture))

        return best_solution

