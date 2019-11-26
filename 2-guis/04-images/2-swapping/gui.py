from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()
        
        # load resources
        self.cactus_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/2-swapping/cactus.gif")
        self.catcus_name = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/04-images/2-swapping/bike.gif")

        # set window attributes
        self.title("Gui")
        
        # add components
        self.add_cactus_image_label()
        self.add_main_label()
        self.add_flip_button()

    def add_main_label(self):
        #create
        self.main_label = Label()
        self.main_label.grid(row=0)

        #style
        self.main_label.configure(font="arial 20", text="Cactus Leaves")
        
    def add_cactus_image_label(self):
        #create
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1)
        
        #style
        self.cactus_image_label.configure(image=self.cactus_image,
                                             height=300,
                                             width=400)

    def add_flip_button(self):
        #create
        self.flip_button = Button()
        self.flip_button.grid(row=2)

        #style
        self.flip_button.configure(font="arial 20", text="Flip", height=2, width=10)

        #event
        self.flip_button.bind("<ButtonRelease-1>", self.__left_button_clicked)
        self.flip_button.bind("<ButtonRelease-3>", self.__right_button_clicked)
        

    def __left_button_clicked(self, event):
        self.cactus_image_label.configure(image= self.catcus_name)

    def __right_button_clicked(self, event):
        self.cactus_image_label.configure(image= self.cactus_image)

