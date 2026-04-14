"""
tokenizer.py – Placeholder for tokenisation and vocabulary construction.

TODO: Implement:
  - Subword tokenisation (e.g. BPE or SentencePiece) for Arabic and English
  - Vocabulary building from training corpus
  - Encoding / decoding helpers (token ↔ integer index)
  - Special token handling: <pad>, <sos>, <eos>, <unk>
"""


class Tokenizer:
    """Tokeniser for Arabic ↔ English translation.

    Parameters
    ----------
    vocab_size : int
        Maximum vocabulary size.
    """

    def __init__(self, vocab_size: int = 32000):
        self.vocab_size = vocab_size
        self.vocab = {}
        raise NotImplementedError("Tokenizer is not yet implemented.")

    def build_vocab(self, corpus: list) -> None:
        """Build vocabulary from a list of sentences.

        Parameters
        ----------
        corpus : list of str
            Training sentences used to derive the vocabulary.
        """
        raise NotImplementedError("build_vocab() is not yet implemented.")

    def encode(self, text: str) -> list:
        """Convert a string into a list of integer token ids.

        Parameters
        ----------
        text : str
            Input sentence.

        Returns
        -------
        list of int
            Token id sequence.
        """
        raise NotImplementedError("encode() is not yet implemented.")

    def decode(self, token_ids: list) -> str:
        """Convert a list of integer token ids back into a string.

        Parameters
        ----------
        token_ids : list of int
            Token id sequence.

        Returns
        -------
        str
            Decoded sentence.
        """
        raise NotImplementedError("decode() is not yet implemented.")
