from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt
import time

load_dotenv()


def handle_post(request: HttpRequest):
    filename = request.path[len("/api/files/?file=") :]
    print(type(request.data))
    file_meta = create_file(filename, request.data.encode("utf-8"))
    # file_meta["_id"] = str(file_meta["_id"])
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
        json.dumps({"id": file_meta}),
    )


def handle_post_uu(request: HttpRequest):
    data = json.loads(request.data)
    other_user = get_user(data.get("name"))
    # if len(other_user) == 0:
    #     return wrap_response(
    #         request.version,
    #         404,
    #         {
    #             "Content-Type": "text/html",
    #             "Connection": "close",
    #             "Access-Control-Allow-Origin": "http://localhost:3000",
    #             "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    #             "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    #             "Access-Control-Allow-Credentials": "true",
    #         },
    #     )

    # user = jwt.decode(
    #     request.cookies["token"], os.environ["secret"], algorithms=["HS256"]
    # )
    # user = get_user(user["username"])
    # if len(user) == 0:
    #     return wrap_response(
    #         request.version,
    #         404,
    #         {
    #             "Content-Type": "text/html",
    #             "Connection": "close",
    #             "Access-Control-Allow-Origin": "http://localhost:3000",
    #             "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    #             "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    #             "Access-Control-Allow-Credentials": "true",
    #         },
    #     )
    # other_user = other_user[0]
    # user = user[0]
    # upload file
    file_meta = create_file(data["file"], data["data"])
    message = {
        "senders": user["username"] + "," + other_user["username"],
        "msg": json.dumps(
            {
                "type": "file",
                "filename": data.get("file").get("name"),
                "file_id": file_meta["_id"],
            }
        ),
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
