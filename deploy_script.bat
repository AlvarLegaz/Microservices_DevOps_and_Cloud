echo Deploy Stage ...
dir
set FLASK_APP=app\api.py
python -m flask --debug run
pause()
