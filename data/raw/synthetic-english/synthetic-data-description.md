This repository contains the synthetic dataset introduced in *Generating Synthetic Data for Lexical Semantic Change Detection Over Multiple Time Periods .*

The dataset provides sense-annotated historical sentences together with the metadata used to generate them, enabling controlled evaluation of lexical semantic change detection (LSCD) methods across multiple historical time periods. This resource contains explicit sense distributions over a sequence of time slices from 1810 to 1990 (20-year intervals).

The dataset is organized into two archives:

**`metadata.zip`**

Contains one JSON file per target lemma, organized by the number of senses:

```text
metadata.zip/
├── 2_senses/
├── 3_senses/
├── 4_senses/
└── ...
```

Each file (`<lemma>.json`) contains one entry for every sense of the lemma. For each sense, the following information is provided:

- **sense_id**: unique identifier of the OED sense
- **start - end**: first and last attested years of the sense
- **tier**: assigned frequency tier (Top, Mid, or Low)
- **probability_from_proxy**: estimated prior probability derived from a SemCor proxy
- **semcor_proxy_word**: SemCor lemma used to estimate the sense-frequency distribution
- **timeseries_word**: CCOHA proxy word whose historical frequency profile models the temporal evolution of the sense
- **frequencies**: proxy word frequencies for each 20-year time period
- **log2_frequencies**: log-transformed frequencies used during normalization

**`sentences.zip`**

Contains newline-delimited JSON (JSONL) files with the generated historical sentences, organized using the same directory structure:

```text
sentences.zip/
├── 2_senses/
├── 3_senses/
├── 4_senses/
└── ...
```

Each line represents one generated sentence with the following fields:

- **lemma**: target lemma
- **sense_id**: OED sense used during generation
- **start - end**: character offsets of the target word
- **pos**: part-of-speech tag
- **year**: target historical period
- **text**: generated historical sentence

**Intended use**

The dataset is intended for:

- benchmarking lexical semantic change detection methods;
- evaluating contextual embedding models across multiple historical periods;
- developing and calibrating clustering and sense induction approaches;