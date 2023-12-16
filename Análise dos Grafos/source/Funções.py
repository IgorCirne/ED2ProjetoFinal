import networkx as nx
import osmnx as ox
import matplotlib


def diff_grafos(grafo1, grafo2):
    # Cria uma cópia dos grafos originais para evitar alterações indesejadas
    diff = grafo1.copy()

    # Remove os nós e arestas que estão presentes no segundo grafo
    diff.remove_nodes_from(grafo2.nodes())
    diff.remove_edges_from(grafo2.edges())

    return diff
