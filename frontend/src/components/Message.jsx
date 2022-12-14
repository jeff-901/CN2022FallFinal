import React from "react";
import { useState } from "react";
import { makeStyles } from "@mui/styles";
import { createStyles } from "@mui/material/styles";
import { createTheme } from "@mui/material";
import Avatar from "@mui/material/Avatar";
import { deepOrange } from "@mui/material/colors";
import FileDownloadIcon from "@mui/icons-material/FileDownload";
import { FileAPI } from "../api";
import fileDownload from "react-file-download";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import VideoPop from "react-video-pop";
import StickyVideo from "react-sticky-video";
import "react-sticky-video/dist/index.css";
import ReactPlayer from "react-player";
const theme = createTheme();
const useStyles = makeStyles({
  messageRow: {
    display: "flex",
  },
  messageRowRight: {
    display: "flex",
    justifyContent: "flex-end",
  },
  messageBlue: {
    position: "relative",
    marginLeft: "20px",
    marginBottom: "10px",
    padding: "10px",
    backgroundColor: "#A8DDFD",
    width: "100%",
    //height: "50px",
    textAlign: "left",
    font: "400 .9em 'Open Sans', sans-serif",
    border: "1px solid #97C6E3",
    borderRadius: "10px",
    "&:after": {
      content: "''",
      position: "absolute",
      width: "0",
      height: "0",
      borderTop: "15px solid #A8DDFD",
      borderLeft: "15px solid transparent",
      borderRight: "15px solid transparent",
      top: "0",
      left: "-15px",
    },
    "&:before": {
      content: "''",
      position: "absolute",
      width: "0",
      height: "0",
      borderTop: "17px solid #97C6E3",
      borderLeft: "16px solid transparent",
      borderRight: "16px solid transparent",
      top: "-1px",
      left: "-17px",
    },
  },
  messageOrange: {
    position: "relative",
    marginRight: "20px",
    marginBottom: "10px",
    padding: "10px",
    backgroundColor: "#f8e896",
    width: "45%",
    maxWidth: "500px",
    //height: "50px",
    textAlign: "left",
    font: "400 .9em 'Open Sans', sans-serif",
    border: "1px solid #dfd087",
    borderRadius: "10px",
    "&:after": {
      content: "''",
      position: "absolute",
      width: "0",
      height: "0",
      borderTop: "15px solid #f8e896",
      borderLeft: "15px solid transparent",
      borderRight: "15px solid transparent",
      top: "0",
      right: "-15px",
    },
    "&:before": {
      content: "''",
      position: "absolute",
      width: "0",
      height: "0",
      borderTop: "17px solid #dfd087",
      borderLeft: "16px solid transparent",
      borderRight: "16px solid transparent",
      top: "-1px",
      right: "-17px",
    },
  },

  messageContent: {
    padding: 0,
    margin: 0,
  },
  messageTimeStampRight: {
    position: "absolute",
    fontSize: ".85em",
    fontWeight: "300",
    marginTop: "10px",
    bottom: "-3px",
    right: "5px",
  },

  orange: {
    color: theme.palette.getContrastText(deepOrange[500]),
    backgroundColor: deepOrange[500],
    width: theme.spacing(4),
    height: theme.spacing(4),
  },
  avatarNothing: {
    color: "transparent",
    backgroundColor: "transparent",
    width: theme.spacing(4),
    height: theme.spacing(4),
  },
  displayName: {
    marginLeft: "20px",
  },
  videoPaper: {
    width: "630px",
    height: "420px",
    position: "absolute",
    top: "80px",
    left: "10%",
  },
});

const downloadFile = async (filename, file_id) => {
  fetch(import.meta.env.VITE_USER_BACKEND_URL + "/api/files/" + file_id).then(
    function (res) {
      console.log(
        res.arrayBuffer().then((buffer) => fileDownload(buffer, filename))
      );
    }
  );
};

export const MessageLeft = (props) => {
  const message = props.message;
  const timestamp = props.timestamp ? props.timestamp : "";
  const photoURL = props.photoURL ? props.photoURL : "dummy.js";
  const displayName = props.displayName ? props.displayName : "Anonymous";
  const classes = useStyles();

  //const watch = props.watch;
  //const handleWatch = ()=>{
  //  props.setWatch(!watch);
  //}
  const [watch, setWatch] = useState(false);
  return (
    <div className={classes.messageRow}>
      <Avatar
        alt={displayName}
        className={classes.orange}
        src={photoURL}
      ></Avatar>
      <div>
        <div className={classes.displayName}>{displayName}</div>
        <div className={classes.messageBlue}>
          {message.type === "msg" ? (
            <p className={classes.messageContent}>{message.data}</p>
          ) : message.type === "audio" ? (
            <audio
              src={
                import.meta.env.VITE_USER_BACKEND_URL +
                "/api/audio?id=" +
                message.id
              }
              controls={true}
            />
          ) : message.type === "video" ? (
            watch ? (
              <>
                <video
                  src={
                    import.meta.env.VITE_USER_BACKEND_URL +
                    "/api/video?id=" +
                    message.id
                  }
                  width="320"
                  height="240"
                  controls={true}
                />
                <Button
                  onClick={() => {
                    setWatch(false);
                    //handleWatch
                  }}
                >
                  close
                </Button>
              </>
            ) : (
              <p
                className={classes.messageContent}
                onClick={() => {
                  // downloadFile(message.name, message.id);
                  setWatch(true);
                  //handleWatch
                }}
              >
                <FileDownloadIcon />
                {message.name}
              </p>
            )
          ) : (
            <p
              className={classes.messageContent}
              onClick={() => {
                downloadFile(message.name, message.id);
              }}
            >
              <FileDownloadIcon />
              {message.name}
            </p>
          )}
          {/* <div className={classes.messageTimeStampRight}>
              {new Date(timestamp).toUTCString()}
            </div> */}
        </div>
      </div>
    </div>
  );
};

export const MessageRight = (props) => {
  const classes = useStyles();
  const message = props.message;
  const timestamp = props.timestamp ? props.timestamp : "";
  const [watch, setWatch] = useState(false);
  return (
    <div className={classes.messageRowRight}>
      <div className={classes.messageOrange}>
        {message.type === "msg" ? (
          <p className={classes.messageContent}>{message.data}</p>
        ) : message.type === "audio" ? (
          <audio
            src={
              import.meta.env.VITE_USER_BACKEND_URL +
              "/api/audio?id=" +
              message.id
            }
            controls={true}
          />
        ) : message.type === "video" ? (
          watch ? (
            <>
              <video
                src={
                  import.meta.env.VITE_USER_BACKEND_URL +
                  "/api/video?id=" +
                  message.id
                }
                width="320"
                height="240"
                controls={true}
              />
              <Button
                onClick={() => {
                  setWatch(false);
                }}
              >
                close
              </Button>
            </>
          ) : (
            <p
              className={classes.messageContent}
              onClick={() => {
                // downloadFile(message.name, message.id);
                setWatch(true);
              }}
            >
              <FileDownloadIcon />
              {message.name}
            </p>
          )
        ) : (
          <p
            onClick={() => {
              downloadFile(message.name, message.id);
            }}
          >
            <FileDownloadIcon />
            {message.name}
          </p>
        )}

        {/* <div className={classes.messageTimeStampRight}>
          {new Date(timestamp).toUTCString()}
        </div> */}
      </div>
    </div>
  );
};
