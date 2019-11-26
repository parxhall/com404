from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.bus_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/3-positioning/bus.gif")
        self.map_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/3-positioning/map.gif")

        # set window attributes
        self.title("Gui")

        #load components
        self.add_map_frame()
        self.add_map_image_label()
        self.add_bus_image_label()
        
    def add_map_frame(self):
        #create
        self.map_frame = Frame()

        #style
        self.map_frame.configure(width=400, height=400)

    def add_map_image_label(self):
        #create
        self.map_image_label = Label()
        self.map_image_label.place(x=0, y=0)

        #style
        self.map_image_label.configure(image=self.map_image, width=400, height=400)

        #event
        self.map_image_label.bind("<B1-Motion>", self.__bus_move)

    def add_bus_image_label(self):
        #create
        self.bus_image_label = Label()
        self.bus_image_label.place(x=20, y=20)

        #style
        self.bus_image_label.configure(image=self.bus_image, width=100, height=100)


    def __bus_move(self,event):
        self.bus_image_label.place(x=event.x,y=event.y)
