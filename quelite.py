import sqlite3

#Crea una base de datos quelite y una tabla

conexion = sqlite3.connect('quelite.db')
conexion.text_factory = str
c = conexion.cursor()

dato = ("ureshii")

c.execute("INSERT INTO productos (nombre) VALUES (?)" , dato)

c.execute("SELECT * FROM productos")
registros = c.fetchall()

for i in range(len(registros)):
    print (registros[i])

conexion.commit()

conexion.close()
