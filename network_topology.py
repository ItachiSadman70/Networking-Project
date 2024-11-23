from router import Router
import networkx as nx
import matplotlib.pyplot as plt

def initialize_network():
    # Create routers
    router_a = Router('A')
    router_b = Router('B')
    router_c = Router('C')
    router_d = Router('D')

    # Define neighbors and link costs
    router_a.neighbors = {'B': 1, 'C': 4}
    router_b.neighbors = {'A': 1, 'C': 2, 'D': 7}
    router_c.neighbors = {'A': 4, 'B': 2, 'D': 3}
    router_d.neighbors = {'B': 7, 'C': 3}

    # Initialize distance vectors
    for router in [router_a, router_b, router_c, router_d]:
        for neighbor in router.neighbors:
            router.distance_vector[neighbor] = router.neighbors[neighbor]
        router.distance_vector[router.router_id] = 0

    return {'A': router_a, 'B': router_b, 'C': router_c, 'D': router_d}

def simulate_network_changes(network):
    # Example: Modify the cost of the link between B and C
    network['B'].neighbors['C'] = 5
    network['C'].neighbors['B'] = 5

def draw_graph(network):
    G = nx.Graph()

    # Add nodes and edges to the graph
    for router_id, router in network.items():
        G.add_node(router_id)
        for neighbor, cost in router.neighbors.items():
            G.add_edge(router_id, neighbor, weight=cost)

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for better visualization
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    plt.title("Network Topology with Link Costs")
    plt.show()
