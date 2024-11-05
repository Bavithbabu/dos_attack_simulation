class DoSSimulator:
    def __init__(self, dos_intervals):
        self.dos_intervals = dos_intervals

    def is_under_attack(self, t):
        for interval in self.dos_intervals:
            if interval[0] <= t < interval[1]:
                return True
        return False
