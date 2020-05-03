import json
import mysql.connector



def insert_json(msg):
    print('trying')
    y = json.loads(msg[0:-1]).values()

    mydb = mysql.connector.connect(
    host="localhost",
    user="felix",
    passwd="felix", 
    database="home"
    )
    sql_statment = "insert into sensor (house_id, sensor_id, pressure, temperature, humidity) VALUES (%d, %d, %f, %f, %f);"
    sql_statement = sql_statment % tuple(y)
    mycursor = mydb.cursor()
    mycursor.execute(sql_statement)
    mydb.commit()


f = open("/home/felix/Documents/HouseSensors/Cloud/DataTransfer/temp_data/data.txt", "r")
x = f.readline()
insert_json(x)


