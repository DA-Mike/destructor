import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from os import getenv
from dotenv import load_dotenv
from PIL import ImageTk, Image
from utils import destructor as d

load_dotenv()


class App:
    """This is the application and GUI"""

    def __init__(self):
        self.window = tk.Tk()
        self.ph1 = tk.PhotoImage(file=getenv("ICON_PATH"))
        self.window.iconphoto(False, self.ph1)
        self.window.title("DESTRUCTOR")
        self.window.geometry("720x625")

        self.mainframe = ttk.Frame(self.window, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(tk.NSEW))
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.elmo = Image.open("./images/elmo.jpg")
        self.elmo = self.elmo.resize((300, 150))
        self.elmo_obj = ImageTk.PhotoImage(self.elmo)

        ttk.Label(
            self.mainframe,
            text="Welcome to Destructor",
            padding="5",
            font=("Arial", 25),
            justify="center",
        ).grid(column=2, row=1)
        ttk.Label(
            self.mainframe,
            image=self.elmo_obj,
            padding="5",
            justify="center",
            background="black",
        ).grid(column=2, row=2, pady=10)
        ttk.Label(self.mainframe, text="Starting Directory", padding="5").grid(
            column=1, row=3, sticky=tk.E
        )

        self.folder_path = tk.StringVar()
        self.path = tk.StringVar()
        self.path_entry = tk.Entry(
            self.mainframe, textvariable=self.folder_path, justify="center"
        )
        self.path_entry.grid(column=2, row=3, pady=10, sticky=tk.EW)
        self.path_entry.focus()

        self.frame1 = ttk.Frame(self.mainframe)
        self.frame1.grid(column=2, row=4, sticky=tk.NSEW, pady=10)
        self.seek = ttk.Button(
            self.frame1, text="Seek", padding=5, command=lambda: self.seek_handler()
        ).grid(column=1, row=1, sticky=tk.W, padx=100)
        self.destroy = ttk.Button(
            self.frame1, text="Destroy", padding=5, command=lambda: self.verify()
        ).grid(column=4, row=1, stick=tk.E, padx=50)

        self.btn_find = ttk.Button(
            self.mainframe, text="Browse", command=lambda: self.get_folder_path()
        )
        self.btn_find.grid(row=3, column=4, padx=10)

        self.msg_frame = ttk.Frame(self.mainframe)
        self.msg_frame.grid(column=2, row=5, sticky=tk.NSEW)
        self.msg_frame.config(height=200, width=500)
        self.msg_box = tk.Text(
            self.msg_frame,
            background="white",
            width=60,
            height=15,
            relief="solid",
            borderwidth=1,
            state="disabled",
            fg="black",
        )
        self.msg_box.grid(column=2, row=2, sticky=tk.W, pady=30)

        self.window.mainloop()

    def choice(self, option):
        """Handles destroy/deletion of node_modules in selected path
        after user selects 'yes' from verification modal"""

        pop.destroy()
        if option == "yes":
            result = d.destroy(self.folder_path.get())
            self.msg_box.config(state="normal")
            self.msg_box.insert(tk.INSERT, "\n" + result[0] + "\n" + result[1])
            self.msg_box.config(state="disabled")

    def seek_handler(self):
        """Initiates seek function, insterts results into text module"""

        result = d.seek(self.folder_path.get())
        self.msg_box.config(state="normal")
        self.msg_box.insert(tk.INSERT, "\n" + result[0] + "\n" + result[1])
        self.msg_box.config(state="disabled")

    def verify(self):
        """Validates that the user wants to proceed with
        deleting node_modules directories"""

        global pop
        pop = tk.Toplevel(self.window)
        pop.geometry("300x200")
        ph2 = tk.PhotoImage(file=getenv("ICON_PATH"))
        pop.iconphoto(False, ph2)
        label = tk.Label(
            pop,
            text="Are you sure? \n This will permanently delete all node_modules directories in this path.",
            font=("Arial", 10),
            wraplength=200,
        )
        label.pack(pady=20)
        frame = tk.Frame(pop)
        frame.pack(pady=10)
        ok_button = tk.Button(
            frame, text="Yes", command=lambda: self.choice("yes"), fg="black"
        )
        ok_button.grid(row=2, column=1, padx=10)
        ok_button.config(padx=10)
        cancel_button = tk.Button(
            frame, text="No", command=lambda: self.choice("no"), fg="black"
        )
        cancel_button.grid(row=2, column=2, padx=10)
        cancel_button.config(padx=10)

    def get_folder_path(self):
        """Gets directory path from user"""
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)


App()
