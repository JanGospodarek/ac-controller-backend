from flask import Flask

from actions.ping import action_ping

app = Flask(__name__)

@app.route("/api/ping")
def ping():
    print('ping called')
    res=action_ping()
    return res, 200, {'Content-Type': 'application/json'}
app.run(host="0.0.0.0", port=8000)
