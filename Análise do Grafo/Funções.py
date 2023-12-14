def diferenca_grafos(grafo1, grafo2):
    # Cria uma cópia dos grafos originais para evitar alterações indesejadas
    diferenca = grafo1.copy()

    # Remove os nós e arestas que estão presentes no segundo grafo
    diferenca.remove_nodes_from(grafo2.nodes())
    diferenca.remove_edges_from(grafo2.edges())

    return diferenca