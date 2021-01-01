import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

#execute fungsinya mengesukisi perintah sql
c.execute('CREATE TABLE IF NOT EXISTS \
           data(id INTEGER PRIMARY KEY, plat TEXT, jenis TEXT, durasi INTEGER, bayar INTEGER)')

#create table if not exits artinya jika table sudah ada
#tidak perlu di buat lagi

c.close()
conn.close()
