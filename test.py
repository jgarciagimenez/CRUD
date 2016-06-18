# -*- coding: utf-8 -*-
import MySQLdb

Conexion = MySQLdb.connect(host='localhost', user='jose',passwd='cine', db='DBdePeliculas')
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# ID = 1
# Titulo = 'Pulp Fiction'
# year = 1994
# Director = 'Tarantino'
# Nacion = 'EstadosUnidos'
# Nota = 9
#   query = "INSERT INTO Peliculas (id,Titulo,Año,Director,Nacionalidad,Nota) VALUES (" + ID + ",'" + Titulo + "'," + year + ",'" + Director +"','" + Nacion +"'," + Nota + ");"

query = "INSERT INTO Peliculas (id,Titulo,Año,Director,Nacionalidad,Nota) VALUES (1,'Pulp Fiction',1994,'Tarantino','EstadosUnidos',9);"
         
# query = "INSERT INTO Victimas (id,Nombre,Profesion,Muerte) VALUES (2, 'Vampiro feo','Muertos Vivientes','Estaca de madera');"

micursor.execute(query)
Conexion.commit()


query= "SELECT * FROM Victimas WHERE id=1;"
registro= micursor.fetchone()

print registro
