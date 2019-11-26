from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.ambulance_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/1-loading/plane.gif")
        
        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_ambulance_image_label()
        self.add_bike_image_label()
        self.add_plane_image_label()
        self.add_main_label()

    def add_main_label(self):
        #create
        self.main_label = Label()
        self.main_label.grid(row=0, columnspan=3)

        #style
        self.main_label.configure(font="arial 13", text="TRANSPORT")
        
    def add_ambulance_image_label(self):
        #create
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        
        #style
        self.ambulance_image_label.configure(image=self.ambulance_image,
                                             height=60,
                                             width=60)

    def add_bike_image_label(self):
        #create
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=1)
        
        #style
        self.ambulance_image_label.configure(image=self.bike_image,height=60,width=60)
 
    def add_plane_image_label(self):
        #create
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=2)
        
        #style
        self.ambulance_image_label.configure(image=self.plane_image,height=60,width=60)