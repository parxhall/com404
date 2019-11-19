from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Passport Check")
        
        # add components
        self.__add_heading_label()
        self.__add_q1_label()
        self.__add_first_check()
        self.__add_second_check()
        self.__add_q2_label()
        self.__add_first2_check()
        self.__add_second2_check()
        self.__add_q3_label()
        self.__add_first3_check()
        self.__add_second3_check()
        self.__add_check_button()

        
    def __add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.grid(row=1, column = 0, columnspan=2)
        
        # style
        self.heading_label.configure(font="Arial 14", text="Passport Checker")
        

    def __add_q1_label(self):
        #create
        self.q1_label = Label()
        self.q1_label.grid(row=2, column = 0, columnspan=2)

        #style
        self.q1_label.configure(font="Arial 8", text="1.Photo matches face?")


    def __add_first_check(self):
        #create
        self.first_check = Checkbutton()
        self.first_check.grid(row=3, column=0, columnspan=1)

        #stlye
        self.first_check.configure(text="Yes")
    

    def __add_second_check(self):
        #create
        self.second_check = Checkbutton()
        self.second_check.grid(row=3, column=1, columnspan=1)

        #stlye
        self.second_check.configure(text="No")

    
    def __add_q2_label(self):
        #create
        self.q2_label = Label()
        self.q2_label.grid(row=4, column=0, columnspan=2)

        #style
        self.q2_label.configure(font="Arial 8", text="1.Passport has at least 6 months validity?")

    
    def __add_first2_check(self):
        #create
        self.first2_check = Checkbutton()
        self.first2_check.grid(row=5, column=0, columnspan=1)

        #stlye
        self.first2_check.configure(text="Yes")
    

    def __add_second2_check(self):
        #create
        self.second2_check = Checkbutton()
        self.second2_check.grid(row=5, column=1, columnspan=1)

        #stlye
        self.second2_check.configure(text="No")
        

    def __add_q3_label(self):
        #create
        self.q3_label = Label()
        self.q3_label.grid(row=6, column=0, columnspan=2)

        #style
        self.q3_label.configure(font="Arial 8", text="1.Passport has at least 6 months validity?")

    
    def __add_first3_check(self):
        #create
        self.first3_check = Checkbutton()
        self.first3_check.grid(row=7, column=0, columnspan=1)

        #stlye
        self.first3_check.configure(text="Yes")
    

    def __add_second3_check(self):
        #create
        self.second3_check = Checkbutton()
        self.second3_check.grid(row=7, column=1, columnspan=1)

        #stlye
        self.second3_check.configure(text="No")
        
    def __add_check_button(self):
        #create
        self.check_button = Button()
        self.check_button.grid(row=8)

        #style
        self.check_button.configure(text="Check")


    
        