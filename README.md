# Smart-Stove
IoT setup that sends stove temperature readings in real time to the user through a web and mobile application. 

# Architecture
1. ESp32 connects to Wifi, samples the sensor data and sends to the Web Server via HTTP Post request.
2. Web server running on AWS receives sensor data and sends it to the Web Client and Mobile Client.
3. Web Server uses SQLite3 to store data.

Server backend is written in Python. Django is the open source API used which is modular and secure.
Mobile app is made using Ionic, a cross-platform mobile app development platform.
