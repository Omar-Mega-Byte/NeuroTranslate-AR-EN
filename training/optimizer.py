"""
optimizer.py – Placeholder for optimizer and learning-rate scheduler setup.

TODO: Implement:
  - Adam / AdamW optimizer construction
  - Transformer warm-up learning-rate schedule (Vaswani et al. 2017):
      lr = d_model^(-0.5) * min(step^(-0.5), step * warmup_steps^(-1.5))
  - Gradient clipping helper
"""


def build_optimizer(model, learning_rate: float = 1e-4, betas=(0.9, 0.98), eps: float = 1e-9):
    """Create an Adam optimizer for the given model.

    Parameters
    ----------
    model
        The Transformer model whose parameters will be optimized.
    learning_rate : float
        Initial learning rate.
    betas : tuple of float
        Adam beta coefficients.
    eps : float
        Adam epsilon for numerical stability.

    Returns
    -------
    Optimizer
        Configured optimizer instance.
    """
    raise NotImplementedError("build_optimizer() is not yet implemented.")


def build_scheduler(optimizer, d_model: int, warmup_steps: int = 4000):
    """Create a Transformer warm-up learning-rate scheduler.

    Implements the schedule from *Attention Is All You Need* (Vaswani et al., 2017):
    ``lr = d_model^(-0.5) * min(step^(-0.5), step * warmup_steps^(-1.5))``

    Parameters
    ----------
    optimizer
        The optimizer whose learning rate will be scheduled.
    d_model : int
        Model dimensionality (used to scale the learning rate).
    warmup_steps : int
        Number of warm-up steps.

    Returns
    -------
    LRScheduler
        Configured scheduler instance.
    """
    raise NotImplementedError("build_scheduler() is not yet implemented.")
