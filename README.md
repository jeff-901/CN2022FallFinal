# CN2022FallFinal

## deploy link
<https://cnfinal2022.herokuapp.com/>

## port number
PORT = 5556

## function

### server
* multithread server

### login & register
* type the password and account name you want and press register
* After register, you can use this acccount name and password to login
* Use the logout icon on the upper-right corner to logout in the mainpage
* uses jwt to encode
* implemented cookie to manage user state

### Add Friend
* Can use add button and type the account name you want to make friends with
* After adding friend, you can select to chat with them


### Chatbox
* After selecting friend, the chatbox is showed with previously posted image. 
* Uses the textinput field and to enter message.

### File Upload/Download
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

## build 


