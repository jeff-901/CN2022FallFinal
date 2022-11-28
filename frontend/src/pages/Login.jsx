import { useState } from "react";
// mui
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
// api
import { SessionAPI, UserAPI } from "../api";

export default function Login({ setIsLogin, setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    const user = await SessionAPI.createSession(username, password);
    if (user.username != null){
      setUser(user);
      setIsLogin(true);
    } else {
      setPassword("");
      setUser("");
    }
  };

  const handleCreate = async (event) => {
    event.preventDefault();
    const user = await UserAPI.createUser(username, password);
    if (user.username != null){
      setUser(user);
      setIsLogin(true);
    } else {
      setPassword("");
      setUser("");
    }
  };

  return (
    <Container component="main" maxWidth="xs" bgcolor="white">
      <Box
        sx={{
          marginTop: 4,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography component="h1" variant="h5">
          Login
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }} onSubmit={handleSubmit}>
          <TextField
            margin="normal"
            type="username"
            required
            fullWidth
            id="username"
            label="username"
            name="username"
            autoComplete="username"
            autoFocus
            value={username}
            onChange={(event) => setUsername(event.target.value)}
          />
          <TextField
            margin="normal"
            type="password"
            required
            fullWidth
            name="password"
            label="password"
            id="password"
            autoComplete="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
          <Button type="submit" fullWidth variant="contained" sx={{ mt: 3 }}>
            Login
          </Button>
          <Button onClick={handleCreate} fullWidth variant="contained" sx={{ mt: 3 }}>
            Register
          </Button>
        </Box>
      </Box>
    </Container>
  );
}
