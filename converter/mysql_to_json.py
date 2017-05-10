import json

import MySQLdb

conn = MySQLdb.connect("localhost","root","limitless","nim_finder")
cursor = conn.cursor()
sql = "SELECT nim, nama FROM nim_nama"
cursor.execute(sql)
result = cursor.fetchall()

object_list = []
for item in result:
    nim_nama = {
        "nim": item[0],
        "nama": item[1]
        }
    object_list.append(nim_nama)

data = {
    "data" : object_list,
}
json_string = json.dumps(data)
print(json_string)