# Importa pandas y sqlite3
import pandas as pd
import sqlite3

# Crea una conexión a la base de datos SQLite y si no existe la db la crea
#con = sqlite3.connect("dbpython")
# Extrae los datos de la consulta directamente a un DataFrame
#surveys_df = pd.read_sql_query("SELECT * from surveys", con)
# Selecciona sólo datos en el año 2002
#surveys2002 = surveys_df[surveys_df.year == 2002]
# Escribe los datos del nuevo DataFrame en una nueva tabla en SQLite
#df.to_sql("ACCION TANTO", con, if_exists="replace")
ticker = sqlite3.connect("ticker_database")
c = ticker.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tickers (results)")
ticker.commit()
df.to_sql('tickers', ticker, if_exists='replace', index = False)
c.execute('''  
SELECT * FROM tickers
          ''')

for row in c.fetchall():
    print (row)
# No te olvides de cerrar la conexión
con.close()