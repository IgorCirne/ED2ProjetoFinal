import networkx as nx
import osmnx as ox
import matplotlib
import Funções




#B = ox.graph_from_place("Pipa, Tibau do Sul, Brazil", network_type="drive")
G = ox.graph_from_place("Natal, Brazil", network_type="bike")
#grafo_diferenca = Funções.diferenca_grafos(G, B)

# calculos para centralidade

bc = nx.betweenness_centrality(ox.get_digraph(G), weight="length")
max_node, max_bc = max(bc.items(), key=lambda x: x[1])
max_node, max_bc
nx.set_node_attributes(G, bc, "bc")
nc = ox.plot.get_node_colors_by_attr(G, "bc", cmap="plasma")


fig, ax = ox.plot_graph(
    G,
    node_color=nc,
    node_size=30,
    node_zorder=2,
    edge_linewidth=0.2,
    edge_color="w",
)

#fig, ax = ox.plot_graph(G)
