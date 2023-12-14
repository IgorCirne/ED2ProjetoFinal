import networkx as nx
import osmnx as ox
import matplotlib
import Funções


B = ox.graph_from_place("Gramado, Rio Grande Do Sul, Brazil", network_type="drive")
G = ox.graph_from_place("Gramado, Rio Grande Do Sul, Brazil", network_type="bike")
grafo_diff = Funções.diff_grafos(G, B)

# calculos para centralidade

Funções.centralidade(G)
Funções.centralidade(B)
Funções.centralidade(grafo_diff)

# Outros atributos da rede

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
print(f"Comprimento total das estradas de Gramado: {total_edge_length} metros")

# Desenhando o grafo

ncg = ox.plot.get_node_colors_by_attr(G, "bc", cmap="plasma")
ncb = ox.plot.get_node_colors_by_attr(B, "bc", cmap="plasma")
ncd = ox.plot.get_node_colors_by_attr(grafo_diff, "bc", cmap="plasma")

fig, ax = ox.plot_graph(
    G,
    node_color=ncg,
    node_size=30,
    node_zorder=2,
    edge_linewidth=0.2,
    edge_color="w",
)

fig, ax = ox.plot_graph(
    B,
    node_color=ncb,
    node_size=30,
    node_zorder=2,
    edge_linewidth=0.2,
    edge_color="w",
)


fig, ax = ox.plot_graph(
    grafo_diff,
    node_color="None",
    node_size=0,
    edge_linewidth=0.4,
    edge_color="w",
)

