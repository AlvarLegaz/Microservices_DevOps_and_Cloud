echo Power UP Scrip
dir
set FLASK_APP=app\api.py
python -m flask --debug run
pause()