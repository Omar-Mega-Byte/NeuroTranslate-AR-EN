"""
dataset.py – Placeholder for dataset loading and batching.

TODO: Implement:
  - Load aligned Arabic–English sentence pairs from disk
  - Apply normalisation and tokenisation
  - Pad / truncate sequences to a fixed maximum length
  - Return train / validation / test splits
  - Provide a DataLoader-compatible interface (e.g. torch.utils.data.Dataset)
"""


class TranslationDataset:
    """Dataset wrapper for Arabic–English parallel corpora.

    Parameters
    ----------
    src_path : str
        Path to the Arabic source file (one sentence per line).
    tgt_path : str
        Path to the English target file (one sentence per line).
    max_len : int
        Maximum sequence length (longer sequences will be truncated).
    """

    def __init__(self, src_path: str, tgt_path: str, max_len: int = 128):
        self.src_path = src_path
        self.tgt_path = tgt_path
        self.max_len = max_len
        raise NotImplementedError("TranslationDataset is not yet implemented.")

    def __len__(self) -> int:
        raise NotImplementedError("__len__() is not yet implemented.")

    def __getitem__(self, idx: int):
        raise NotImplementedError("__getitem__() is not yet implemented.")


def build_dataloaders(
    train_src: str,
    train_tgt: str,
    val_src: str,
    val_tgt: str,
    batch_size: int = 32,
    max_len: int = 128,
):
    """Construct train and validation DataLoaders.

    Parameters
    ----------
    train_src, train_tgt : str
        Paths to training source / target files.
    val_src, val_tgt : str
        Paths to validation source / target files.
    batch_size : int
        Mini-batch size.
    max_len : int
        Maximum sequence length.

    Returns
    -------
    tuple
        (train_loader, val_loader)
    """
    raise NotImplementedError("build_dataloaders() is not yet implemented.")
