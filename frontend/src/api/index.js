import { userRequest } from "./request";
export const SessionAPI = {
  createSession: (username, password) =>
    userRequest({
      method: "post",
      url: `/api/session`,
      data: {
        username,
        password,
      },
    }),
  getSession: () =>
    userRequest({
      method: "get",
      url: `/api/session`,
    }),
  deleteSession: () =>
    userRequest({
      method: "delete",
      url: `/api/session`,
    }),
};

export const UserAPI = {
  createUser: (username, password) =>
    userRequest({
      method: "post",
      url: `/api/users`,
      data: { username, password },
    }),
  getUser: (username) =>
    userRequest({
      method: "get",
      url: `/api/users/${username}`,
    }),
  deleteUser: (username) =>
    userRequest({
      method: "delete",
      url: `/api/users/${username}`,
    }),
};
