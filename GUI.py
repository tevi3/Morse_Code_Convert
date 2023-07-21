from tkinter import *
from tkinter import messagebox
from morse_code_covert import encrypt, decrypt


PINK = "#e2979c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


class MorseCodeGui:

    def __init__(self, window):
        self.option = ['ENG', 'MORSE CODE']
        self.option_value_1 = StringVar(window)
        self.option_value_1.set('ENG or MORSE')
        self.option_value_2 = StringVar(window)
        self.option_value_2.set('ENG or MORSE')

        self.window = window
        window.title('Morse Code Convert')
        window.geometry('800x600')
        window.config(padx=100, pady=30, bg=YELLOW)

        self.label_1 = Label(window, text='Input', fg=PINK, bg=YELLOW, font=(FONT_NAME, 20), width=7)
        self.label_1.grid(row=0, column=0)
        self.label_2 = Label(window, text='From', fg=PINK, bg=YELLOW, font=(FONT_NAME, 20), width=7)
        self.label_2.grid(row=1, column=0, pady=10)
        self.label_3 = Label(window, text='To', fg=PINK, bg=YELLOW, font=(FONT_NAME, 20), width=7)
        self.label_3.grid(row=2, column=0, pady=10)
        self.label_4 = Label(window, text='Output', fg=PINK, bg=YELLOW, font=(FONT_NAME, 20), width=7)
        self.label_4.grid(row=4, column=0)

        self.input_field = Text(window, height=13, width=60, font=FONT_NAME, highlightthickness=0)
        self.input_field.grid(row=0, column=1, padx=10)
        self.output_field = Text(window, height=13, width=60, font=FONT_NAME, highlightthickness=0)
        self.output_field.grid(row=4, column=1, padx=10)

        self.from_option = OptionMenu(window, self.option_value_1, *self.option)
        self.from_option.grid(row=1, column=1)
        self.to_option = OptionMenu(window, self.option_value_2, *self.option)
        self.to_option.grid(row=2, column=1)

        self.covert_btn = Button(window, text='Convert', command=self.convert, highlightbackground=YELLOW)
        self.covert_btn.grid(row=3, column=1, pady=10)
        self.clear_btn = Button(window, text='Clear', command=self.clear, highlightbackground=YELLOW)
        self.clear_btn.grid(row=5, column=1, pady=10)

    def convert(self):

        message = self.input_field.get(1.0, 'end-1c')

        if self.option_value_1.get() == self.option_value_2.get():
            messagebox.showerror(message="Do not choose same thing.")
            return
        elif self.option_value_1.get() == 'ENG' and self.option_value_2.get() == 'MORSE CODE':
            result = encrypt(message)
        elif self.option_value_1.get() == 'MORSE CODE' and self.option_value_2.get() == 'ENG':
            result = decrypt(message)
        else:
            messagebox.showerror(message="Please check again typed message is valid.")
            return

        self.output_field.insert('end-1c', result)

    def clear(self):
        self.input_field.delete(1.0, 'end-1c')
        self.output_field.delete(1.0, 'end-1c')