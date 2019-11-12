from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="light grey", height=174, width=333)
    
        self.add_main_canvas()
        
        self.add_heading_label()

        self.add_small_label()

        self.add_entry_label()

        self.add_email_entry()

        self.add_sub_button()


    def add_main_canvas(self):
        #create 
        self.main_canvas = Canvas()
        self.main_canvas.place(x=10, y=10)

        # style
        self.main_canvas.configure(height=150, width=310)
        
    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.place(x=25, y=20)
        
        # style
        self.heading_label.configure(font="Arial 14", text="RECIEVE OUR NEWSLETTER")
    
    def add_small_label(self):
        #create
        self.small_label = Label()
        self.small_label.place(x=22, y=70)

        #style
        self.small_label.configure(font="Arial 8", text="Please enter your email below to recieve our newsletter.")
    
    def add_entry_label(self):
        #create
        self.entry_label = Label()
        self.entry_label.place(x=50, y=110)

        #style
        self.entry_label.configure(font="Arial 8", text="Email:")

    def add_email_entry(self):
        #create
        self.email_entry = Entry()
        self.email_entry.place(x=110, y=110)
    
    def add_sub_button(self):
        #create
        self.sub_button = Button()
        self.sub_button.place(x=10, y=140)

        #style
        self.sub_button.configure(text="Subscribe", bg="light salmon", height=1, width=44)


