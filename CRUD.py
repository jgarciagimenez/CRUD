# -*- coding: utf-8 -*-

from gi.repository import Gtk




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

        self.entry_RD.set_text('')
        self.dia_RD.hide()
        

    def on_btn_cancel_clicked_RD(self,*args):

        self.entry_RD.set_text('')       
        self.dia_RD.hide()
        

    def on_btn_accept_clicked_CU(self,*args):

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