.PHONY: install install-dev test clean build publish docker-run docker-build

# نصب تیزپر
install:
	pip install -e .

# نصب با وابستگی‌های توسعه
install-dev:
	pip install -e ".[dev]"

# اجرای تست‌ها
test:
	pytest -v --tb=short

# تست با پوشش
test-cov:
	pytest --cov=src/tizpar --cov-report=term-missing

# پاکسازی فایل‌های ساختی
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	rm -rf src/*.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

# ساخت پکیج
build: clean
	pip install build
	python -m build

# انتشار روی PyPI
publish: build
	pip install twine
	twine upload dist/*

# اجرای داکر
docker-build:
	docker build -t tizpar:latest .

docker-run:
	docker run --rm tizpar:latest --help

# اجرای لینتر
lint:
	pip install ruff
	ruff check src/tizpar/

# اجرای type checker
typecheck:
	pip install mypy
	mypy src/tizpar/

# نصب وابستگی‌های کامل
deps:
	pip install rich click requests python-dateutil pyyaml pytest pytest-cov ruff mypy
