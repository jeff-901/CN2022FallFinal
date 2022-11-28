import socket
from _thread import *
import threading
from utils import *
import time

# thread function
def threaded(c):
    data = c.recv(1024)
    if not data:
        print("Bye")
    request = parse_request(data)
    print(request)
    if (request.path == "/"):
        if (request.method == "GET"):
            c.send(
                wrap_response(
                    request.version,
                    200,
                    {"Content-Type": "text/html",
                    "Connection": "close"},
                    "<html><h1>Hello</h1></html>",
                )
            )
        else:
            c.send(
                wrap_response(
                    request.version,
                    501,
                    {"Content-Type": "text/html",
                    "Connection": "close"},
                )
            )
    elif (request.path == "/login"):
        c.send(
            wrap_response(
                request.version,
                200,
                {"Content-Type": "text/html",
                "Connection": "close"},
                "<html><h1>Login</h1></html>",
            )
        )
    else:
        c.send(
            wrap_response(
                request.version,
                501,
                {"Content-Type": "text/html",
                "Connection": "close"},
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
