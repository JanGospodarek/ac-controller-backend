from model.getResponse import GetResponse


def action_ping():
    response = GetResponse(status="success", message="pong", data=None)
    return response.to_dict()