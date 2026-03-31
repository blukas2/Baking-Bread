# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import END

from config import TITLE_FONT


def show_info(parent, title, message):
    dialog = tk.Toplevel(parent)
    dialog.title(title)
    label = tk.Label(dialog, text=message, anchor=tk.CENTER)
    label.pack(pady=10)
    ok_button = tk.Button(dialog, text="OK", width=8, command=dialog.destroy)
    ok_button.pack(pady=10)


def show_confirmation(parent, title, message, on_yes):
    dialog = tk.Toplevel(parent)
    dialog.title(title)
    label = tk.Label(dialog, text=message, anchor=tk.CENTER, font=TITLE_FONT)
    label.pack(pady=10)
    button_frame = tk.Frame(dialog)
    button_frame.pack()
    _add_yes_no_buttons(button_frame, dialog, on_yes)


def _add_yes_no_buttons(frame, dialog, on_yes):
    def confirm():
        on_yes()
        dialog.destroy()
    yes_button = tk.Button(frame, text="Yes", width=8, command=confirm)
    yes_button.pack(side=tk.LEFT, padx=10, pady=10)
    no_button = tk.Button(frame, text="No", width=8, command=dialog.destroy)
    no_button.pack(side=tk.RIGHT, padx=10, pady=10)


def show_input_dialog(parent, title, prompt, on_ok):
    dialog = tk.Toplevel(parent)
    dialog.title(title)
    label = tk.Label(dialog, text=prompt, anchor=tk.CENTER, font=TITLE_FONT)
    label.pack(pady=10)
    name_var = tk.StringVar()
    entry = tk.Entry(dialog, width=20, borderwidth=5, textvariable=name_var)
    entry.pack()
    button_frame = tk.Frame(dialog)
    button_frame.pack()
    _add_ok_cancel_buttons(button_frame, dialog, name_var, on_ok)


def _add_ok_cancel_buttons(frame, dialog, name_var, on_ok):
    def confirm():
        on_ok(name_var.get())
        dialog.destroy()
    ok_button = tk.Button(frame, text="OK", width=8, command=confirm)
    ok_button.pack(side=tk.LEFT, padx=10, pady=10)
    cancel_button = tk.Button(frame, text="Cancel", width=8, command=dialog.destroy)
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)
