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
        self.__add_entry_frame()
        self.__add_button()
        self.__add_song_entry()
        self.__add_lyric_label()
        self.__add_listbox()
        
        

    def __add_heading_label(self):
        # create   
        self.heading_label = Label()
        self.heading_label.pack()
        
        # style
        self.heading_label.configure(font="Arial 14", text="Song Maker")
        

    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.pack()

        #style
        self.instruction_label.configure(font="Arial 8", text="Lyric to add:")
        

    def __add_entry_frame(self):
        #create
        self.entry_frame = Frame()
        self.entry_frame.pack()


    def __add_button(self):
        #create
        self.entry_button = Button(self.entry_frame)
        self.entry_button.pack(side=RIGHT)

        #style
        self.entry_button.configure(text="Add")

        #event
        self.entry_button.bind("<ButtonRelease-1>", self.__buy_button_clicked) 


    def __add_song_entry(self):
        #create
        self.song_entry = Entry(self.entry_frame)
        self.song_entry.pack(side=LEFT)

    def __add_lyric_label(self):
        #create
        self.lyric_label = Label()
        self.lyric_label.pack()

        #style
        self.lyric_label.configure(font="Arial 8", text="Lyrics:")
    
    def __add_listbox(self):
        #create
        self.listbox = Listbox()
        self.listbox.pack()

        #style
        self.listbox.configure(height=2)


    def __buy_button_clicked(self, event):
        num = int(self.ticket_entry.get())
        if num == 1:
            messagebox.showinfo("Purchased!", "You have purchased "+ str(num) + " ticket!")
        elif num > 1:
            messagebox.showinfo("Purchased!", "You have purchased "+ str(num) + " tickets!")
        else:
            messagebox.showinfo("You have entered an invalid number of tickets!")