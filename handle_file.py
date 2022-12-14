from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt
import time

load_dotenv()


def handle_post(c, request: HttpRequest):
    filename_type = request.path[len("/api/files/?file=") :].split("&type=")
    filename = filename_type[0]
    file_type = filename_type[1]
    size = int(request.headers["Content-Length"])
    cur = len(request.data)
    print(cur, len(request.data), size)
    data = request.data
    while cur < size:
        left = c.recv(1000000)
        cur += len(left)
        data += left
        print(cur, len(left), len(data), size)
    print(size, len(data))
    print(file_type)
    file_meta = create_file(filename, data, file_type, size)

    return wrap_response(
        request.version,
        200,
        {
            "Content-Type": "application/json",
            "Connection": "close",
            "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
            "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Credentials": "true",
        },
        json.dumps({"id": file_meta}),
    )


def handle_get(request: HttpRequest):
    file_id = request.path[len("/api/files/") :]
    file_type, size, data = get_file(file_id)
    print(len(data), size)
    if data != None:
        return wrap_response(
            request.version,
            200,
            {
                "Content-Type": file_type,
                "Content-Length": size,
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
            data,
        )
    else:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "application/json",
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
