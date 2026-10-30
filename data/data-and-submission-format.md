# Data and Submission Format

## Data Release

| Dataset | Release Date | Ground Truth Public Release | Number of Words | Definitions for Subtask 2 | Languages | Download |
| --- | --- | --- | ---: | --- | --- | --- |
| Sample Data | 18/08/2026 | NO | 2 | YES | SV | [LINK](https://www.codabench.org/datasets/download/id/934357/) |
| Development Data | 08/09/2026 | YES | 10 | YES | SV | [LINK](https://www.codabench.org/datasets/download/568b0ea8-3490-4b1b-ac87-5b3cf03570c0/) |
| Evaluation Data – Subtask 1 | 10/01/2027 | NO | 132 | NO | EN, SV, IT, ES, NL, RU | --- |
| Evaluation Data – Subtask 2 | 21/01/2027 | NO | 132 | YES | EN, SV, IT, ES, NL, RU | --- |

**Both Subtask 1 and Subtask 2 are designed to be unsupervised. However, in September 2026, we will provide 10 Swedish words that participants may use to tune the parameters of their models. We therefore encourage participants to explore other existing datasets. For example, a synthetic English dataset is available [HERE](https://zenodo.org/records/21703081) and can be used to train and/or test their models.**

## Data Format

We provide a ZIP archive containing the data. The archive includes a separate folder for each language (EN, SV, IT, ES, NL, RU). Each folder contains two files: `raw/development-swedish/usages.jsonl` and `definitions.jsonl`.

### `raw/development-swedish/usages.jsonl`

This file contains the usages of the target words in context. Each line is a JSON object representing one occurrence of a target word.

Each object contains:

- **target word** - the target word;
- **sentence** - the sentence in which the target word occurs;
- **sentence ID** - a unique identifier for the sentence;
- **start** - the starting character offset of the target word in the sentence;
- **end** - the ending character offset of the target word in the sentence;
- **year** - the year from which the sentence originates;
- **period label** - the time period to which the sentence belongs.

Individual years are aggregated into periods. A target word may contain data from **up to 10 time points**. **Warning:** **The evaluation is based on the periods defined by `period_label`**, not on individual years. Occurrences are aggregated according to `period_label`. The `year` field is provided as metadata only.

### `raw/development-swedish/definitions.jsonl`

This file contains the sense definitions used for **Subtask 2**.

For each target word, the file provides the definition of the specific sense that participants are asked to track over time.

There is **exactly one sense per target word** that should be tracked across all usages.

## Submission Format

An example submission for the sample data can be download [HERE](https://www.codabench.org/datasets/download/id/936979/)

### Example of a valid **Subtask 1** submission

Each line contains:

- the **target word**;
- the **sentence ID**;
- the predicted **label**.

The label must always be a **list** of **integers**.

If a system predicts only one sense per sentence, the sense identifier must still be wrapped in a list.

For example:

```json
{"word": "...", "sentence_id": "...", "label": ["..."]}
```

### Example of a valid **Subtask 2** submission

Each line contains:

- the **target word**;
- the **sentence ID**;
- the predicted **label**.

The label must be an integer and must be either `0` or `1`. Where `1` indicates that the target word meaning in the given sentence match the meaning provided in the `definition.jsonl` file, and `0` otherwise.

For example:

```json
{"word": "...", "sentence_id": "...", "label": 1}
```

## Development data

The development data is available from this Codabench competition as `dev.zip`.

After registering for the competition, participants can download it from the competition files/public data section.
