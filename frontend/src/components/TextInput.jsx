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
    let res = await VideoAPI.createVideo(user);
  };

  const handleAudio = async () => {
    navigator.mediaDevices
      .getUserMedia({ audio: true })
      .then((stream) => {
        // const audioContext = new AudioContext;
        // const audioInput = audioContext.createMediaStreamSource(stream);

        const rec = new MediaRecorder(stream);
        // 這個聲音串流一開時，就開始進行錄製。
        rec.start();
        console.log("start record");
        setTimeout(function () {
          // 然後在 10 秒後結束錄製，並產生個語音控制項與下載連結。
          rec.stop();
          console.log("finish record");
          console.log(rec.state);
          // createAudioController(rec);
          // createDownloadLink(rec);
        }, 3000);
      })
      .catch((err) => {
        console.log("nonono ~~~ !!");
        console.log(err);
      });
  };

  return (
    <>
      <form className={classes.wrapForm} noValidate autoComplete="off">
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
          onClick={handleAudio}
        >
          <VideoCallRoundedIcon />
        </Button>
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
      </form>
    </>
  );
}
