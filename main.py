from flask import Flask


app = Flask(__name__)

@app.route("/api/ping")
def ping():
    from actions.ping import action_ping
    res=action_ping()
    return res, 200, {'Content-Type': 'application/json'}

@app.route("/api/network-information")
def network_information():
    from actions.networkInformation import actions_networkInformation
    res = actions_networkInformation()
    return res, 200, {'Content-Type': 'application/json'}

app.run(host="0.0.0.0", port=8000)
