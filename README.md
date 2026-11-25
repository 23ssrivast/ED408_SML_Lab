# ED408 Statistical Machine Learning II Lab

Lab work for ED408. Every question on the lab sheet has its own notebook, `Q1.ipynb` to `Q35.ipynb`.

## What is in this folder

- `Q1.ipynb` to `Q35.ipynb`: one notebook per question, saved with its output
- `Datasets/`: the data files the notebooks read
- `Pretrained/`: ResNet50 weights for Q27 and the MiniLM model for Q28
- `app.py` and `digit_model.joblib`: written by Q33 and used again in Q34
- `Dockerfile` and `.dockerignore`: written by Q34
- `requirements.txt`: packages needed

## Datasets

| Dataset | Used in |
|---|---|
| BSDS500 (Berkeley segmentation images) | Q1 to Q7, Q12, Q15, Q27 |
| pr1002 from TSPLIB | Q9 |
| Bike Sharing, hourly (UCI) | Q11 |
| Pen-Based Recognition of Handwritten Digits (UCI) | Q14, Q17, Q20, Q22, Q26, Q29, Q33, Q34, Q35 |
| Bank Marketing (UCI) | Q16, Q18, Q19, Q21, Q30, Q31 |
| Fashion-MNIST | Q23 |
| Shakespeare text | Q24 |
| AG News | Q28 |
| Jena Climate 2009-2016 | Q32 |

Q8, Q10, Q13 and Q25 do not use a dataset.

## How to run

```
pip install -r requirements.txt
jupyter notebook
```

Start Jupyter from this folder, because the notebooks use relative paths like `Datasets/hour.csv`.

Run Q33 before Q34. Q33 saves the model and writes `app.py`, and Q34 puts both into a Docker image, so Q34 also needs Docker running.
