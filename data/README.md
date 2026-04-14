# Data Directory

This directory holds all datasets used for Arabic–English translation training,
validation, and testing.

## Sub-folders

| Folder       | Description                                                   |
|--------------|---------------------------------------------------------------|
| `raw/`       | Original, unmodified parallel corpora (Arabic ↔ English).    |
| `processed/` | Tokenised, normalised, and vocabulary-encoded data files.     |

## Expected File Format

Parallel corpora should be stored as aligned plain-text pairs:

```
raw/
  train.ar   # Arabic source sentences (one per line)
  train.en   # English target sentences (one per line)
  val.ar
  val.en
  test.ar
  test.en
```

After running the preprocessing pipeline the `processed/` folder will contain
serialised dataset files (e.g. `.pt` tensors or `.json` vocabulary files).
