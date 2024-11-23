class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.neighbors = {}  # Format: {neighbor_id: cost}
        self.distance_vector = {}  # Format: {destination: cost}
        self.routing_table = {}  # Format: {destination: (next_hop, cost)}

    def update_distance_vector(self):
        updated = False
        for dest in self.distance_vector:
            for neighbor, cost in self.neighbors.items():
                if neighbor in self.distance_vector:
                    new_cost = cost + self.distance_vector[neighbor]
                    if new_cost < self.distance_vector[dest]:
                        self.distance_vector[dest] = new_cost
                        self.routing_table[dest] = (neighbor, new_cost)
                        updated = True
        return updated

    def exchange_routing_table(self, network):
        for neighbor in self.neighbors:
            network[neighbor].update_routing_table(self.router_id, self.distance_vector)

    def update_routing_table(self, neighbor_id, received_vector):
        for dest, cost in received_vector.items():
            if dest not in self.distance_vector or cost < self.distance_vector[dest]:
                self.distance_vector[dest] = cost
                self.routing_table[dest] = (neighbor_id, cost)
