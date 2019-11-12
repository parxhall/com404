from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="light grey")
        
        self.add_heading_label()

        self.add_small_label()

        self.add_entry_label()

        self.add_email_entry()

        self.add_sub_button()
        
    
    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)
        
        # style
        self.heading_label.configure(font="Arial 14", text="RECIEVE OUR NEWSLETTER")
    
    def add_small_label(self):
        #create
        self.small_label = Label()
        self.small_label.grid(row=1, column=0, columnspan=2)

        #style
        self.small_label.configure(font="Arial 8", text="Please enter your email below to recieve our newsletter.")
    
    def add_entry_label(self):
        #create
        self.entry_label = Label()
        self.entry_label.grid(row=2, column=0, columnspan=1)

        #style
        self.entry_label.configure(font="Arial 8", text="Email:")

    def add_email_entry(self):
        #create
        self.email_entry = Entry()
        self.email_entry.grid(row=2, column=1, columnspan=1)
    
    def add_sub_button(self):
        #create
        self.sub_button = Button()
        self.sub_button.grid(row=3, column=0, columnspan=2)

        #style
        self.sub_button.configure(text="Subscribe", bg="light salmon", height=1, width=44)


