from tkinter import *
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()
        
        # load resources
        self.ball_image = PhotoImage(file="//filestore.soton.ac.uk/users/ph2r19/mydocuments/University Work/5) Programming/com404/2-guis/05-animation/1-single-object/ball1.gif")
        
        # set window attributes
        self.title("Animation")
        self.configure(height=500,
                       width=500)

        # set animation attributes
        self.ball_x_pos = 230
        self.ball_y_pos = 10
        self.ball_x_change = 1
        self.ball_y_change = 1
        
        # add components
        self.add_ball_image_label() 
        
        # start the timer
        self.tick()
        
    # the timer tick function    
    def tick(self):
        if self.ball_x_pos == 0 or self.ball_x_pos == 400:
            self.ball_x_change *= -1
        if self.ball_y_pos == 0 or self.ball_y_pos == 400:
            self.ball_y_change *= -1

        self.ball_x_pos = self.ball_x_pos + self.ball_x_change
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_image_label.place(x=self.ball_x_pos, 
                                    y=self.ball_y_pos)
        self.after(10, self.tick)

    # the ball image
    def add_ball_image_label(self):
        #create
        self.ball_image_label = Label()
        self.ball_image_label.place(x=self.ball_x_pos,
                                    y=self.ball_y_pos)
        #style
        self.ball_image_label.configure(image=self.ball_image)
     
# the object
if __name__ == "__main__":
    gui = AnimatedGui()    
    gui.mainloop() 