PYTHON = ./venv/bin/python3
PIP = ./venv/bin/pip

.PHONY: all install describe histogram scatter_plot pair_plot train predict clean

all: install

install:
	python3 -m venv venv
	$(PIP) install pandas numpy matplotlib

describe:
	$(PYTHON) describe.py $(ARGS)

histogram:
	$(PYTHON) histogram.py $(ARGS)

scatter_plot:
	$(PYTHON) scatter_plot.py $(ARGS)

pair_plot:
	$(PYTHON) pair_plot.py $(ARGS)

train:
	$(PYTHON) logreg_train.py $(ARGS)

predict:
	$(PYTHON) logreg_predict.py $(ARGS)

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf venv
