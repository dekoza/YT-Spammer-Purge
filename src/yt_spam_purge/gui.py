# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

# import YouTubeSpammerPurge as myFunctions

from pathlib import Path
from .utils import make_char_set
import os
import sys

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Menu, TclError, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import END
from functools import partial


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Probably not needed anymore because of resource_path(), but will keep in case
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Checks if the application is running as a pyinstaller bundle, if so, specifies correct path to resources - use resource_path() when specifying resources
# Also need to add to 'datas' in pyinstaller spec file, such as:   a.datas += [('icon.png', '.\\assets\\icon.png', 'DATA')]
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):  # If running as a pyinstaller bundle
        # print("Test1") # For Debugging
        # print(os.path.join(sys._MEIPASS, relative_path)) # For Debugging
        return os.path.join(sys._MEIPASS, relative_path)
    # print("Test2") # for Debugging
    # print(os.path.join(os.path.abspath("assets"), relative_path)) # For debugging
    return os.path.join(
        os.path.abspath("assets"), relative_path
    )  # If running as script, specifies resource folder as /assets


# To allow canvas objects to be updated and called upon, need to create object wrapper
class CanvasObject:
    id = 0

    def __init__(self, canvas, canvas_id):
        self.canvas = canvas  # keep a reference of the canvas
        self.canvas_id = canvas_id  # keep a reference of the item id on the canvas
        self.id = CanvasObject.id  # each CanvasObject has its own unique id
        CanvasObject.id += 1

    def itemconfig(self, **kwargs):
        self.canvas.itemconfig(self.canvas_id, kwargs)


################## RIGHT CLICK MENU ######################
# Code From: https://stackoverflow.com/a/4552646/17312053


def rClicker(e):
    #''' right click context menu for all Tk Entry and Text widgets'''
    try:

        def rClick_Copy(e, apnd=0):
            e.widget.event_generate("<Control-c>")

        def rClick_Cut(e):
            e.widget.event_generate("<Control-x>")

        def rClick_Paste(e):
            e.widget.event_generate("<Control-v>")

        e.widget.focus()

        nclst = [
            (" Cut", lambda e=e: rClick_Cut(e)),
            (" Copy", lambda e=e: rClick_Copy(e)),
            (" Paste", lambda e=e: rClick_Paste(e)),
        ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root + 40, e.y_root + 10, entry="0")

    except TclError:
        print(" - rClick menu, something wrong")
        pass

    return "break"


def rClickbinder(r):
    try:
        for b in ["Text", "Entry", "Listbox", "Label"]:  #
            r.bind_class(b, sequence="<Button-3>", func=rClicker, add="")
    except TclError:
        print(" - rClickbinder, something wrong")
        pass


###################### Main Window ############################

# Function that is called by main program that brings up window to take in user input
def take_input_gui(
    mode, stripLettersNumbers=False, stripKeyboardSpecialChars=False, stripPunctuation=False
):
    validModes = ["string", "chars"]
    if mode not in validModes:
        raise ValueError("Invalid mode. Possible values: 'string' or 'chars'.")

    window = Tk()
    window.title("YT Spammer Purge")
    window.iconphoto(False, PhotoImage(file=resource_path("icon.png")))

    window.geometry("276x279")
    window.configure(bg="#FFFFFF")

    #################### Functions ####################

    # Get text from textbox and then clear the box
    def submit(boxName):
        global returnText
        text = boxName.get()
        boxName.delete("0", END)

        if mode == "chars":
            # Convert characters string to 'set' of characters
            returnText = make_char_set(
                text,
                stripLettersNumbers=stripLettersNumbers,
                stripKeyboardSpecialChars=stripKeyboardSpecialChars,
                stripPunctuation=stripPunctuation,
            )

        outputTextBox.config(state="normal")
        outputTextBox.delete("1.0", END)
        outputTextBox.insert(END, returnText)
        outputTextBox.config(state="disabled")

        if len(returnText) > 0:
            warningMessage.itemconfig(state="hidden")
        elif len(returnText) == 0:
            warningMessage.itemconfig(state="normal")

    def quit():
        global returnText
        returnText = []
        window.destroy()

    def execute():
        try:
            if len(returnText) == 0:
                warningMessage.itemconfig(state="normal")
                pass
            elif len(returnText) > 0:
                window.destroy()
        except NameError:
            warningMessage.itemconfig(state="normal")

    canvas = Canvas(
        window,
        # bg = "#FFFFFF",
        bg="#f0f0f0",
        height=279,
        width=276,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        19.0,
        48.0,
        anchor="nw",
        text="Enter Search Terms:",
        fill="#000000",
        font=("Roboto", 12 * -1),
    )

    canvas.create_text(
        19.0,
        148.0,
        anchor="nw",
        text="Terms will be displayed back here:",
        fill="#000000",
        font=("Roboto", 12 * -1),
    )

    # Bottom text box
    entry_image_1 = PhotoImage(file=resource_path("outputTextBox.png"))
    entry_bg_1 = canvas.create_image(138.5, 186.0, image=entry_image_1)
    outputTextBox = Text(
        bd=0,
        bg="#F8F8F8",
        state="disabled",
        highlightthickness=0,
        # tag="False"
    )
    outputTextBox.place(x=27.0, y=164.0, width=223.0, height=38.0)

    entry_image_2 = PhotoImage(file=resource_path("inputTextBox.png"))
    entry_bg_2 = canvas.create_image(138.5, 85.0, image=entry_image_2)
    inputTextBox = Entry(bd=0, bg="#FCFCFC", highlightthickness=0)
    inputTextBox.place(x=27.0, y=67.0, width=223.0, height=30.0)

    button_image_1 = PhotoImage(file=resource_path("cancelButton.png"))
    cancelButton = Button(
        image=button_image_1, borderwidth=0, highlightthickness=0, command=quit, relief="flat"
    )
    cancelButton.place(
        x=152.0,
        y=225.0,
        # width=78.0,
        # height=32.0,
        width=86.0,
        height=40.0,
    )

    button_image_2 = PhotoImage(file=resource_path("executeButton.png"))
    executeButton = Button(
        image=button_image_2, borderwidth=0, highlightthickness=0, command=execute, relief="flat"
    )
    executeButton.place(
        x=42.0,
        y=225.0,
        # width=78.0,
        # height=32.0
        width=86.0,
        height=40.0,
    )

    canvas.create_text(
        32.0, 8.0, anchor="nw", text="Filter Terms Input", fill="#000000", font=("Roboto", 24 * -1)
    )

    # Submit Button
    button_image_3 = PhotoImage(file=resource_path("inputSubmitButton.png"))
    inputSubmitButton = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(submit, inputTextBox),
        relief="flat",
    )
    inputSubmitButton.place(
        x=174.0,
        y=110.0,
        # width=71.0,
        # height=22.0
        width=78.0,
        height=28.0,
    )

    # Warning about no input
    # Object wrapper for canvas text object, so can update it with warningMessage.itemconfig(state=warningState)
    warningMessage = CanvasObject(
        canvas,
        canvas.create_text(
            19.0,
            105.0,
            anchor="nw",
            text="No valid terms entered!",
            fill="red",
            font=("Roboto", 12 * -1),
            state="hidden",
        ),
    )

    inputTextBox.bind("<Button-3>", rClicker, add="")  # Binds right click menu to inputTextBox only

    window.resizable(False, False)
    window.mainloop()
    try:
        window.update()
    except Exception as e:
        if "destroyed" in str(e):
            pass
    return returnText


# take_input_gui() # For testing this module in standalone, uncomment
