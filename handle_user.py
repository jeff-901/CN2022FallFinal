import json
from utils import *
from db import *
import jwt
import os
from dotenv import load_dotenv

load_dotenv()


def handle_post(request):
    try:
        user = json.loads(request.data.decode("utf-8"))
        if "username" not in user or "password" not in user:
            return wrap_response(
                request.version, 200, {}, "Data must contain username and password"
            )
        if len(get_user(user["username"])) != 0:
            return wrap_response(
                request.version,
                502,
                {
                    "Content-Type": "application/json",
                    "Connection": "close",
                    "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                    "Access-Control-Allow-Credentials": "true",
                    "Set-Cookie": "token="
                    + jwt.encode(
                        {"username": user["username"]},
                        os.environ["secret"],
                        algorithm="HS256",
                    ),
                },
                json.dumps({"message": "Already exist"}),
            )
        user["friends"] = []
        user_obj = create_user(user)
        return wrap_response(
            request.version,
            200,
            {
                "Content-Type": "application/json",
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
                "Set-Cookie": "token="
                + jwt.encode(
                    {"username": user["username"]},
                    os.environ["secret"],
                    algorithm="HS256",
                ),
            },
            json.dumps({"username": user["username"], "friends": []}),
        )

    except Exception as e:
        print(e)
        return wrap_response(
            request.version,
            502,
            {},
            "Data format must be json. It contains username and password",
        )


def handle_option(request):
    return wrap_response(
        request.version,
        200,
        {
            "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Cookie, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Max-Age": 86400,
            "Connection": "keep-alive",
        },
        "success",
    )
