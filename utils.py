RESET = "\033[0m"
LIGHT_BLUE = "\033[94m"  # Light Blue



def log_states(t, x):
    print(f"Time {LIGHT_BLUE}{t:.2f}{RESET}: Node states = {x.flatten()}")
