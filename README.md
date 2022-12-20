# CN2022FallFinal

## Deploy link
<https://cnfinal2022.herokuapp.com>

## Team Members
B07901052 劉展碩
B09901142 呂睿超

## Function

### Server (Bonus)
* multithread server

### Login & Register
* type the password and account name you want and press register
* After register, you can use this acccount name and password to login
* Use the logout icon on the upper-right corner to logout in the mainpage
* **Bonus**: uses jwt to store user state in cookie

### Add Friend (Bonus)
* Can use add button and type the account name you want to make friends with
* After adding friend, you can select to chat with them


### Chatbox
* After selecting friend, the chatbox is showed with previously posted image. 
* Uses the textinput field and to enter message.

### File Upload/Download (Bonus)
* Use the file upload icon and press the send message button to upload file
* It would be shown similar with the message form in the chatbox
* Can use file download icon to fetch and download file.

### Audio Streaming
* Use the Audio Record icon to record live audio recordings.
* Save button for upload
* Pause button for temporary pause
* Stop button for permanently discard

### Video Streaming
* If the file uploaded is a video, click the message(file name) in the chatbox to view the uploaded video.
* Uses streaming to fetch data from database

## Build 
### set .env
Add `.env` file with following variables
```bash
VITE_USER_BACKEND_URL=<user backend url>
```
Then run
```
cd frontend
yarn
yarn build
```

## Run
### set .env
Add `.env` file with following variables
```bash
MONGO_URL=<mongo url>
secret=<secret key>
PORT=<port>
```
Then run
```
pip install -r requirements.txt
python3 server.py
```


