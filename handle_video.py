from flask import Flask, render_template, Response
import cv2
from dotenv import load_dotenv
import json
from utils import *
from db import *
import jwt
import time

app = None


class handle_video:
    def __init__(self):
        self.app = Flask(__name__)
        self.camera = cv2.VideoCapture(0)
        return

    def gen_frames(self):
        while True:
            # Capture frame-by-frame
            success, frame = self.camera.read()  # read the camera frame
            if not success:
                break
            else:
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )
                # concat frame one by one and show result


Video_obj = handle_video()
# @Video_obj.app.route('/api/videos/video_feed')
@Video_obj.app.route("/aaa")
def video_feed():

    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        Video_obj.gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# @Video_obj.app.route('/api/videos')
@Video_obj.app.route("/")
def index():
    """Video streaming home page."""
    return render_template("index.html")


def return_video_response(request: HttpRequest):
    data = json.loads(request.data)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


'''

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera
#return app ,camera

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/api/vidoes/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/api/videos')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1')

'''
