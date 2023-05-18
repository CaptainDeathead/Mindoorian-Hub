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
        
    def nationstates(self):
        # make a frame
        self.nationstates_frame = tkinter.Frame(self.root)
        self.nationstates_frame.pack()
        
        # make a label
        self.nationstates_label = tkinter.Label(self.nationstates_frame, text="Nationstates")
        self.nationstates_label.pack()
        
        nation_name = ""
        
        # make a label that holds the name of the nation
        self.nationstates_name_label = tkinter.Label(self.nationstates_frame, text=nation_name)
        self.nationstates_name_label.pack()
    
        # make text entry
        self.nationstates_entry = tkinter.Entry(self.nationstates_frame)
        self.nationstates_entry.pack()
        
        # make a button to submit the entry to the nationstates module
        self.nationstates_button = tkinter.Button(self.nationstates_frame, text="Submit", command=self.nationstates_submit)
        self.nationstates_button.pack()
        
    def nationstates_submit(self):
        nation_name = self.nationstates_entry.get()
        nation = nationstates.Nationstates(nation_name)
        self.nationstates_name_label.config(text=nation.get_nation_name())
        
    def run(self):
        self.nationstates()
        self.root.mainloop()
        
window = Window("Nationstates", 500, 500).run()