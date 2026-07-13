import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(
        Q: torch.Tensor,
        K: torch.Tensor,
        V: torch.Tensor
) -> torch.Tensor:
    d_k = K.shape[-1]
    scores = torch.matmul(Q, K.transpose(-2,-1))

    scores = scores/ math.sqrt(d_k)
    weights = torch.softmax(scores, dim=-1)  

    result = torch.matmul(weights, V)
    return result

print(scaled_dot_product_attention(Q = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]]), K = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]]), V = torch.tensor([[[1.0, 2.0], [3.0, 4.0]]])))
