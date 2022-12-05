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
import { TextInput } from "../components/TextInput";
import AddFriend from "../components/AddFriend";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
// import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
const useStyles = makeStyles({
  paper: {
    width: "80vw",
    height: "80vh",
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
  sidebar: {
    width: "15%",
    height: "100%",
    float: "left",
    "overflow-y": "scroll",
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
                  <ListItemText primary={x}/>
                </ListItemButton>
              </ListItem>
            );
          })}
        </List>
      </div>
      <div className={classes.container}>
        <Paper className={classes.paper} zdepth={2}>
          <Paper id="style-1" className={classes.messagesBody}>
            <MessageLeft
              message="あめんぼあかいなあいうえお"
              timestamp="MM/DD 00:00"
              // photoURL="https://lh3.googleusercontent.com/a-/AOh14Gi4vkKYlfrbJ0QLJTg_DLjcYyyK7fYoWRpz2r4s=s96-c"
              photoURL=""
              displayName=""
              avatarDisp={true}
            />
            <MessageLeft
              message="xxxxxhttps://yahoo.co.jp xxxxxxxxxあめんぼあかいなあいうえおあいうえおかきくけこさぼあかいなあいうえおあいうえおかきくけこさぼあかいなあいうえおあいうえおかきくけこさいすせそ"
              timestamp="MM/DD 00:00"
              photoURL=""
              displayName="テスト"
              avatarDisp={false}
            />
            <MessageRight
              message="messageRあめんぼあかいなあいうえおあめんぼあかいなあいうえおあめんぼあかいなあいうえお"
              timestamp="MM/DD 00:00"
              // photoURL="https://lh3.googleusercontent.com/a-/AOh14Gi4vkKYlfrbJ0QLJTg_DLjcYyyK7fYoWRpz2r4s=s96-c"
              photoURL=""
              displayName="まさりぶ"
              avatarDisp={true}
            />
            <MessageRight
              message="messageRあめんぼあかいなあいうえおあめんぼあかいなあいうえお"
              timestamp="MM/DD 00:00"
              // photoURL="https://lh3.googleusercontent.com/a-/AOh14Gi4vkKYlfrbJ0QLJTg_DLjcYyyK7fYoWRpz2r4s=s96-c"
              photoURL=""
              displayName="まさりぶ"
              avatarDisp={false}
            />
          </Paper>
          <TextInput />
        </Paper>
      </div>
    </div>
  );
}
