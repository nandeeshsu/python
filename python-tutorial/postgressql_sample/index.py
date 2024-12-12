import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="mitanandeesh",
                        password="admin123",
                        port="5432")

print("database connected==>", conn)

cursor = conn.cursor()

cursor.execute("SELECT * FROM book")

print("fetched data from table book==>", cursor.fetchall())