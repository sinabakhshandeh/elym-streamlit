# Streamlit Implementation

> An interactive web application for data visualization and analysis — built for Thesis.

---

## Requirements

- Python `3.8+`
- `streamlit`
- `pandas`
- `numpy`
- `pygal`

---

## Getting Started

### 1. Clone the repository

```bash
git clone repository-address
cd elym-streamlit
```

### 2. Set up a virtual environment

```bash
python -m venv your-venv-name
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
cd app
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 🐳 Docker

Prefer containers? You can build and run the app with Docker or Docker Compose — no local Python setup required.

### Using Docker

**Build the image:**

```bash
docker build -t elym-streamlit .
```

**Run the container:**

```bash
docker run -p 8501:8501 elym-streamlit
```

The app will be available at `http://localhost:8501`.

### Using Docker Compose

For a one-command setup, use Docker Compose:

```bash
docker compose up --build
```

To run in detached (background) mode:

```bash
docker compose up --build -d
```

To stop the containers:

```bash
docker compose down
```


---

## 🔍 Code Quality & Pre-commit Hooks (Optional)

This project uses [pre-commit](https://pre-commit.com/) with [Ruff](https://docs.astral.sh/ruff/) to enforce code style (PEP 8) and catch issues before every commit.

### What runs on every commit

| Hook | What it does |
|------|-------------|
| `ruff check` | Lints code, catches PEP 8 violations, unused imports, bugs |
| `ruff format` | Auto-formats code (like Black) |
| `trailing-whitespace` | Removes trailing whitespace |
| `end-of-file-fixer` | Ensures files end with a newline |
| `check-yaml` | Validates YAML files |

---

### Setup

**1. Install dependencies**

```bash
pip install pre-commit ruff
# or, if using a dev requirements file:
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

That's it — hooks will now run automatically on every `git commit`.

---

### Usage

#### Automatic (recommended)

Hooks run automatically when you commit:

```bash
git add .
git commit -m "your message"
# hooks run here — commit is blocked if any check fails
```

If a hook auto-fixes something (e.g. formatting), just stage and commit again:

```bash
git add .
git commit -m "your message"
```

#### Manual — run on all files

```bash
pre-commit run --all-files
```

#### Manual — run a specific hook

```bash
pre-commit run ruff           # lint only
pre-commit run ruff-format    # format only
```

#### Run Ruff directly

```bash
ruff check .          # show all issues
ruff check --fix .    # auto-fix issues
ruff format .         # format all files
```

---

### Skipping hooks

```bash
git commit --no-verify -m "your message"
```

> ⚠️ Use sparingly. Bypassing hooks may introduce style or lint issues.

---

### Updating hooks

```bash
pre-commit autoupdate
```
