import sqlite3

conn = sqlite3.connect("Attadance.db")

cmd = input("SQL>")
cursor = conn.execute(cmd)