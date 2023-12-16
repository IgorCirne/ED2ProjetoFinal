import networkx as nx
import osmnx as ox
import matplotlib
import Funções


B = ox.graph_from_place("Gramado, Rio Grande do Sul, Brazil", network_type="drive")
G = ox.graph_from_place("Gramado, Rio Grande do Sul, Brazil", network_type="bike")
grafo_diff = Funções.diff_grafos(G, B)

# Atributos da rede

# Número de nós
num_nodes = len(G.nodes)
print(f"Número de nós em Gramado: {num_nodes}")

# Número de arestas
num_edges = len(G.edges)
print(f"Número de ruas em Gramado: {num_edges}")

# Densidade da rede
density = nx.density(G)
print(f"Densidade da rede de estradas de Gramado: {density}")

# Comprimento total das arestas

total_edge_length = sum(nx.get_edge_attributes(G, "length").values())
print(f"Comprimento total das ruas em Gramado: {total_edge_length} metros")

# Desenhando os grafos, primeiro o de estradas, segundo onde pode-se navegar com bicicletas, e por fim, onde somente
# bicicletas podem navegar


fig, ax = ox.plot_graph(B, figsize=(10, 10), node_size=0, edge_color="y", edge_linewidth=0.2)
fig2, ax3 = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_color="y", edge_linewidth=0.2)
fig3, ax3 = ox.plot_graph(grafo_diff, figsize=(10, 10), node_size=0, edge_color="y", edge_linewidth=0.2)

