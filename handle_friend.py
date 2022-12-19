from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt

load_dotenv()


def handle_post(request: HttpRequest):
    data = json.loads(request.data.decode("utf-8"))
    other_user = get_user(data.get("name"))
    if len(other_user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )

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
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    user = user[0]
    user["friends"].append(data.get("name"))
    update_user({"username": user["username"], "friends": user["friends"]})
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
            "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
        },
        json.dumps({"username": user["username"], "friends": user["friends"]}),
    )


def handle_delete(request: HttpRequest):
    data = json.loads(request.data.decode("utf-8"))
    other_user = get_user(data.get("name"))
    if len(other_user) == 0:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "text/html",
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )

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
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    user = user[0]
    user["friends"].remove(data.get("name"))
    update_user({"username": user["username"], "friends": user["friends"]})
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
            "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
        },
        json.dumps({"username": user["username"], "friends": user["friends"]}),
    )
