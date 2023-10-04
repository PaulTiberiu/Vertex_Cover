import Graph as gr

sommet = {0, 3, 6, 8, 10, 14}
arrete = {0 : {6, 3, 8}, 3 : {0,6}, 6 : {8, 0, 14, 10, 6}, 8 : {6}}
graph = gr.Graph(sommet, arrete)
# graph.add_edge(0, 3)
# graph.add_edge(0, 6)
# graph.add_edge(6, 8)
# graph.add_edge(6, 3)
print("Graphe original:")
print(graph.V)
print("___________________")
print(graph.E)
print("___________________")

dico = graph.nombre_degre()
print(f'dico : {dico}')
print("___________________")
print(f'Le degré max est : {graph.max_degre()}' )


# v_to_remove = {3, 0, 4, 5, 9}
# graph.remove_many_vertex(v_to_remove)
# print("\nGraphe aprÃ¨s suppression du sommet", v_to_remove, ":"
#print(graph)