"""
transformer.py – Placeholder for the full Seq2Seq Transformer model.

TODO: Implement:
  - Combine Encoder and Decoder into a single Transformer class
  - Implement greedy / beam-search decoding helpers
  - Optionally share source and target embeddings when vocabularies overlap
"""


class Transformer:
    """Seq2Seq Transformer for Arabic → English machine translation.

    Parameters
    ----------
    src_vocab_size : int
        Source (Arabic) vocabulary size.
    tgt_vocab_size : int
        Target (English) vocabulary size.
    d_model : int
        Model dimensionality.
    num_layers : int
        Number of encoder and decoder layers.
    num_heads : int
        Number of attention heads.
    d_ff : int
        Feed-forward hidden size.
    max_len : int
        Maximum sequence length.
    dropout : float
        Dropout probability.
    """

    def __init__(
        self,
        src_vocab_size: int,
        tgt_vocab_size: int,
        d_model: int = 512,
        num_layers: int = 6,
        num_heads: int = 8,
        d_ff: int = 2048,
        max_len: int = 512,
        dropout: float = 0.1,
    ):
        self.src_vocab_size = src_vocab_size
        self.tgt_vocab_size = tgt_vocab_size
        self.d_model = d_model
        raise NotImplementedError("Transformer is not yet implemented.")

    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        """Run a forward pass through encoder and decoder.

        Parameters
        ----------
        src : Tensor
            Source token ids of shape (batch, src_len).
        tgt : Tensor
            Target token ids of shape (batch, tgt_len).
        src_mask : Tensor or None
            Source padding mask.
        tgt_mask : Tensor or None
            Target causal mask.

        Returns
        -------
        Tensor
            Logits of shape (batch, tgt_len, tgt_vocab_size).
        """
        raise NotImplementedError("forward() is not yet implemented.")

    def translate(self, src, max_len: int = 100, sos_idx: int = 1, eos_idx: int = 2):
        """Translate a single source sequence using greedy decoding.

        Parameters
        ----------
        src : Tensor
            Source token ids of shape (1, src_len).
        max_len : int
            Maximum number of tokens to generate.
        sos_idx : int
            Start-of-sequence token index.
        eos_idx : int
            End-of-sequence token index.

        Returns
        -------
        list of int
            Generated target token id sequence.
        """
        raise NotImplementedError("translate() is not yet implemented.")
