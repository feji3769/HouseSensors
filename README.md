# HouseSensors
This project allows one to connect esp32 devices to a network on a raspberry pi, save data collected from these sensors to a database, 
run a website with a rest API to view this data, and accesss the data via a phone app. 

As it stands this repo has been made to work on a single raspberry pi 38, an esp32 connected to a temp/pressure/humidity/elev. sensor, a linux box running Mosquitto as the MQTT broker and mySQL server as the database. 


# App 
Contains a basic IOS app. 

# Cloud 
Contains code for the webserver. Including database. 

# Data 
Data for testing purposes. Actual data is stored in a SQL database. 

# Pi
The code that runs on the PIs

# Sensors
Code written for the sensors collecting data. 

. . . 
