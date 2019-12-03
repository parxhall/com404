from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.yoda_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/05-animation/2-multiple-components/yoda.gif")

        # set window attributes
        self.title("Animation")
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.yoda_x_pos = 0
        self.yoda_y_pos = 100

        self.x_change = 1
        self.y_change = 1

        # add components
        self.add_yoda_image_label() 
        self.add_up_button()

        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        self.yoda_x_pos = self.yoda_x_pos + self.x_change
        self.yoda_y_pos = self.yoda_y_pos + self.y_change

        self.yoda_image_label.place(x=self.yoda_x_pos, 
                                    y=self.yoda_y_pos)

        self.after(10, self.tick)

    # the yoda image
    def add_yoda_image_label(self):
        #create
        self.yoda_image_label = Label()
        self.yoda_image_label.place(x=self.yoda_x_pos,
                                    y=self.yoda_y_pos)
        #style
        self.yoda_image_label.configure(image=self.yoda_image)
     
    def add_up_button(self):
        #create
        self.up_button = Button()
        self.up_button.place(x=150, y=450)
        #style
        self.up_button.configure(font="arial 20", text="UP/DOWN")

        #event
        self.up_button.bind("<ButtonRelease-1>", self.__up_button_clicked)
        

    def __up_button_clicked(self, event):
        self.y_change *= -1

# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 