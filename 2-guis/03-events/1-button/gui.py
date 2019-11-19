from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)
        
        # style
        self.heading_label.configure(font="Arial 14", text="Entrance Ticket")
        
    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, sticky=W)

        #style
        self.instruction_label.configure(font="Arial 8", text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        #create
        self.ticket_entry = Entry()
        self.ticket_entry.grid(row=2, column=0, columnspan=1)

        
    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0, columnspan=2)

        #style
        self.buy_button.configure(text="Buy")

        #event
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
        

    def __buy_button_clicked(self, event):
        num = int(self.ticket_entry.get())
        if num == 1:
            messagebox.showinfo("Purchased!", "You have purchased "+ str(num) + " ticket!")
        elif num > 1:
            messagebox.showinfo("Purchased!", "You have purchased "+ str(num) + " tickets!")
        else:
            messagebox.showinfo("You have entered an invalid number of tickets!")