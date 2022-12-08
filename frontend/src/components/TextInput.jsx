import React from "react";
import { useState } from "react";
import TextField from "@mui/material/TextField";
import { makeStyles } from "@mui/styles";
import SendIcon from "@mui/icons-material/Send";
import Button from "@mui/material/Button";
import { createTheme } from "@mui/material";
import { MessageAPI } from "../api";
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

export default function TextInput({ user, friend, setMessages, messages }) {
  const classes = useStyles();
  const [text, setText] = useState("");
  const sendMsg = async () => {
    console.log(`${user.username} send to ${friend} ${text}`);
    let res = await MessageAPI.createMessage(friend, text);
    console.log(res);
    setMessages([...messages, res]);
    setText("");
  };
  return (
    <>
      <form className={classes.wrapForm} noValidate autoComplete="off">
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
