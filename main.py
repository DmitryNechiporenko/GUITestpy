import tkinter as tk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


if __name__ == "__main":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x400+300+200")
    root.resizable(False, False)
    root.mainloop()
