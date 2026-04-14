"""
evaluator.py – Placeholder for the end-to-end evaluation pipeline.

TODO: Implement:
  - Load a trained model from a checkpoint
  - Run inference on the test set
  - Decode output token ids back to text using the target tokeniser
  - Compute and report BLEU, chrF, and any other desired metrics
  - Optionally write predictions to a file for manual inspection
"""


class Evaluator:
    """Runs the full evaluation pipeline on a trained Transformer model.

    Parameters
    ----------
    model
        A trained Transformer model.
    tokenizer
        Target-language tokeniser used for decoding predictions.
    device : str
        Device to run inference on (``"cpu"`` or ``"cuda"``).
    """

    def __init__(self, model, tokenizer, device: str = "cpu"):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        raise NotImplementedError("Evaluator is not yet implemented.")

    def evaluate(self, data_loader) -> dict:
        """Evaluate the model on a dataset and return metric scores.

        Parameters
        ----------
        data_loader
            DataLoader providing (src, tgt) batch pairs from the test split.

        Returns
        -------
        dict
            Dictionary mapping metric names to their scores, e.g.:
            ``{"bleu": 28.4, "chrf": 55.1, "perplexity": 12.3}``.
        """
        raise NotImplementedError("evaluate() is not yet implemented.")

    def translate_batch(self, src_batch) -> list:
        """Translate a batch of source sentences.

        Parameters
        ----------
        src_batch : Tensor
            Source token ids of shape (batch, src_len).

        Returns
        -------
        list of str
            Decoded English translations, one per source sentence.
        """
        raise NotImplementedError("translate_batch() is not yet implemented.")
