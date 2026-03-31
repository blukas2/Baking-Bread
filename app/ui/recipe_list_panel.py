# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import END

from config import TITLE_FONT


class RecipeListPanel(tk.Frame):

    def __init__(self, parent, on_select, on_save, on_save_as, on_delete, on_rename, on_update):
        super().__init__(parent)
        self._on_select = on_select
        self._build_title()
        self._build_listbox()
        self._build_buttons(on_save, on_save_as, on_delete, on_rename, on_update)
        self._build_comments()

    def _build_title(self):
        label = tk.Label(self, text="Recipe List", font=TITLE_FONT, anchor=tk.CENTER)
        label.grid(row=0, column=0, columnspan=4)

    def _build_listbox(self):
        self._listbox = tk.Listbox(self, height=5, exportselection=False)
        self._listbox.grid(row=1, column=0, columnspan=4, rowspan=5, sticky="nsew")
        self._listbox.bind('<<ListboxSelect>>', self._on_listbox_select)

    def _build_buttons(self, on_save, on_save_as, on_delete, on_rename, on_update):
        row = 6
        tk.Button(self, text="Save as..", command=on_save_as).grid(row=row, column=0)
        tk.Button(self, text="Save", command=on_save).grid(row=row, column=1)
        tk.Button(self, text="Delete", command=on_delete).grid(row=row, column=2)
        tk.Button(self, text="Rename", command=on_rename).grid(row=row, column=3)
        tk.Button(self, text="Update dataset", command=on_update).grid(
            row=row + 1, column=0, columnspan=4, sticky="ew")

    def _build_comments(self):
        tk.Label(self, text="Comments", font=TITLE_FONT, anchor=tk.CENTER).grid(
            row=8, column=0, columnspan=5)
        self._comments = tk.Text(self, width=20, height=5)
        self._comments.grid(row=9, column=0, columnspan=5, rowspan=7, sticky="nsew")

    def _on_listbox_select(self, event):
        name = self.get_selected_name()
        if name is not None:
            self._on_select(name)

    def get_selected_name(self):
        selection = self._listbox.curselection()
        if not selection:
            return None
        return self._listbox.get(selection)

    def refresh_list(self, names):
        self._listbox.delete(0, END)
        for name in names:
            self._listbox.insert(0, name)

    def get_comments(self):
        return self._comments.get("1.0", END)

    def set_comments(self, text):
        self._comments.delete("1.0", END)
        self._comments.insert(tk.INSERT, text)
