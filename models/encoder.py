"""
encoder.py – Placeholder for the Transformer encoder.

TODO: Implement:
  - Positional encoding (sinusoidal or learned)
  - N stacked encoder layers, each containing:
      * Multi-head self-attention
      * Position-wise feed-forward network
      * Add & Norm (residual connections + layer normalisation)
  - Input embedding + positional encoding
"""


class EncoderLayer:
    """Single Transformer encoder layer.

    Parameters
    ----------
    d_model : int
        Model dimensionality.
    num_heads : int
        Number of attention heads.
    d_ff : int
        Hidden size of the feed-forward sub-layer.
    dropout : float
        Dropout probability.
    """

    def __init__(self, d_model: int, num_heads: int, d_ff: int, dropout: float = 0.1):
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.dropout = dropout
        raise NotImplementedError("EncoderLayer is not yet implemented.")

    def forward(self, src, src_mask=None):
        """Pass input through one encoder layer.

        Parameters
        ----------
        src : Tensor
            Source tensor of shape (batch, src_len, d_model).
        src_mask : Tensor or None
            Optional padding mask.

        Returns
        -------
        Tensor
            Encoded tensor of shape (batch, src_len, d_model).
        """
        raise NotImplementedError("forward() is not yet implemented.")


class Encoder:
    """Transformer encoder stack.

    Parameters
    ----------
    vocab_size : int
        Source vocabulary size.
    d_model : int
        Model dimensionality.
    num_layers : int
        Number of stacked encoder layers.
    num_heads : int
        Number of attention heads.
    d_ff : int
        Feed-forward hidden size.
    max_len : int
        Maximum sequence length for positional encoding.
    dropout : float
        Dropout probability.
    """

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 512,
        num_layers: int = 6,
        num_heads: int = 8,
        d_ff: int = 2048,
        max_len: int = 512,
        dropout: float = 0.1,
    ):
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.num_layers = num_layers
        raise NotImplementedError("Encoder is not yet implemented.")

    def forward(self, src, src_mask=None):
        """Encode a batch of source sequences.

        Parameters
        ----------
        src : Tensor
            Integer token ids of shape (batch, src_len).
        src_mask : Tensor or None
            Optional padding mask.

        Returns
        -------
        Tensor
            Encoder output of shape (batch, src_len, d_model).
        """
        raise NotImplementedError("forward() is not yet implemented.")
