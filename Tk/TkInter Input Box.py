.
from tkinter import *
from functools import partial


class global_variables:
    def __init__(self):
        pass

    Case_Name = ''
    USB_Drive = ''


class user_form(object):
    def __init__(self):
        self.root = Tk()

    @property
    def input_form(self):
        self.root.title('Case Information ')
        frame = Frame(self.root, pady=10)
        form_data = dict()
        form_fields = ['Case Name', 'USB Drive']  # Add dict entries to this dict to add more fields IN ORDER
        cnt = 0
        for form_field in form_fields:
            Label(frame, text=form_field, anchor=NW).grid(row=cnt, column=1, pady=5, padx=(10, 1), sticky="W")
            textbox = Text(frame, height=1, width=15)
            form_data.update({form_field: textbox})
            textbox.grid(row=cnt, column=2, pady=5, padx=(3, 20))
            cnt += 1

        set_global_variables = partial(self.set_vars, form_data=form_data)
        Button(frame, text='Submit', width=15, command=set_global_variables).grid(row=cnt, column=2, pady=5,
                                                                                  padx=(3, 20))
        frame.pack()

        self.root.mainloop()

    def set_vars(self, form_data):
        data = {k: v.get('1.0', END).strip() for k, v in form_data.items()}
        # validate data or do anything you want with it if needed here
        global_variables.Case_Name = data['Case Name']
        global_variables.USB_Drive = data['USB Drive']
        # Add more variables to these lines to make the entries available use the Dict entries from input_form
        self.root.destroy()  # quits tkinter


if __name__ == '__main__':
    global_variables()
    selection = user_form()
    selection.input_form
    print('this is from the tkinter class ' + global_variables.Case_Name)