install:
		poetry install
		poetry add prompt
		poetry add --group dev flake8
start: 
	poetry run brain-games

build:
	 poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games