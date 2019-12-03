from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.yoda_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/05-animation/3-varying-ticks/yoda.gif")
        self.yoda1_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/05-animation/3-varying-ticks/yoda1.gif")

        # set window attributes
        self.title("Animation")
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.yoda_x_pos = 250
        self.yoda_y_pos = 10
        self.yoda1_x_pos = 500
        self.yoda1_y_pos = 150

        self.x_change = 1
        self.x1_change = 1

        self.tick_num = 0
        
        # add components
        self.add_yoda_image_label() 
        self.add_yoda1_image_label()
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if (self.tick_num % 4 == 0):
            self.x_change *= -1
        if self.tick_num % 100 == 0:
            self.x1_change *= -1

        self.yoda_x_pos = self.yoda_x_pos + self.x_change
        self.yoda1_x_pos = self.yoda1_x_pos + self.x1_change
        self.yoda_image_label.place(x=self.yoda_x_pos, 
                                    y=self.yoda_y_pos)
        self.yoda1_image_label.place(x=self.yoda1_x_pos, 
                                    y=self.yoda1_y_pos)

        self.tick_num +=1
        self.after(10, self.tick)

    # the yoda image
    def add_yoda_image_label(self):
        #create
        self.yoda_image_label = Label()
        self.yoda_image_label.place(x=self.yoda_x_pos,
                                    y=self.yoda_y_pos)
        #style
        self.yoda_image_label.configure(image=self.yoda_image)

    # the yoda1 image
    def add_yoda1_image_label(self):
        #create
        self.yoda1_image_label = Label()
        self.yoda1_image_label.place(x=self.yoda1_x_pos,
                                    y=self.yoda1_y_pos)
        #style
        self.yoda1_image_label.configure(image=self.yoda1_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 