import numpy as np

class ZenoFreeControl:
    def __init__(self, sigma, epsilon):
        self.sigma = sigma  # Event trigger threshold
        self.epsilon = epsilon  # Zeno-free minimum inter-event time
        self.last_trigger_times = None  # To track last trigger times

    def update_consensus(self, x, consensus, t):
        if self.last_trigger_times is None:
            self.last_trigger_times = np.zeros(x.shape[0] - 1)  # For all followers

        control_input = consensus.update(x)

        # Event-triggered control with Zeno-free condition
        for i in range(x.shape[0] - 1):  # Only followers
            error = np.linalg.norm(x[i] - x[-1])  # Error relative to leader
            if error > self.sigma or (t - self.last_trigger_times[i]) > self.epsilon:
                x[i] += consensus.dt * control_input[i]
                self.last_trigger_times[i] = t

    def check_zeno_behavior(self, x):
        # Zeno behavior can be approximated by checking if event-triggered updates are too frequent
        # We'll detect it if a node's state changes too quickly over successive small time steps
        for i in range(x.shape[0] - 1):  # Only check followers
            if np.abs(x[i] - x[-1]) < self.epsilon / 10:  # Threshold condition for Zeno behavior
                return True
        return False

    def adjust_control_strategy(self, x):
        # Adjust control strategy to mitigate Zeno behavior
        print("Adjusting control strategy to prevent Zeno behavior...")
    
        # A simple strategy could be to temporarily increase the event-trigger threshold `sigma`
        self.sigma *= 1.5  # Increase the threshold, making updates less frequent

        # Optionally, reduce the consensus gain alpha to slow down updates
        print("Increasing event-trigger threshold and slowing down consensus rate.\n")
