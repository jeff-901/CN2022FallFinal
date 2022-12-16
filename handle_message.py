from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt
import time

load_dotenv()


def handle_post(request: HttpRequest):
    data = json.loads(request.data)
    other_user = get_user(data.get("name"))
    if len(other_user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    other_user = other_user[0]
    user = jwt.decode(
        request.cookies["token"], os.environ["secret"], algorithms=["HS256"]
    )
    user = get_user(user["username"])
    if len(user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    user = user[0]
    message = {
        "senders": user["username"] + "," + other_user["username"],
        "msg": data.get("msg"),
        "timestamp": int(time.time()),
    }
    create_message(message)
    del message["_id"]
    return wrap_response(
        request.version,
        200,
        {
            "Content-Type": "application/json",
            "Connection": "close",
            "Set-Cookie": "token="
            + jwt.encode(
                {"username": user["username"]}, os.environ["secret"], algorithm="HS256",
            ),
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
        },
        json.dumps(message),
    )


def handle_get(request: HttpRequest):
    other_user_name = request.path[len("/api/messages/") :]
    print("handle message get data: ", request.data)
    other_user = get_user(other_user_name)
    if len(other_user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    other_user = other_user[0]
    user = jwt.decode(
        request.cookies["token"], os.environ["secret"], algorithms=["HS256"]
    )
    user = get_user(user["username"])
    if len(user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    user = user[0]
    msgs = get_messages(user["username"], other_user["username"])
    msgs = sorted(msgs, key=lambda x: x["timestamp"])
    for msg in msgs:
        msg["_id"] = str(msg["_id"])
        # if type(msg["msg"]) == str:
        #     msg["msg"]= json.loads(msg["msg"])
    return wrap_response(
        request.version,
        200,
        {
            "Content-Type": "application/json",
            "Connection": "close",
            "Set-Cookie": "token="
            + jwt.encode(
                {"username": user["username"]}, os.environ["secret"], algorithm="HS256",
            ),
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
        },
        json.dumps(msgs),
    )
