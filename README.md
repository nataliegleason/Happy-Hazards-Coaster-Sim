confirms controller imports and returns the safe defaults
'python -c "from src.controller import scan, Inputs, State; print(scan(Inputs(), State()))'

run tests
'python -m pytest -v'

test again