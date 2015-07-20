test:
	pip install -e .
	pip install "file://`pwd`#egg=sentry-auth-github[tests]"
	py.test -x
