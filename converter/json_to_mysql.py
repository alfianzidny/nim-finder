import json
import MySQLdb

def create_nim_nama(conn, nim_nama):
    sql = "INSERT INTO nim_nama(nim,nama) VALUES(%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, nim_nama)
    conn.commit()
    return cur.lastrowid

def cek_nim(conn, nim):
    sql = "SELECT nim FROM nim_nama WHERE nim=" + nim + ""
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchone()

conn = MySQLdb.connect("localhost","root","limitless","nim_finder" )
with conn:
    with open('../data/nim_nama_draft.json') as data_file:
        data = json.load(data_file)
    for item in data:
        if(cek_nim(conn,item['nim'])):
            continue
        nim_nama=(item['nim'],item["nama"])
        print(nim_nama)
        create_nim_nama(conn, nim_nama)
conn.close()