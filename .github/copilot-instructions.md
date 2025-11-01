# Copilot instructions for this repository

Purpose: Give a focused summary so an AI coding agent can be immediately productive in this tiny linear-regression project.

- Big picture
  - This repo is a small, single-module linear-regression demo. The core logic lives in `relations.py` and is exercised by the notebook `FirstTest.ipynb` which reads `data.csv`.
  - `relations.py` implements basic statistics and a simple linear regression (slope/intercept) using population formulas (1/N). Expect functions to accept pandas Series or numpy arrays.

- Key files to inspect
  - `relations.py` — core functions: `moyenne`, `variance`, `ecarts_type`, `covariance`, `correlation`, `a_b` (returns slope, intercept). Example: `a, b = rl.a_b(x, y)` where `x` and `y` are pandas Series.
  - `FirstTest.ipynb` — example usage and plots. Cell 2 loads data (`pd.read_csv("data.csv")`); later cells compute statistics via `rl.*` and plot a fitted line with matplotlib.
  - `data.csv` / `testDATA.csv` — sample datasets used by the notebook; tests or validations (when added) should reuse these.

- Project-specific patterns and expectations
  - Numeric input types: functions in `relations.py` rely on sequence operations (`sum(x)`, `x**2`, `x*y`) and `len(x)`. They work with pandas Series or numpy arrays but do not sanitize inputs (no NaN handling, no empty-checks). If adding code, follow the same simple style unless adding explicit validation.
  - Statistical formulas: the code uses population variance and covariance (division by N). Do not switch to sample formulas (N-1) unless you also update docstrings and notebook outputs.
  - No test framework present. If you add tests, keep them minimal and local (e.g., `tests/test_relations.py`, using plain `pytest` conventions) and reference `testDATA.csv` for fixtures.

- Developer workflows (how to run & debug)
  - Interactive: open `FirstTest.ipynb` in Jupyter (Lab/Notebook) and run cells. The notebook imports `relations.py` as `import relations as rl` from the same directory.
  - Quick script check: you can run a small Python REPL from the project folder and run `import relations as rl`, then load data via `pandas.read_csv('data.csv')` and call `rl.a_b(x, y)`.
  - No build system or requirements file present — assume standard Python environment with `pandas` and `matplotlib`. If creating CI, include a minimal `requirements.txt` (pandas, matplotlib, pytest).

- Integration & external dependencies
  - Runtime dependencies: `pandas` (for the notebook) and `matplotlib` (plotting). `relations.py` itself is pure Python and has no external imports.
  - No networked services or external APIs.

- Common quick fixes and what to watch for
  - Division by zero: `variance(x)` can be zero => `a = cov/variance(x)` may raise a `ZeroDivisionError` in float context. Follow existing repo simplicity: either add a guard or raise a clear error with an explanatory message.
  - Input types: code assumes numeric, finite arrays. If you add helpers, convert inputs using `np.asarray` or `pandas.Series` to keep behavior predictable.

- Good first edits for contributors/agents
  - Add basic unit tests for `relations.py` verifying `moyenne`, `variance`, `covariance`, and `a_b` on small arrays (include a case with perfectly correlated data).
  - Add a `requirements.txt` containing `pandas` and `matplotlib` and a short `README.md` with run instructions for the notebook.

- Example snippets (copyable)
  - Compute slope/intercept in REPL or a script:

    >>> import pandas as pd
    >>> import relations as rl
    >>> data = pd.read_csv('data.csv')
    >>> x = data['x']
    >>> y = data['y']
    >>> a, b = rl.a_b(x, y)

  - Note: `rl.correlation(x, y)` uses population formulas and will fail on empty or non-numeric inputs.

If anything important is missing (CI preferences, Python version, or preferred test runner), tell me and I will update this file to include those details.