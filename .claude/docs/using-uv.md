### uv Field Manual (Code‑Gen Ready, Bootstrap‑free)

*Assumption: `uv` is already installed and available on `PATH`.*

---

## 0 — Sanity Check

```bash
uv --version               # verify installation; exits 0
```

If the command fails, halt and report to the user.

---

## 1 — Daily Workflows

### 1.1 Project ("cargo‑style") Flow

```bash
uv init myproj                     # ① create pyproject.toml + .venv
cd myproj
uv add ruff pytest httpx           # ② fast resolver + lock update
uv run pytest -q                   # ③ run tests in project venv
uv lock                            # ④ refresh uv.lock (if needed)
uv sync --locked                   # ⑤ reproducible install (CI‑safe)
```

### 1.2 Script‑Centric Flow (PEP 723)

```bash
echo 'print("hi")' > hello.py
uv run hello.py                    # zero‑dep script, auto‑env
uv add --script hello.py rich      # embeds dep metadata
uv run --with rich hello.py        # transient deps, no state
```

### 1.3 CLI Tools (pipx Replacement)

```bash
uvx ruff check .                   # ephemeral run
uv tool install ruff               # user‑wide persistent install
uv tool list                       # audit installed CLIs
uv tool update --all               # keep them fresh
```

### 1.4 Python Version Management

```bash
uv python install 3.10 3.11 3.12
uv python pin 3.12                 # writes .python-version
uv run --python 3.10 script.py
```

### 1.5 Legacy Pip Interface

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv pip sync   -r requirements.txt   # deterministic install
```
