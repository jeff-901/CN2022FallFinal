import json
from utils import *
from db import *
import jwt
import os
from dotenv import load_dotenv
load_dotenv()


def handle_post(request):
    data = json.loads(request.data)
    user = get_user(data.get("username"))
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
    else:
        if user[0]["password"] != data.get("password"):
            return wrap_response(
                request.version,
                200,
                {
                    "Content-Type": "application/json",
                    "Connection": "close",
                    "Access-Control-Allow-Origin": "http://localhost:3000",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                    "Access-Control-Allow-Credentials": "true",
                },
                "Password is not correct",
            )
        else:
            return wrap_response(
                request.version,
                200,
                {
                    "Content-Type": "application/json",
                    "Connection": "close",
                    "Set-Cookie": "token="
                    + jwt.encode(
                        {"username": user[0]["username"]}, os.environ["secret"], algorithm="HS256",
                    ),
                    "Access-Control-Allow-Origin": "http://localhost:3000",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                    "Access-Control-Allow-Credentials": "true",
                },
                json.dumps({"username": user[0]["username"]}),
            )


def handle_get(request):
    if "token" not in request.cookies:
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
    try:
        data = jwt.decode(request.cookies["token"], os.environ["secret"], algorithms=["HS256"])
    except:
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
    username = data["username"]
    user = get_user(username)
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
    else:
        return wrap_response(
            request.version,
            200,
            {
                "Content-Type": "application/json",
                "Connection": "close",
                "Access-Control-Allow-Origin": "http://localhost:3000",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
            json.dumps({"username": user[0]["username"]}),
        )


def handle_delete(request):
    return wrap_response(
        request.version,
        200,
        {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": 86400,
            "Set-Cookie": "token=''",
            "Connection": "keep-alive",
        },
        "success",
    )


def handle_option(request):
    return wrap_response(
        request.version,
        200,
        {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": 86400,
            "Connection": "keep-alive",
        },
        "success",
    )
