import networkx as nx
import osmnx as ox
import matplotlib


def diff_grafos(grafo1, grafo2):
    # Cria uma cópia dos grafos originais para evitar alterações indesejadas
    difff = grafo1.copy()

    # Remove os nós e arestas que estão presentes no segundo grafo
    difff.remove_nodes_from(grafo2.nodes())
    difff.remove_edges_from(grafo2.edges())

    return difff

def centralidade(A):
    bc = nx.betweenness_centrality(ox.get_digraph(A), weight="length")
    max_node, max_bc = max(bc.items(), key=lambda x: x[1])
    max_node, max_bc
    nx.set_node_attributes(A, bc, "bc")
