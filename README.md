# mygeopy

Tiny geometry helpers.

## Dev setup

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
python -m pip install --upgrade pip
pip install -U pytest
pip install -e .
## Run tests
pytest
pytest --doctest-modules
