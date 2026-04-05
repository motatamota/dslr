PYTHON = python3
PIP = pip3
SCRIPT = dslr.py

.PHONY: all install run debug lint test clean

all: install

install:
	$(PIP) install pandas numpy matplotlib

run:
	$(PYTHON) $(SCRIPT)

debug:
	$(PYTHON) -m pdb $(SCRIPT)

lint:
	$(PIP) install --quiet flake8
	flake8 *.py

test:
	$(PYTHON) -m pytest

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
