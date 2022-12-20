import "./App.css";
import { Route, Switch, Redirect } from "react-router-dom";
// hooks
import { useState, useEffect } from "react";
import { styled } from "@mui/material/styles";
import { makeStyles } from "@mui/styles";
// mui
import { createTheme } from "@mui/material/styles";
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import CircularProgress from "@mui/material/CircularProgress";
// components
import NavigationBar from "./components/NavigationBar";
// pages
import Chatroom from "./pages/Chatroom";
import Login from "./pages/Login";
// api
import { SessionAPI } from "./api";

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: 0,
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const themeOptions = {
  palette: {
    type: "light",
    primary: {
      main: "#0257b8",
    },
    secondary: {
      main: "#f50057",
    },
  },
};

const theme = createTheme(themeOptions);

const useStyles = makeStyles({
  root: {
    margin: 0,
    padding: 0,
  },
});

function App() {
  // drawer functions
  const classes = useStyles();
  const [openDrawer, setOpenDrawer] = useState(false);
  const handleOpenDrawer = () => setOpenDrawer(true);
  const handleCloseDrawer = () => setOpenDrawer(false);

  // login
  const [fetching, setFetching] = useState(true);
  const [isLogin, setIsLogin] = useState(false);
  const [user, setUser] = useState({});
  useEffect(() => {
    const checkLogin = async () => {
      try {
        const user = await SessionAPI.getSession();
        setIsLogin(true);
        setUser(user);
      } catch (err) {
        console.error(err);
      }
      setFetching(false);
    };
    checkLogin();
  }, []);

  // logout
  const handleLogout = async () => {
    try {
      await SessionAPI.deleteSession();
      setIsLogin(false);
      setUser({});
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ display: "flex" }}>
        <NavigationBar
          isLogin={isLogin}
          handleLogout={handleLogout}
          user={user}
          handleOpenDrawer={handleOpenDrawer}
        />
        {/* <SideBar open={openDrawer} handleCloseDrawer={handleCloseDrawer} /> */}
        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <DrawerHeader />
          {/* <Container> */}
          {fetching ? (
            <CircularProgress />
          ) : (
            <Switch>
              <Route exact path="/">
                {isLogin ? (
                  <Chatroom user={user} setUser={setUser} />
                ) : (
                  <Login setUser={setUser} setIsLogin={setIsLogin} />
                )}
              </Route>
            </Switch>
          )}
        </Box>
      </Box>
    </ThemeProvider>
  );
}

export default App;
