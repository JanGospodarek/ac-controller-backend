import socket
from model.getResponse import GetResponse

def actions_networkInformation():


    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except Exception:
        local_ip = None

    data = {
        "ipAddress": local_ip
    }
    response = GetResponse(status="success", message="", data=data)
    return response.to_dict()