import psycopg2
import json

def insert_data(server_name, data_array):
    conn = psycopg2.connect(
    host="localhost",
    database="nodedata",
    user="flaskuser",
    password="password"
)
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO mytable (server_name, data1)
        VALUES (%s, %s)
        ON CONFLICT (server_name) DO UPDATE SET
            data1 = EXCLUDED.data1;
    """, (server_name, json.dumps(data_array)))
    
    conn.commit()
    cur.close()
    conn.close()

def extract_data(server_name):
    conn = psycopg2.connect(
    host="localhost",
    database="nodedata",
    user="flaskuser",
    password="password"
    )
    cur = conn.cursor()
    if server_name:
        cur.execute("SELECT * FROM mytable WHERE server_name = %s", (server_name,))
    else:
        cur.execute("SELECT * FROM mytable")

    rows = cur.fetchall()

    data = []
    for row in rows:
        data.append({
            "server": row[0],
            "data": row[1]
        })

    return data