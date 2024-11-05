
import numpy as np

class Consensus:
    def __init__(self, adjacency_matrix, alpha, dt):
        self.num_nodes = adjacency_matrix.shape[0]
        self.alpha = alpha
        self.dt = dt
        self.laplacian_matrix = self.compute_laplacian(adjacency_matrix)

    def compute_laplacian(self, adjacency_matrix):
        degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))
        return degree_matrix - adjacency_matrix

    def update(self, x):
        control_input = np.zeros_like(x)
        for i in range(self.num_nodes - 1):  # Update only for followers
            control_input[i] = -self.alpha * np.dot(self.laplacian_matrix[i, :], x).item()
        return control_input

    def adjust_for_attack(self, x, t):
        # During a DoS attack, we may want to freeze the states of the nodes
        print(f"DoS attack detected at time {t:.1f}, halting updates.")

        
        # Simulate stopping state updates by freezing follower nodes
        # This could simulate failure in communication caused by the attack.
        for i in range(x.shape[0] - 1):  # Only freeze followers
            x[i] = x[i]  # Keep the state unchanged
