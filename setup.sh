kill $(pgrep -f flask)
export FLASK_APP=flask_server.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
