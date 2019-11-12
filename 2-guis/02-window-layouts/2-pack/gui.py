from tkinter import *

class Gui(Tk):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="light grey", height=174, width=333)
        
        self.add_heading_label()

        self.add_small_label()
        
        self.add_email_frame()
                
        self.add_entry_label()

        self.add_email_entry()

        self.add_sub_button()
    
        
    def add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.pack() 
        
        # style
        self.heading_label.configure(font="Arial 14", text="RECIEVE OUR NEWSLETTER")
    
    def add_small_label(self):
        #create
        self.small_label = Label()
        self.small_label.pack()

        #style
        self.small_label.configure(font="Arial 8", text="Please enter your email below to recieve our newsletter.")
    
    def add_email_frame(self):
        #create
        self.email_frame = Frame()
        self.email_frame.pack()

    def add_entry_label(self):
        #create
        self.entry_label = Label(self.email_frame)
        self.entry_label.pack(side=LEFT)

        #style
        self.entry_label.configure(font="Arial 8", text="Email:")

    def add_email_entry(self):
        #create
        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack(side=RIGHT)
    
    def add_sub_button(self):
        #create
        self.sub_button = Button()
        self.sub_button.pack()

        #style
        self.sub_button.configure(text="Subscribe", bg="light salmon", height=1, width=44)


