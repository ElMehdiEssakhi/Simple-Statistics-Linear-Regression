# Linear Regression — Minimal Demo

This is a tiny, single-module linear-regression demo intended for teaching and quick experimentation.

## Big picture

- Purpose: demonstrate simple population-statistics formulas and a least-squares linear fit implemented from scratch.
- Core logic: `relations.py` contains the statistical primitives and linear-regression helper used by the notebook.
- Example runner: `FirstTest.ipynb` loads `data.csv`, computes statistics with `relations.py`, and plots a fitted line using `matplotlib`.

## Key files

- `relations.py` — Implements:
  - `moyenne(x)` — mean
  - `variance(x)` — population variance (division by N)
  - `ecarts_type(x)` — standard deviation
  - `covariance(x, y)` — population covariance
  - `correlation(x, y)` — Pearson correlation using population formulas
  - `a_b(x, y)` — returns `(a, b)` slope and intercept for the regression line

- `FirstTest.ipynb` — Example notebook that:
  - Reads `data.csv` (`pd.read_csv("data.csv")`)
  - Computes and prints statistics
  - Plots the dataset and the regression line

- `data.csv` / `testDATA.csv` — sample datasets used by the notebook.

## What to know (project-specific)

- Population formulas: All variance/covariance calculations use the population denominator (1/N). Do not switch to sample formulas (N-1) unless you intentionally change outputs and docstrings.
- Input expectations: `relations.py` assumes numeric, finite sequence-like inputs (e.g., `pandas.Series` or `numpy.ndarray`). There is no NaN handling or empty-input checking.
- Simple style: The code uses plain Python and built-in operations (e.g., `sum(x)`, `x**2`, `x*y`), so prefer lightweight edits that preserve this style unless adding explicit validation.

## How to run

Prerequisites: a local Python environment with `pandas` and `matplotlib` installed.

Install dependencies (CMD):

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Open the example notebook (recommended):


Then run cells in `FirstTest.ipynb`. The notebook imports `relations.py` directly, so run it from the project root.


## Example snippet

In Python or the notebook:

```python
import pandas as pd
import relations as rl

data = pd.read_csv('data.csv')
x = data['x']
y = data['y']
a, b = rl.a_b(x, y)
print(f"Regression: y = {a} * x + {b}")
```
## License

This project is provided as-is for learning purposes. Use and modify freely.

