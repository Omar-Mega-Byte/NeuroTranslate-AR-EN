"""
metrics.py – Placeholder for translation quality metrics.

TODO: Implement (or integrate existing libraries for):
  - BLEU score  (e.g. sacrebleu)
  - chrF score
  - TER (Translation Edit Rate)
  - Perplexity
"""


def compute_bleu(hypotheses: list, references: list) -> float:
    """Compute corpus-level BLEU score.

    Parameters
    ----------
    hypotheses : list of str
        Model-generated translations.
    references : list of str
        Ground-truth reference translations.

    Returns
    -------
    float
        BLEU score in the range [0, 100].
    """
    raise NotImplementedError("compute_bleu() is not yet implemented.")


def compute_chrf(hypotheses: list, references: list) -> float:
    """Compute corpus-level chrF score.

    Parameters
    ----------
    hypotheses : list of str
        Model-generated translations.
    references : list of str
        Ground-truth reference translations.

    Returns
    -------
    float
        chrF score in the range [0, 100].
    """
    raise NotImplementedError("compute_chrf() is not yet implemented.")


def compute_perplexity(loss: float) -> float:
    """Compute perplexity from cross-entropy loss.

    Parameters
    ----------
    loss : float
        Average cross-entropy loss per token.

    Returns
    -------
    float
        Model perplexity (exp(loss)).
    """
    raise NotImplementedError("compute_perplexity() is not yet implemented.")
