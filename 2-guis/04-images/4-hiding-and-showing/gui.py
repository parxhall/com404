from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_main_label()
        self.add_name_label()
        self.add_name_entry()
        self.add_name_check()
        self.add_pass_label()
        self.add_pass_entry()
        self.add_pass_check()
        self.add_night_label()
        self.add_night_entry()
        self.add_night_check()
        self.add_check_button()

    def add_main_label(self):
        #create
        self.main_label = Label()
        self.main_label.grid(row=0, columnspan=3)

        #style
        self.main_label.configure(font="arial 13", text="Hotel Check In")

    def add_name_label(self):
        #create
        self.name_label = Label()
        self.name_label.grid(row=1, column=1)

        #style
        self.name_label.configure(font="arial 8", text="Name:")

    def add_name_entry(self):
        #create
        self.name_entry = Entry()
        self.name_entry.grid(row=1, column=2)

        #event
        self.name_entry.bind("<FocusOut>", self.__name_box)

    def add_name_check(self):
        #create
        self.name_check = Checkbutton()
        self.name_check.grid(row=1, column=3)

    def add_pass_label(self):
        #create
        self.pass_label = Label()
        self.pass_label.grid(row=2, column=1)

        #style
        self.pass_label.configure(font="arial 8", text="Passport Number:")

    def add_pass_entry(self):
        #create
        self.pass_entry = Entry()
        self.pass_entry.grid(row=2, column=2)

        #event
        self.pass_entry.bind("<FocusOut>", self.__pass_box)

    def add_pass_check(self):
        #create
        self.pass_check = Checkbutton()
        self.pass_check.grid(row=2, column=3)

    def add_night_label(self):
        #create
        self.night_label = Label()
        self.night_label.grid(row=3, column=1)

        #style
        self.night_label.configure(font="arial 8", text="No of Nights:")

    def add_night_entry(self):
        #create
        self.night_entry = Entry()
        self.night_entry.grid(row=3, column=2)

        #event
        self.night_entry.bind("<FocusOut>", self.__check_box)

    def add_night_check(self):
        #create
        self.night_check = Checkbutton()
        self.night_check.grid(row=3, column=3)

    def add_check_button(self):
        #create
        self.check_button = Button()
        self.check_button.grid(row=4, columnspan=3)

        #style
        self.check_button.configure(text="Check In")

    def __name_box(self,event):
        name = (self.name_entry.get())
        if name == "":
            self.name_check.deselect()
            messagebox.showinfo("failed","please input some text")
        else:
            self.name_check.select()

    def __pass_box(self,event):
        name = (self.pass_entry.get())
        if name == "" :
            self.pass_check.deselect()
            messagebox.showerror("failed","please input some text")
        else:
            self.pass_check.select()


    def __check_box(self,event):
        num = int(self.night_entry.get())
        if num < 10:
            self.night_check.select()
        else:
            self.night_check.deselect()
            messagebox.showerror("failed","please select less nights")