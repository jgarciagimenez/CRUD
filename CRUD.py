# -*- coding: utf-8 -*-

from gi.repository import Gtk

import MySQLdb

Conexion = MySQLdb.connect(host='localhost', user='jose',passwd='cine', db='DBdePeliculas')
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)



class Handler:

    Builder = None


    def __init__(self):
        
        self.Create = None        
        self.Read = None       
        self.Update = None        
        self.Delete = None

        self.builder = Gtk.Builder()
        self.builder.add_from_file("menu_CRUD.glade")
        self.handlers = { "on_window_destroy": self.on_window_destroy,
                          "on_btn_accept_clicked_RD": self.on_btn_accept_clicked_RD,
                          "on_btn_cancel_clicked_RD": self.on_btn_cancel_clicked_RD,
                          "on_btn_accept_clicked_CU": self.on_btn_accept_clicked_CU,
                          "on_btn_cancel_clicked_CU": self.on_btn_cancel_clicked_CU,
                          "on_accept_error_ID": self.on_accept_error_ID,
                          "on_accept_dialog": self.on_accept_dialog,
                          "on_accept_error_1": self.on_accept_error_1,
                          "on_accept_error_ID2": self.on_accept_error_ID2,
                          "on_Create_Activate": self.on_Create_Activate,
                          "on_Update_Activate": self.on_Update_Activate,
                          "on_Read_Activate": self.on_Read_Activate,
                          "on_Delete_Activate": self.on_Delete_Activate,
                          "on_About_Activate": self.on_About_Activate,
                          "on_Close_Dia_CU": self.on_Close_Dia_CU,
                          "on_Close_no_ID": self.on_Close_no_ID,
                          "on_Close_about_dialog": self.on_Close_about_dialog,
                          "on_Close_dia_error_1": self.on_Close_dia_error_1,
                          "on_Close_dia_error_ID": self.on_Close_dia_error_ID,
                          "on_Close_Dia_RD": self.on_Close_Dia_RD }
   

        # Conectamos las señales e iniciamos la aplicación
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window")
        self.dia_CU = self.builder.get_object("dia_CU")
        self.dia_RD = self.builder.get_object("dia_RD")  
        self.about_dialog = self.builder.get_object("about_dialog") 
        self.dia_error_1 = self.builder.get_object("dia_error_1")    
        self.dia_error_ID = self.builder.get_object("dia_error_ID")  
        self.dialog_no_ID = self.builder.get_object("dialog_no_ID")  
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

    def on_About_Activate(self,*args):

        self.about_dialog.show()

    def on_Create_Activate(self, *args):

        self.entry1.set_text('')
        self.entry2.set_text('')
        self.entry3.set_text('')
        self.entry4.set_text('')
        self.entry5.set_text('')

        self.Create = True
        self.dia_CU.show()

    def on_Update_Activate(self, *args):

        self.entry1.set_text('')
        self.entry2.set_text('')
        self.entry3.set_text('')
        self.entry4.set_text('')
        self.entry5.set_text('')

        self.Update = True
        self.dia_CU.show()

    def on_Read_Activate(self, *args):

        self.entry1.set_text('')
        self.entry2.set_text('')
        self.entry3.set_text('')
        self.entry4.set_text('')
        self.entry5.set_text('')

        self.Read = True
        self.dia_RD.show()

    def on_Delete_Activate(self, *args):

        self.entry1.set_text('')
        self.entry2.set_text('')
        self.entry3.set_text('')
        self.entry4.set_text('')
        self.entry5.set_text('')

        self.Delete = True
        self.dia_RD.show()



    def on_btn_accept_clicked_RD(self,*args):


        ID = self.entry_RD.get_text()


        query= "SELECT * FROM Peliculas WHERE id="+ID+";"
        micursor.execute(query)
        registro= micursor.fetchone()

        if registro is None:

            self.dialog_no_ID.show()

            return

        if  self.Read:

            query= "SELECT * FROM Peliculas WHERE id=" + ID + ";"
            micursor.execute(query)
            registro= micursor.fetchone()

            self.entry1.set_text(registro['Titulo'])
            self.entry2.set_text(str(registro['Fecha']))
            self.entry3.set_text(registro['Director'])
            self.entry4.set_text(registro['Nacionalidad'])
            self.entry5.set_text(str(registro['Nota']))

            self.Read = False

        if self.Delete:

            query= "DELETE FROM Peliculas WHERE id="+str(ID)+";"
            micursor.execute(query)
            Conexion.commit()
            self.Delete = False

        self.entry_RD.set_text('')
        self.dia_RD.hide()
        

    def on_btn_cancel_clicked_RD(self,*args):

        self.entry_RD.set_text('')       
        self.dia_RD.hide()
        

    def on_btn_accept_clicked_CU(self,*args):

        ID = self.entry_DB_1.get_text() 
        Titulo = self.entry_DB_2.get_text() 
        year = self.entry_DB_3.get_text() 
        Director = self.entry_DB_4.get_text() 
        Nacion = self.entry_DB_5.get_text() 
        Nota = self.entry_DB_6.get_text() 

        if not ID.isdigit() or not Nota.isdigit() or not year.isdigit():

            self.dia_error_1.show()

            return  

        if self.Create:

            query= "SELECT * FROM Peliculas WHERE id="+ID+";"
            micursor.execute(query)
            registro= micursor.fetchone()

            if registro is not None:

                self.dia_error_ID.show()

                return

            query = "INSERT INTO Peliculas (id,Titulo,Fecha,Director,Nacionalidad,Nota) VALUES (" + str(ID) + ",'" + Titulo + "'," +str(year) + ",'" + Director +"','" + Nacion +"'," + str(Nota) + ");"
            micursor.execute(query)
            Conexion.commit()
            self.Create = False

        if self.Update:

            query = "UPDATE Peliculas SET Titulo='"+Titulo+"', Fecha="+str(year)+", Director='"+Director+"', Nacionalidad='"+Nacion+"', Nota="+str(Nota)+" WHERE id="+str(ID)+";"
            self.Update = False
            micursor.execute(query)
            Conexion.commit()
        

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


    def on_accept_dialog(self,*args):
        self.about_dialog.hide()

    def on_accept_error_1(self,*args):
        self.dia_error_1.hide()

    def on_accept_error_ID(self,*args):
        self.dia_error_ID.hide()

    def on_accept_error_ID2(self,*args):
        self.dialog_no_ID.hide()


    def on_Close_Dia_RD(self,*args):

        self.entry_RD.set_text('')
        self.dia_RD.hide()


    def on_Close_dia_error_1(self,*args):
        self.dia_error_1.hide()

    def on_Close_no_ID(self,*args):
        self.dialog_no_ID.hide()

    def on_Close_dia_error_ID(self,*args):
        self.dia_error_ID.hide()

    def on_Close_about_dialog(self,*args):
        self.about_dialog.hide()


def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()