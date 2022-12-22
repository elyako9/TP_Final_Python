import sqlite3

def resumen():
  con = sqlite3.connect("dbacciones")
  cursor = con.cursor()
  cursor.execute('SELECT name FROM sqlite_master WHERE type = "table";')
  row = cursor.fetchall()
  for g in range(len(row)):
    acc = row[g][0]
    cursor.execute(f'SELECT Fecha FROM {acc};')
    fechasacc = cursor.fetchall()
    print (f">>> {acc} - {fechasacc[0][0]} <--> {fechasacc[-1][0]}")
  con.close()
  return None

