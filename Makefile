setup:
	pip install poetry
	poetry install

unittest: setup
	set +e;poetry run pytest; set -e

package: setup
	poetry build

download: setup
	poetry run download