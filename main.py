from network_topology import initialize_network, simulate_network_changes, draw_graph

def run_simulation():
    network = initialize_network()
    iterations = 5

    for i in range(iterations):
        print(f"--- Iteration {i + 1} ---")

        # Update and exchange routing tables
        for router_id, router in network.items():
            router.update_distance_vector()
            router.exchange_routing_table(network)

        # Print routing tables
        for router_id, router in network.items():
            print(f"Routing table for {router_id}: {router.routing_table}")

        # Visualize the network topology
        draw_graph(network)

        # Simulate a network change in the third iteration
        if i == 2:
            simulate_network_changes(network)
            print("Simulated network changes: Modified link costs.")

if __name__ == "__main__":
    run_simulation()
