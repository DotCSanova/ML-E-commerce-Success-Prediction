# Makefile for ML E-commerce Success Prediction
install:
	pip install -e .[dev]

lint:
	black src/ tests/
	isort src/ tests/

format:
	black src/ tests/
	isort src/ tests/

test:
	pytest tests/

run:
	uvicorn src.api.main:app --reload
