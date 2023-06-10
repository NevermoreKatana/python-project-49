install:
	poetry install
	poetry shell
brain_game: 
	poetry run brain-games
brain_calc: 
	poetry run brain-calc
brain_even: 
	poetry run brain-even 
brain_nod:
	poetry run brain-gcd
brain_prime:
	poetry run brain-prime
brain_prog:
	poetry run brain-progression

build:
	 poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games
