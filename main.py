from consensus_protocol import Consensus
from zeno_prevention import ZenoFreeControl
from utils import log_states
from DOS import DoSSimulator
import numpy as np

RED = "\033[31m"
RESET = "\033[0m"
LIGHT_BLUE = "\033[94m"  # Light Blue


time_horizon = 20  
dt = 0.1  
num_nodes = 4  


x = np.random.rand(num_nodes, 1)  
x[-1] = 10  


adjacency_matrix = np.array([
    [0, 1, 0, 0],  
    [0, 0, 1, 0],  
    [0, 0, 0, 1],  
    [0, 0, 0, 0]   
])


dos_intervals = [(5, 7), (12, 14)]  


consensus = Consensus(adjacency_matrix, alpha=0.5, dt=dt)
zeno_control = ZenoFreeControl(sigma=0.1, epsilon=0.05)
dos_simulator = DoSSimulator(dos_intervals)


for t in np.arange(0, time_horizon, dt):
    if not dos_simulator.is_under_attack(t):
        zeno_control.update_consensus(x, consensus, t)
    else:
        consensus.adjust_for_attack(x, t)

    if zeno_control.check_zeno_behavior(x):
        print(f"{RED}Zeno behavior detected{RESET} at time {LIGHT_BLUE}{t:.1f}s{RESET}, adjusting control strategy.")
        zeno_control.adjust_control_strategy(x)
    # _t = f"{t}"

    if t % 1 == 0:
        log_states(t, x)
        # print(f"{_t:<10} Node states = {x.flatten()}")
        input()


print("\nFinal states after simulation:")
for i in range(num_nodes):
    print(f"Node {i+1} state: {x[i][0]}")
