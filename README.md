# Streamlit Implementation

## About

This repository contains a Streamlit implementation for Thesis. It demonstrates how to build interactive web applications with Streamlit for data visualization and analysis.

## Requirements

- `python 3.8+`
- `streamlit`
- `pandas`
- `numpy`
- `pygal`

## How to Run

1. Clone the repository:
```bash
git clone <repository-url>
cd elym-streamlit
```

2. Install required packages:
```bash
python -m venv yout-venv-name
source venv/bin/acivqate
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
cd app
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.


## 🔍 Code Quality & Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) with [Ruff](https://docs.astral.sh/ruff/) to automatically enforce code style (PEP8) and catch issues before every commit.

---

### What runs on every commit

| Hook | What it does |
|------|-------------|
| `ruff check` | Lints code, catches PEP8 violations, unused imports, bugs |
| `ruff format` | Auto-formats code (like Black) |
| `trailing-whitespace` | Removes trailing whitespace |
| `end-of-file-fixer` | Ensures files end with a newline |
| `check-yaml` | Validates YAML files |

---


### How to use


**1. Install dependencies**
```bash
pip install pre-commit ruff
```

Or if the project uses a requirements file:
```bash
pip install -r requirements-dev.txt
```

**2. Install the git hooks**
```bash
pre-commit install
```

You should see:
```
pre-commit installed at .git/hooks/pre-commit
```

That's it — the hooks will now run automatically on every `git commit` and if there is any
any check fails. You will receive feedback in the terminal, allowing you to address issues before finalizing your commit.

---

### How it works

#### Automatic (recommended)
Once installed, hooks run automatically when you commit:
```bash
git add .
git commit -m "your message"
# hooks run here — commit is blocked if any check fails
```

If a hook **auto-fixes** something (e.g. formatting), just stage and commit again:
```bash
git add .
git commit -m "your message"
```

#### Manual — run on all files
To check the entire codebase at any time:
```bash
pre-commit run --all-files
```

#### Manual — run a specific hook
```bash
pre-commit run ruff          # lint only
pre-commit run ruff-format   # format only
```

#### Run Ruff directly
```bash
ruff check .              # show all issues
ruff check --fix .        # auto-fix issues
ruff format .             # format all files
```

---

### Skipping hooks (use sparingly)
```bash
git commit --no-verify -m "your message"
```
> ⚠️ Only use this in emergencies. Bypassing hooks may introduce style or lint issues.

---

### Updating hooks
To update all hooks to their latest versions:
```bash
pre-commit autoupdate
```
