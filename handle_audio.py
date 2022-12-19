from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt
import os, math

load_dotenv()


def handle_get(request: HttpRequest):
    audio_file_id = request.path[len("/api/audio?id=") :]

    range_size = request.headers.get("Range")
    if range_size is None:
        return wrap_response(
            request.version,
            404,
            {
                "Content-Type": "application/pdf",
                "Connection": "close",
                "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
                "Access-Control-Allow-Credentials": "true",
            },
        )
    print(audio_file_id)
    file_meta = get_file_meta(audio_file_id)
    audio_size = file_meta["size"]
    CHUNK_SIZE = 10 ** 6
    start = int(range_size.replace("-", "")[len("bytes=") :])
    end = min(start + CHUNK_SIZE, audio_size)
    contentLength = end - start
    header = {
        "Content-Range": f"bytes {start}-{end-1}/{audio_size}",
        "Accept-Ranges": "bytes",
        "Content-Length": contentLength,
        "Content-Type": file_meta["type"],
        "Access-Control-Allow-Origin": "https://cnfinal2022.herokuapp.com",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Request-Headers": "Access-Control-Allow-Headers, Content-Type, X-Requested-With, content-type, Origin, Accept, Access-Control-Request-Method, Access-Control-Request-Headers",
    }
    _, _, data = get_file(audio_file_id, start, end)
    # print(len(data))
    return wrap_response(request.version, 206, header, data)
