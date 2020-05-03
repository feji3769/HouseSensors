import json
import mysql.connector



def select_record():
    mydb = mysql.connector.connect(
    host="localhost",
    user="felix",
    passwd="felix", 
    database="home"
    )

    sql_statement = "select * from sensor limit 1;"
    mycursor = mydb.cursor()
    mycursor.execute(sql_statement)
    col_names = mycursor.column_names
    results = mycursor.fetchall()

    json_list = []
    for r in results:
        json_list.append(dict(zip(col_names, r)))

    return(json_list)

def json_record():

   cur = mysql.connection.cursor()
   cur.execute('''SELECT * FROM Users WHERE id=1''')
   row_headers=[x[0] for x in cur.description] #this will extract row headers
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data)