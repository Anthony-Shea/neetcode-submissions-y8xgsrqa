class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for i in range(iterations):
            init = round(init - (init*2 * learning_rate),6)
        return round(init,5)