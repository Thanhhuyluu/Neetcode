# https://neetcode.io/problems/gradient-descent/question
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        for _ in range(iterations):
            x = x - learning_rate * 2 * x
        return round(x, 5)

solution = Solution()
print(solution.get_minimizer(iterations = 0, learning_rate = 0.01, init = 5))
print(solution.get_minimizer(iterations = 10, learning_rate = 0.01, init = 5))
