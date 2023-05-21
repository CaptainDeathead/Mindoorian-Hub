import tkinter
import nationstates

class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.root = tkinter.Tk()
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        #make the window frameless
        self.root.overrideredirect(True) 
        #add a background colour
        self.root.configure(bg='#7FFFD4')
        
    def nationstates(self):
        # Create a large label
        label = tkinter.Label(self.root, text="Mindoorian Hub!", font=("Arial", 24), fg="black", bg="#7FFFD4")
        label.place(relx=0.5, rely=0.2, anchor="center")

        # Create a small label
        label = tkinter.Label(self.root, text="Enter your username", font=("Times", 16), fg="black", bg="#7FFFD4")
        label.place(relx=0.5, rely=0.4, anchor="center")
        
        # Add an entry thign to the window
        entry = tkinter.Entry(self.root, font=("Arial", 16), fg="black", bg="white")
        entry.place(relx=0.5, rely=0.5, anchor="center")

        # Add a button to the window
        button = tkinter.Button(self.root, text="Submit", font=("Arial", 13), fg="white", bg="grey", command=lambda: print(entry.get()))
        button.place(relx=0.5, rely=0.6, anchor="center")
        
    def nationstates_submit(self):
        #nation_name = self.nationstates_entry.get()
        #nation = nationstates.Nationstates(nation_name)
        #self.nationstates_name_label.config(text=nation.get_nation_name())
        pass
        
    def run(self):
        self.nationstates()
        self.root.mainloop()
        e = "e"
        return e
    
        
window = Window("Nationstates", 1100 , 575).run()
