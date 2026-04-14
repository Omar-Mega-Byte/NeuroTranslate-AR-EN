"""
config.py – Hyperparameter and path configuration for training.

All training-relevant settings live here so that experiments can be reproduced
by simply modifying this file or passing overrides from the command line.

TODO: Replace hard-coded defaults with a proper config system (e.g. YAML,
      argparse, or Hydra) as the project matures.
"""

# ---------------------------------------------------------------------------
# Data paths
# ---------------------------------------------------------------------------
TRAIN_SRC = "data/raw/train.ar"
TRAIN_TGT = "data/raw/train.en"
VAL_SRC = "data/raw/val.ar"
VAL_TGT = "data/raw/val.en"
TEST_SRC = "data/raw/test.ar"
TEST_TGT = "data/raw/test.en"

PROCESSED_DIR = "data/processed"

# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------
SRC_VOCAB_SIZE = 32000
TGT_VOCAB_SIZE = 32000

# ---------------------------------------------------------------------------
# Model architecture
# ---------------------------------------------------------------------------
D_MODEL = 512
NUM_LAYERS = 6
NUM_HEADS = 8
D_FF = 2048
MAX_LEN = 512
DROPOUT = 0.1

# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------
BATCH_SIZE = 32
NUM_EPOCHS = 20
LEARNING_RATE = 1e-4
WARMUP_STEPS = 4000
LABEL_SMOOTHING = 0.1
CLIP_GRAD_NORM = 1.0

# ---------------------------------------------------------------------------
# Checkpointing
# ---------------------------------------------------------------------------
CHECKPOINT_DIR = "checkpoints"
SAVE_EVERY_N_EPOCHS = 1
KEEP_LAST_N_CHECKPOINTS = 3

# ---------------------------------------------------------------------------
# Misc
# ---------------------------------------------------------------------------
SEED = 42
DEVICE = "cuda"  # "cpu" or "cuda"
LOG_EVERY_N_STEPS = 100
