install:
		poetry install
		poetry add prompt
start: 
	poetry run brain-games

build:
	 poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl