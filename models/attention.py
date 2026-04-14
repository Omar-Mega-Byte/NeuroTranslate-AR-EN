"""
attention.py – Placeholder for attention mechanism implementations.

TODO: Implement:
  - Scaled dot-product attention
  - Multi-head attention (split Q/K/V across heads, concat + project)
  - Optional: relative positional encodings
"""


class MultiHeadAttention:
    """Multi-head attention module.

    Parameters
    ----------
    d_model : int
        Model dimensionality.
    num_heads : int
        Number of attention heads.
    dropout : float
        Dropout probability applied to attention weights.
    """

    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1):
        self.d_model = d_model
        self.num_heads = num_heads
        self.dropout = dropout
        raise NotImplementedError("MultiHeadAttention is not yet implemented.")

    def forward(self, query, key, value, mask=None):
        """Compute multi-head attention.

        Parameters
        ----------
        query, key, value : Tensor
            Input tensors of shape (batch, seq_len, d_model).
        mask : Tensor or None
            Optional boolean mask.

        Returns
        -------
        Tensor
            Attention output of shape (batch, seq_len, d_model).
        """
        raise NotImplementedError("forward() is not yet implemented.")
