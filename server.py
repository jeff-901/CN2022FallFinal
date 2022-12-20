import socket
from _thread import *
import threading
from utils import *
import time

from db import *
import handle_session, handle_user, handle_friend, handle_message
import handle_file, handle_v, handle_audio
from dotenv import load_dotenv

load_dotenv()
index_html = None
with open("frontend/dist/index.html", "r") as f:
    index_html = f.read()

# thread function
def threaded(c):
    data = c.recv(4096)
    if not data:
        print("Bye")
    request = parse_request(data)
    print(request)

    if request.path == "/":
        if request.method == "GET":
            c.send(
                wrap_response(
                    request.version,
                    200,
                    {
                        "Content-Type": "text/html",
                        "Connection": "close",
                        "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                        "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                        "Access-Control-Allow-Credentials": "true",
                    },
                    index_html,
                )
            )
    elif request.path[: len("/assets")] == "/assets":
        data = ""
        with open("frontend/dist" + request.path, "r") as f:
            data = f.read()
        file_type = ""
        if request.path[-3:] == ".js":
            file_type = "application/javascript; charset=UTF-8"
        else:
            file_type = "text/css; charset=UTF-8"
        if request.method == "GET":
            c.send(
                wrap_response(
                    request.version,
                    200,
                    {
                        "Content-Type": file_type,
                        "Connection": "close",
                        "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                        "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                        "Access-Control-Allow-Credentials": "true",
                    },
                    data,
                )
            )
    #     else:
    #         c.send(
    #             wrap_response(
    #                 request.version,
    #                 501,
    #                 {
    #                     "Content-Type": "text/html",
    #                     "Connection": "close",
    #                     "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
    #                     "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    #                     "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    #                     "Access-Control-Allow-Credentials": "true",
    #                 },
    #             )
    #         )
    elif request.path == "/api/session":
        if request.method == "POST":
            c.send(handle_session.handle_post(request))
        elif request.method == "GET":
            c.send(handle_session.handle_get(request))
        elif request.method == "DELETE":
            c.send(handle_session.handle_delete(request))
        elif request.method == "OPTIONS":
            c.send(handle_session.handle_option(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path[: len("/api/users")] == "/api/users":
        if request.method == "POST" and request.path == "/api/users":
            c.send(handle_user.handle_post(request))
        elif request.method == "OPTIONS":
            c.send(handle_user.handle_option(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path == "/api/friends":
        if request.method == "POST":
            c.send(handle_friend.handle_post(request))
        elif request.method == "DELETE":
            c.send(handle_friend.handle_delete(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path[: len("/api/messages")] == "/api/messages":
        if request.method == "POST":
            c.send(handle_message.handle_post(request))
        elif request.method == "GET":
            c.send(handle_message.handle_get(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path[: len("/api/files")] == "/api/files":
        if request.method == "POST":
            c.send(handle_file.handle_post(c, request))
        elif request.method == "GET":
            c.send(handle_file.handle_get(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path[: len("/api/video")] == "/api/video":
        if request.method == "GET":
            c.send(handle_v.handle_get(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    elif request.path[: len("/api/audio")] == "/api/audio":
        if request.method == "GET":
            c.send(handle_audio.handle_get(request))
        else:
            c.send(wrap_response(request.version, 501, {"Connection": "close"},))
    else:
        c.send(
            wrap_response(
                request.version,
                404,
                {
                    "Content-Type": "text/html",
                    "Connection": "close",
                    "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                    "Access-Control-Allow-Credentials": "true",
                },
            )
        )
    c.close()


def Main():
    host = ""
    port = int(os.environ["PORT"]) or 5556
    # port = os.environ["PORT"] or 5556
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        c, addr = s.accept()

        print("Connected to :", addr[0], ":", addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
        # time.sleep(10)
        # break
    s.close()


if __name__ == "__main__":
    Main()
