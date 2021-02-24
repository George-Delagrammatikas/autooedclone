import tkinter as tk
from system.gui.widgets.factory import create_widget


class ScientistInitView:

    def __init__(self, root):
        self.root = root

        frame_init = tk.Frame(master=self.root)
        frame_init.grid(row=0, column=0, padx=20, pady=20)

        create_widget('logo', master=frame_init, row=0, column=0, columnspan=3)

        self.widget = {}
        self.widget['create_task'] = create_widget('button', master=frame_init, row=1, column=0, text='Create Task')
        self.widget['load_task'] = create_widget('button', master=frame_init, row=1, column=1, text='Load Task')
        self.widget['remove_task'] = create_widget('button', master=frame_init, row=1, column=2, text='Remove Task')
