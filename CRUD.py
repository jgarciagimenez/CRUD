# -*- coding: utf-8 -*-

from gi.repository import Gtk

import MySQLdb

Conexion = MySQLdb.connect(host='localhost', user='jose',passwd='cine', db='DBdePeliculas')
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)



class Handler:

    Builder = None

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("menu_CRUD.glade")
        self.handlers = { "on_window_destroy": self.on_window_destroy,
                          "on_btn_accept_clicked_RD": self.on_btn_accept_clicked_RD,
                          "on_btn_cancel_clicked_RD": self.on_btn_cancel_clicked_RD,
                          "on_btn_accept_clicked_CU": self.on_btn_accept_clicked_CU,
                          "on_btn_cancel_clicked_CU": self.on_btn_cancel_clicked_CU,
                          "on_Create_Activate": self.on_Create_Activate,
                          "on_Update_Activate": self.on_Update_Activate,
                          "on_Read_Activate": self.on_Read_Activate,
                          "on_Delete_Activate": self.on_Delete_Activate,
                          "on_Close_Dia_CU": self.on_Close_Dia_CU,
                          "on_Close_Dia_RD": self.on_Close_Dia_RD }
   

        # Conectamos las señales e iniciamos la aplicación
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window")
        self.dia_CU = self.builder.get_object("dia_CU")
        self.dia_RD = self.builder.get_object("dia_RD")       
        self.entry_RD = self.builder.get_object("entry_RD")
        self.entry_DB_1 = self.builder.get_object("entry_DB_1")
        self.entry_DB_2 = self.builder.get_object("entry_DB_2")           
        self.entry_DB_3 = self.builder.get_object("entry_DB_3")
        self.entry_DB_4 = self.builder.get_object("entry_DB_4")
        self.entry_DB_5 = self.builder.get_object("entry_DB_5")
        self.entry_DB_6 = self.builder.get_object("entry_DB_6")

        self.entry1 = self.builder.get_object("entry1")        
        self.entry2 = self.builder.get_object("entry2")
        self.entry3 = self.builder.get_object("entry3")        
        self.entry4 = self.builder.get_object("entry4")
        self.entry5 = self.builder.get_object("entry5")        

        self.window.show_all()

   
    def on_window_destroy(self, *args):
        print 'Se ha cerrado la ventana'
        Gtk.main_quit(*args)


    def on_Create_Activate(self, *args):
        self.dia_CU.show()

    def on_Update_Activate(self, *args):
        self.dia_CU.show()

    def on_Read_Activate(self, *args):
        self.dia_RD.show()

    def on_Delete_Activate(self, *args):
        self.dia_RD.show()



    def on_btn_accept_clicked_RD(self,*args):


        ID = self.entry_RD.get_text() 
        query= "SELECT * FROM Victimas WHERE id=" + ID + ";"
        registro= micursor.fetchone()

        self.entry1.set_text(registro[1])
        self.entry2.set_text(registro[2])
        self.entry3.set_text(registro[3])
        self.entry4.set_text(registro[4])
        self.entry5.set_text(registro[5])

        self.entry_RD.set_text('')
        self.dia_RD.hide()
        

    def on_btn_cancel_clicked_RD(self,*args):

        self.entry_RD.set_text('')       
        self.dia_RD.hide()
        

    def on_btn_accept_clicked_CU(self,*args):

        ID = self.entry_DB_1.get_text() 
        Titulo = self.entry_DB_2.get_text() ## Tengo que elegir la base de datos y poner los nombres bien
        year = self.entry_DB_3.get_text() ## Tengo que elegir la base de datos y poner los nombres bien
        Director = self.entry_DB_4.get_text() ## Tengo que elegir la base de datos y poner los nombres bien
        Nacion = self.entry_DB_5.get_text() ## Tengo que elegir la base de datos y poner los nombres bien
        Nota = self.entry_DB_6.get_text() ## Tengo que elegir la base de datos y poner los nombres bien

        query = "INSERT INTO Peliculas (id,Titulo,Año,Director,Nacionalidad,Nota) VALUES (" + ID + ",'" + Titulo + "'," + year + ",'" + Director +"','" + Nacion +"'," + Nota + ");"

        micursor.execute(query)

        self.entry_DB_1.set_text('') 
        self.entry_DB_2.set_text('') 
        self.entry_DB_3.set_text('') 
        self.entry_DB_4.set_text('') 
        self.entry_DB_5.set_text('') 
        self.entry_DB_6.set_text('') 

        self.dia_CU.hide()
        

    def on_btn_cancel_clicked_CU(self,*args):

        self.entry_DB_1.set_text('') 
        self.entry_DB_2.set_text('') 
        self.entry_DB_3.set_text('') 
        self.entry_DB_4.set_text('') 
        self.entry_DB_5.set_text('') 
        self.entry_DB_6.set_text('')   

        self.dia_CU.hide()    
 

    def on_Close_Dia_CU(self):


        self.entry_DB_1.set_text('') 
        self.entry_DB_2.set_text('') 
        self.entry_DB_3.set_text('') 
        self.entry_DB_4.set_text('') 
        self.entry_DB_5.set_text('') 
        self.entry_DB_6.set_text('') 

        self.dia_CU.hide()


    def on_Close_Dia_RD(self):

        self.entry_RD.set_text('')
        self.dia_RD.hide()


def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()