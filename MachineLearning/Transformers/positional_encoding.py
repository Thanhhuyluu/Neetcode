import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    pe = np.zeros((seq_length, d_model))
    for pos in range(seq_length):
        for i in range(0, d_model, 2):
            denominator = 10000 ** ((i) / d_model)
            pe[pos][i] = np.sin(pos/denominator)
            if (i + 1) < d_model:
                pe[pos][i + 1] = np.cos(pos/denominator)
    return pe

print(positional_encoding(3, 5))
