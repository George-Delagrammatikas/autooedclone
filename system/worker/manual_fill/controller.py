import numpy as np
import tkinter as tk
from .view import ManualFillView


class ManualFillController:

    def __init__(self, root_controller):
        self.root_controller = root_controller
        self.root_view = self.root_controller.view

        n_obj = self.root_controller.problem_info['n_obj']

        self.view = ManualFillView(self.root_view, n_obj)

        self.view.widget['disp_n_row'].config(
            default=1, 
            valid_check=lambda x: x > 0,
            error_msg='number of rows must be positive',
        )
        self.view.widget['disp_n_row'].set(1)
        self.view.widget['set_n_row'].configure(command=self.update_table)

        table = self.root_controller.view.widget['db_table']
        self.view.widget['performance_excel'].config(
            valid_check=[lambda x: x > 0 and x <= table.n_rows] + [lambda x: True] * n_obj,
        )

        self.view.widget['save'].configure(command=self.add_performance)
        self.view.widget['cancel'].configure(command=self.view.window.destroy)

    def update_table(self):
        '''
        Update excel table of design variables to be added
        '''
        n_row = self.view.widget['disp_n_row'].get()
        self.view.widget['performance_excel'].update_n_row(n_row)

    def add_performance(self):
        '''
        Add performance values
        '''
        try:
            rowids = self.view.widget['performance_excel'].get_column(0)
            if len(np.unique(rowids)) != len(rowids):
                raise Exception('Duplicate row numbers')
        except:
            tk.messagebox.showinfo('Error', 'Invalid row numbers', parent=self.view.window)
            return

        # check if locked
        locked_rows = []
        for rowid in rowids:
            locked = self.root_controller.check_entry(rowid)
            if locked:
                locked_rows.append(rowid)
        if len(locked_rows) > 0:
            tk.messagebox.showinfo('Locked', f'Rows {locked_rows} are locked, cannot proceed')
            return

        n_obj = self.root_controller.problem_info['n_obj']
        table = self.root_controller.view.widget['db_table']

        # check for overwriting
        overwrite = False
        for rowid in rowids:
            for i in range(n_obj):
                if table.get(rowid - 1, f'f{i + 1}') != 'N/A':
                    overwrite = True
        if overwrite and tk.messagebox.askquestion('Overwrite Data', 'Are you sure to overwrite evaluated data?', parent=self.view.window) == 'no': return

        try:
            Y = self.view.widget['performance_excel'].get_grid(column_start=1)
        except:
            tk.messagebox.showinfo('Error', 'Invalid performance values', parent=self.view.window)
            return
        
        self.view.window.destroy()

        # update database
        self.root_controller.update_data(Y, rowids)