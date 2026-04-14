"""
normalizer.py – Placeholder for Arabic text normalisation.

TODO: Implement the following normalisation steps:
  - Remove diacritics (tashkeel)
  - Normalise Hamza variants (أ إ آ → ا)
  - Normalise Yaa/Alef Maqsura (ى → ي)
  - Remove tatweel (ـ)
  - Strip punctuation / non-Arabic characters as needed
"""


def normalize(text: str) -> str:
    """Normalise a raw Arabic string.

    Parameters
    ----------
    text : str
        Raw Arabic source text.

    Returns
    -------
    str
        Normalised Arabic text.
    """
    raise NotImplementedError("normalize() is not yet implemented.")
