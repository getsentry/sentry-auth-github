.PHONY: clean develop install-tests lint publish test

install-pip:
	pip install "pip==19.2.3"

develop: install-pip
	SENTRY_LIGHT_BUILD=1 pip install --no-use-pep517 -e "../sentry[dev]"
	pip install -e .[tests]

ci-install-tests-sentry-git: install-pip
	pip install --no-use-pep517 'git+https://github.com/getsentry/sentry.git#egg=sentry[dev]'
	pip install .[tests]

ci-install-tests-sentry-latest: install-pip
	# Note that requirements-test (setuptools tests_require) is in 9.1.2 but was removed in git.
	pip install --no-use-pep517 'sentry[dev,tests]'
	pip install .[tests]

lint:
	@echo "--> Linting python"
	flake8
	@echo ""

test:
	@echo "--> Running Python tests"
	py.test --cov . tests || exit 1
	@echo ""

publish:
	python setup.py sdist bdist_wheel upload

clean:
	rm -rf *.egg-info src/*.egg-info
	rm -rf dist build
