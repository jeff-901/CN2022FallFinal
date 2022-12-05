import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { FriendAPI } from "../api";
export default function AddFriend({ name, setName, setUser }) {
  const handleAddFriend = async () => {
    let re_user = await FriendAPI.addFriend(name);
    console.log(`re_user: ${re_user}`);
    setUser(re_user);
    setName("");
  };
  return (
    <>
      <TextField
        id="addFriend"
        label="friend"
        variant="standard"
        value={name}
        onChange={(event) => setName(event.target.value)}
      />
      <Button variant="contained" onClick={handleAddFriend}>
        Add
      </Button>
    </>
  );
}
