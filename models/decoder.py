"""
decoder.py – Placeholder for the Transformer decoder.

TODO: Implement:
  - N stacked decoder layers, each containing:
      * Masked multi-head self-attention (causal mask)
      * Multi-head cross-attention over encoder output
      * Position-wise feed-forward network
      * Add & Norm (residual connections + layer normalisation)
  - Output embedding + positional encoding
  - Final linear projection + softmax to produce token probabilities
"""


class DecoderLayer:
    """Single Transformer decoder layer.

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
        raise NotImplementedError("DecoderLayer is not yet implemented.")

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None):
        """Pass input through one decoder layer.

        Parameters
        ----------
        tgt : Tensor
            Target tensor of shape (batch, tgt_len, d_model).
        memory : Tensor
            Encoder output of shape (batch, src_len, d_model).
        tgt_mask : Tensor or None
            Causal (look-ahead) mask.
        memory_mask : Tensor or None
            Encoder padding mask.

        Returns
        -------
        Tensor
            Decoded tensor of shape (batch, tgt_len, d_model).
        """
        raise NotImplementedError("forward() is not yet implemented.")


class Decoder:
    """Transformer decoder stack.

    Parameters
    ----------
    vocab_size : int
        Target vocabulary size.
    d_model : int
        Model dimensionality.
    num_layers : int
        Number of stacked decoder layers.
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
        raise NotImplementedError("Decoder is not yet implemented.")

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None):
        """Decode a batch of target sequences.

        Parameters
        ----------
        tgt : Tensor
            Integer token ids of shape (batch, tgt_len).
        memory : Tensor
            Encoder output of shape (batch, src_len, d_model).
        tgt_mask : Tensor or None
            Causal mask.
        memory_mask : Tensor or None
            Encoder padding mask.

        Returns
        -------
        Tensor
            Logits of shape (batch, tgt_len, vocab_size).
        """
        raise NotImplementedError("forward() is not yet implemented.")
