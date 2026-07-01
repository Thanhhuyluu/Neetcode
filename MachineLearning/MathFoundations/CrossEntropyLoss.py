import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        y_true = np.array(y_true, dtype=np.float64)
        y_pred = np.array(y_pred, dtype=np.float64)

        epsilon = 1e-7
        n = len(y_true)
        loss = - 1 / n * sum( y_true * np.log(y_pred + epsilon) + (1-y_true) * np.log(1-y_pred))
        return np.round(loss, 4)
        
    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        y_true = np.array(y_true, dtype=np.float64)
        y_pred = np.array(y_pred, dtype=np.float64)

        n = len(y_true)
        epsilon = 1e-7
        loss = -1/n * (sum(sum(y_true * np.log(y_pred + epsilon))))
        return np.round(loss, 4)
solution = Solution()
print(solution.binary_cross_entropy(y_true = [1, 0, 1], y_pred = [0.9, 0.1, 0.8]))
print(solution.categorical_cross_entropy(y_true = [[1,0,0], [0,1,0]], y_pred = [[0.9,0.05,0.05], [0.1,0.8,0.1]]))
print(np.log(0.8), np.log(0.1))
