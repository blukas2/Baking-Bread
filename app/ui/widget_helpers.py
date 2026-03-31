# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import END

from config import ENTRY_WIDTH, ENTRY_BORDER, DROPDOWN_WIDTH


def create_entry(parent):
    return tk.Entry(parent, width=ENTRY_WIDTH, borderwidth=ENTRY_BORDER)


def create_dropdown(parent, variable, options):
    dropdown = tk.OptionMenu(parent, variable, *options)
    dropdown.config(width=DROPDOWN_WIDTH)
    return dropdown


def update_entry(entry, value):
    entry.delete(0, END)
    entry.insert(0, value)


def create_ingredient_row(parent, variable, options, row, col_start):
    dropdown = create_dropdown(parent, variable, options)
    dropdown.grid(row=row, column=col_start)
    percentage_entry = create_entry(parent)
    percentage_entry.grid(row=row, column=col_start + 1)
    weight_entry = create_entry(parent)
    weight_entry.grid(row=row, column=col_start + 2)
    return dropdown, percentage_entry, weight_entry


def create_labeled_row(parent, label_text, row, col_start):
    label = tk.Label(parent, text=label_text)
    label.grid(row=row, column=col_start)
    percentage_entry = create_entry(parent)
    percentage_entry.grid(row=row, column=col_start + 1)
    weight_entry = create_entry(parent)
    weight_entry.grid(row=row, column=col_start + 2)
    return label, percentage_entry, weight_entry


def add_separator(parent, row, col_start, orient=tk.HORIZONTAL, span=3):
    separator = tk.ttk.Separator(parent, orient=orient)
    separator.grid(row=row, column=col_start, columnspan=span, sticky='ew')
    return separator
