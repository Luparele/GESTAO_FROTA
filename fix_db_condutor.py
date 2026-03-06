import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# Turn off foreign keys temporarily
cur.execute('PRAGMA foreign_keys = OFF;')

# First, empty out the condutor text column so it doesn't fail the conversion
cur.execute('UPDATE APP_FROTA_veiculo SET condutor = NULL;')
conn.commit()

print("Data in condutor column cleared for migration.")
