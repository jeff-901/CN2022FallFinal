import React from "react";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import { makeStyles } from "@mui/styles";
import SendIcon from "@mui/icons-material/Send";
import Button from "@mui/material/Button";
import { createTheme } from "@mui/material";
import { MessageAPI, VideoAPI, FileAPI } from "../api";
import FileUploadRoundedIcon from "@mui/icons-material/FileUploadRounded";
import VideoCallRoundedIcon from "@mui/icons-material/VideoCallRounded";
import KeyboardVoiceIcon from "@mui/icons-material/KeyboardVoice";
import StopIcon from "@mui/icons-material/Stop";
import { AudioRecorder, useAudioRecorder } from "react-audio-voice-recorder";

import { useReactMediaRecorder } from "react-media-recorder";
import VideoRecorder from "react-video-recorder";
import {
  RecordWebcam,
  useRecordWebcam,
  CAMERA_STATUS,
} from "react-record-webcam";


const theme = createTheme();

const useStyles = makeStyles({
  wrapForm: {
    display: "flex",
    justifyContent: "center",
    width: "95%",
    margin: `${theme.spacing(0)} auto`,
  },
  wrapText: {
    width: "100%",
  },
  button: {
    //margin: theme.spacing(1),
  },
});

export default function TextInput({
  user,
  friend,
  setMessages,
  messages,
  stream,
  setStream,
}) {
  const classes = useStyles();
  const [text, setText] = useState("");
  const [file, setFile] = useState("");
  // const [recording, setRecording] = useState(false);

  function getArrayBuffer(file) {
    return new Promise((resolve, reject) => {
      // STEP 3: 轉成 ArrayBuffer, i.e., reader.result
      const reader = new FileReader();
      reader.addEventListener("load", () => {
        resolve(reader.result);
      });
      reader.readAsArrayBuffer(file);
    });
  }

  const sendMsg = async () => {
    console.log(`send msg file: ${file}`);
    if (file !== "") {
      console.log(`${user.username} send to ${friend} ${file}`);
      const arrayBuffer = await getArrayBuffer(file);
      let res_file = await FileAPI.createFile(file, arrayBuffer, friend);
      let res_msg = await MessageAPI.createMessage(friend, {
        type: "file",
        name: file["name"],
        id: res_file.id,
      });
      setMessages([...messages, res_msg]);
      setFile("");
    }
    if (text !== "") {
      console.log(`${user.username} send to ${friend} ${text}`);
      let res = await MessageAPI.createMessage(friend, {
        type: "msg",
        data: text,
      });
      console.log(res);
      setMessages([...messages, res]);
      setText("");
    }
  };

  //const [stream, setStream] = useState(false);
  const handleStream = async () => {
    setStream(!stream);
    //let res = await VideoAPI.createVideo(user);
  };

  const handleAudio = async (blob) => {
    const buf = await blob.arrayBuffer();
    // console.log(blob.getArrayBuffer())
    let res_file = await FileAPI.createFile(
      { name: "tmp.mp3", type: "audio/mpeg" },
      buf,
      friend
    );
    console.log(res_file);
    let res_msg = await MessageAPI.createMessage(friend, {
      type: "audio",
      name: "tmp.mp3",
      id: res_file.id,
    });
    setMessages([...messages, res_msg]);
    setFile("");
  };

  const handleVideo = async (blob) => {
    const buf = await blob.arrayBuffer();
    // console.log(blob.getArrayBuffer())
    let res_file = await FileAPI.createFile(
      { name: "tmp.mp4", type: "video" },
      buf,
      friend
    );
    console.log(res_file);
    let res_msg = await MessageAPI.createMessage(friend, {
      type: "video",
      name: "tmp.mp4",
      id: res_file.id,
    });
    setMessages([...messages, res_msg]);
    setFile("");
  };
  
  
  return (
    <>
      <form className={classes.wrapForm} noValidate autoComplete="off">
        {!stream ? (
          <>
            <input
              accept="*"
              type="file"
              id="upload_file"
              name="myfile"
              hidden
              onChange={(e) => {
                setFile(e.target.files[0]);
                console.log(e.target.files);
              }}
            />
            <Button
              variant="outlined"
              color="primary"
              size="medium"
              className={classes.button}
              // onClick={sendMsg}
            >
              <label for="upload_file">
                <FileUploadRoundedIcon />
              </label>
            </Button>

            <Button
              variant="outlined"
              color="primary"
              size="small"
              className={classes.button}
              onClick={handleStream}
            >
              <VideoCallRoundedIcon />
            </Button>

            {/* <Button
        variant="outlined"
        color="primary"
        size="small"
        className={classes.button}
        onClick={handleAudio}
      >
        {
        recording?<StopIcon/>:<KeyboardVoiceIcon />
      }
        
      </Button> */}
            <AudioRecorder onRecordingComplete={handleAudio} />
            <TextField
              id="standard-text"
              label="Type a message"
              className={classes.wrapText}
              //margin="normal"
              value={text}
              onChange={(event) => {
                setText(event.target.value);
              }}
            />

            <Button
              variant="contained"
              color="primary"
              className={classes.button}
              onClick={sendMsg}
            >
              <SendIcon />
            </Button>
          </>
        ) : (
          <>
          <button
        >
          Open camera
        </button>
         
          <Button
                onClick={handleStream}
              >
                close
              </Button>
              </>
        )}
      </form>
    </>
  );
}
