echo Test Satege ....

echo Unit Tests
echo {"user":"abcd","pass":"1234"}>users_list_test.json
python -m coverage run --branch --source=app --omit=app/__init__.py,app/api.py -m pytest --junitxml=result-unit.xml tests/unit
python -m coverage report > coverage_report.txt
del .\users_list_test.json
pause()

echo Deploy Stage ....
dir
set FLASK_APP=app\api.py
python -m flask --debug run -h localhost -p 3000
pause()
