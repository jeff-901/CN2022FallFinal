import { useState } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { createTheme } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { MessageLeft, MessageRight } from "../components/Message";
import TextInput from "../components/TextInput";
import AddFriend from "../components/AddFriend";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import { useEffect } from "react";
import { MessageAPI } from "../api";
// import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
const useStyles = makeStyles({
  paper: {
    width: "80%",
    height: "90vh",
    maxWidth: "500px",
    maxHeight: "700px",
    display: "flex",
    alignItems: "center",
    flexDirection: "column",
    position: "relative",
  },
  paper2: {
    width: "80vw",
    maxWidth: "500px",
    display: "flex",
    alignItems: "center",
    flexDirection: "column",
    position: "relative",
  },
  container: {
    width: "100vw",
    height: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  messagesBody: {
    width: "calc( 100% - 20px )",
    margin: 10,
    overflowY: "scroll",
    height: "calc( 100% - 80px )",
  },
  body: {
    backgroundColor: "#eeeeee",
    display: "block",
    width: "75%",
    height: "75%",
    float: "right",
    padding: "10px",
  },
  sidebar: {
    width: "15%",
    height: "100%",
    float: "left",
    margin: "10px",
    padding: "10px",
    alignItems: "center",
    flexDirection: "column",
    justifyContent: "center",
    overflowY: "scroll",
    backgroundColor: "#2196f3",
  },
  chatroom: {
    height: "100%",
    width: "100%",
    position: "fixed",
  },
});

export default function Chatroom({ user, setUser }) {
  const classes = useStyles();
  const [name, setName] = useState("");
  const [friend, setFriend] = useState("");
  const [messages, setMessages] = useState([]);
  const [stream, setStream] = useState(false);
  useEffect(() => {
    const fetchFriends = async () => {
      console.log(`friend: ${friend}`);
      if (friend != "") {
        console.log(`get messages ${friend}`);
        let msgs = await MessageAPI.getMessages(friend);
        console.log(msgs);
        setMessages(msgs);
      }
    };
    fetchFriends();
  }, [friend]);

  return (
    <div className={classes.chatroom}>
      <div className={classes.sidebar}>
        <div>Friend List</div>
        <AddFriend name={name} setName={setName} setUser={setUser} />
        <List>
          {user.friends.map((x) => {
            return (
              <ListItem disablePadding key={x}>
                <ListItemButton>
                  <ListItemText
                    primary={x}
                    onClick={() => {
                      setFriend(x);
                    }}
                  />
                </ListItemButton>
              </ListItem>
            );
          })}
        </List>
      </div>
      {/* <div className={classes.container}> */}
      {/* <Paper className={classes.paper} zdepth={2}> */}
      {/*  */}
      <div className={classes.body} id="Body">
        {friend === "" ? (
          <h1>Choose a friend</h1>
        ) : (
          <div>
            <Paper className={classes.paper} zdepth={2}>
              <Paper id="style-1" className={classes.messagesBody}>
                {messages.map((msg) => {
                  if (msg.senders.split(",")[0] !== user.username) {
                    return (
                      <MessageLeft
                        message={msg.msg}
                        timestamp={msg.timestamp * 1000}
                        // photoURL="https://lh3.googleusercontent.com/a-/AOh14Gi4vkKYlfrbJ0QLJTg_DLjcYyyK7fYoWRpz2r4s=s96-c"
                        photoURL=""
                        displayName={friend}
                        avatarDisp={true}
                      />
                    );
                  } else {
                    return (
                      <MessageRight
                        message={msg.msg}
                        timestamp={msg.timestamp * 1000}
                        // photoURL="https://lh3.googleusercontent.com/a-/AOh14Gi4vkKYlfrbJ0QLJTg_DLjcYyyK7fYoWRpz2r4s=s96-c"
                        photoURL=""
                        displayName={user.username}
                        avatarDisp={true}
                      />
                    );
                  }
                })}
              </Paper>
              <TextInput
                setMessages={setMessages}
                friend={friend}
                messages={messages}
                user={user}
                stream={stream}
                setStream={setStream}
              />
            </Paper>

            {!stream ? (
              <h1>test_function</h1>
            ) : (
              <>
                <h2>test_</h2>
                <img src="{{ url_for('aaa') }}" width="100%" />
              </>
            )}
          </div>
        )}
        <video
          id="videoPlayer"
          width="650"
          controls
          muted="muted"
          crossorigin="anonymous"
          autoplay
        >
          <source src="https://cnfinal2022.herokuapp.com/api/video" type="video/mp4" />
        </video>
      </div>
      {/* </div> */}
    </div>
  );
}
