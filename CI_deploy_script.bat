echo Test Satege ....

echo Unit Tests
echo [{"user":"abcd","pass":"03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"}]>users_list_test.json
python -m coverage run --branch --source=app --omit=app/__init__.py,app/api.py -m pytest --junitxml=result-unit.xml tests/unit
python -m coverage report > coverage_report.txt
pause()
del .\users_list_test.json

echo Security Tests
python -m flake8 --exit-zero --format=pylint --max-line-length 80 app > flake8.out

echo Deploy Stage for API/Rest Integration tests....
dir
set FLASK_APP=app\api.py
start python -m flask --debug run -h localhost -p 3000
pause()

echo Deploy Stage for API/Rest Integration tests....
python -m pytest --junitxml=result-rest.xml tests/integration/api_rest_tests.py
pause()