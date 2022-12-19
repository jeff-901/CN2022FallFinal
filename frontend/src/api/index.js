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

export const FriendAPI = {
  addFriend: (name) =>
    userRequest({
      method: "post",
      url: `/api/friends`,
      data: { name },
    }),
  deleteFriend: (name) =>
    userRequest({
      method: "delete",
      url: `/api/friends`,
      data: { name },
    }),
};

export const MessageAPI = {
  createMessage: (name, msg) =>
    userRequest({
      method: "post",
      url: `/api/messages`,
      data: { name, msg },
    }),
  getMessages: (name) =>
    userRequest({
      method: "get",
      url: `/api/messages/${name}`,
    }),
};

export const FileAPI = {
  createFile: (file, data) =>
    userRequest({
      method: "post",
      url: `/api/files/?file=${file["name"]}&type=${file["type"]}`,
      data: data,
    }),
  getFile: (file_id) =>
    userRequest({
      method: "get",
      url: `/api/files/${file_id}`,
    }),
};

export const VideoAPI = {
  createVideo: (name) =>
    userRequest({
      method: "post",
      url: `/api/videos`,
      data: { name },
    }),
};
