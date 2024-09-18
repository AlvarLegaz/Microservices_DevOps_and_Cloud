echo Test Script v1.0

echo Executing unitary tests

set PYTHONPATH=.
coverage run --branch --source=app -m pytest --junitxml=tests\results\unit\result-unit.xml tests\unit\tests_security_toolbox.py
coverage html --directory=tests\results\coverage
pause()
