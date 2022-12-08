import socket
from _thread import *
import threading
from utils import *
import time

from db import *
import handle_session, handle_user, handle_friend, handle_message

# thread function
def threaded(c):
    data = c.recv(1024)
    if not data:
        print("Bye")
    request = parse_request(data)
    print(request)

    # if request.path == "/":
    #     if request.method == "GET":
    #         c.send(
    #             wrap_response(
    #                 request.version,
    #                 200,
    #                 {
    #                     "Content-Type": "text/html",
    #                     "Connection": "close",
    #                     "Access-Control-Allow-Origin": "http://localhost:3000",
    #                     "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    #                     "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    #                     "Access-Control-Allow-Credentials": "true",
    #                 },
    #                 "<html><h1>Hello</h1></html>",
    #             )
    #         )
    #     else:
    #         c.send(
    #             wrap_response(
    #                 request.version,
    #                 501,
    #                 {
    #                     "Content-Type": "text/html",
    #                     "Connection": "close",
    #                     "Access-Control-Allow-Origin": "http://localhost:3000",
    #                     "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    #                     "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    #                     "Access-Control-Allow-Credentials": "true",
    #                 },
    #             )
    #         )
    if request.path == "/api/session":
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
    else:
        c.send(
            wrap_response(
                request.version,
                501,
                {
                    "Content-Type": "text/html",
                    "Connection": "close",
                    "Access-Control-Allow-Origin": "http://localhost:3000",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                    "Access-Control-Allow-Credentials": "true",
                },
            )
        )
    c.close()


def Main():
    host = ""
    port = 5556
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
