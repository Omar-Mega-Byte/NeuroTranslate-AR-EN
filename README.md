# NeuroTranslate-AR-EN

A Transformer-based neural machine translation system for Arabic → English,
trained on parallel text data and designed to capture contextual and semantic
relationships using attention mechanisms.

This project implements a Seq2Seq Transformer model (encoder–decoder with
multi-head attention) for Arabic → English translation.

---

## Project Structure

```
NeuroTranslate-AR-EN/
├── data/
│   ├── raw/            # Original parallel corpora (*.ar / *.en files)
│   ├── processed/      # Tokenised & encoded datasets produced by preprocessing
│   └── README.md       # Data format and usage notes
│
├── preprocessing/
│   ├── __init__.py
│   ├── normalizer.py   # Arabic text normalisation (diacritics, Hamza, …)
│   ├── tokenizer.py    # Subword tokenisation & vocabulary construction
│   └── dataset.py      # Dataset loading, batching, and DataLoader helpers
│
├── models/
│   ├── __init__.py
│   ├── attention.py    # Scaled dot-product & multi-head attention
│   ├── encoder.py      # Transformer encoder stack
│   ├── decoder.py      # Transformer decoder stack
│   └── transformer.py  # Full Seq2Seq Transformer model
│
├── training/
│   ├── __init__.py
│   ├── config.py       # Hyperparameters and path configuration
│   ├── optimizer.py    # Optimizer & warm-up LR scheduler
│   └── trainer.py      # Training / validation loop & checkpointing
│
├── evaluation/
│   ├── __init__.py
│   ├── metrics.py      # BLEU, chrF, perplexity
│   └── evaluator.py    # End-to-end evaluation pipeline
│
├── requirements.txt    # Python dependencies
└── README.md
```

> **Note:** All modules currently contain **placeholder classes and functions**
> that raise `NotImplementedError`. They serve as a roadmap for implementation.

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare data

Place aligned source/target files in `data/raw/`:

```
data/raw/train.ar  data/raw/train.en
data/raw/val.ar    data/raw/val.en
data/raw/test.ar   data/raw/test.en
```

### 3. Preprocess

```bash
# TODO: run preprocessing pipeline once implemented
python -m preprocessing.tokenizer
```

### 4. Train

```bash
# TODO: run training once implemented
python -m training.trainer
```

### 5. Evaluate

```bash
# TODO: run evaluation once implemented
python -m evaluation.evaluator
```

---

## Roadmap

- [ ] Implement Arabic text normalisation (`preprocessing/normalizer.py`)
- [ ] Implement subword tokeniser (`preprocessing/tokenizer.py`)
- [ ] Implement dataset loader (`preprocessing/dataset.py`)
- [ ] Implement multi-head attention (`models/attention.py`)
- [ ] Implement encoder & decoder (`models/encoder.py`, `models/decoder.py`)
- [ ] Implement full Transformer model (`models/transformer.py`)
- [ ] Implement training loop (`training/trainer.py`)
- [ ] Implement evaluation pipeline (`evaluation/evaluator.py`)

---

## License

See [LICENSE](LICENSE).
