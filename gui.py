import tkinter as tk
from Control import *


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        super().__init__(parent, *args, **kwargs)
        self.bg_color = "#B1DDC6"
        self.parent = parent
        self.control = Control()
        self.control.get_card()
        self.card = self.control.card
        self.timer = self.parent.after(3000, lambda: self.flip_card())

        # def set_canvas(self):
        self.card_front_img = tk.PhotoImage(file='./images/card_front.png')
        self.card_back_img = tk.PhotoImage(file='./images/card_back.png')
        self.canvas = tk.Canvas(self, height=525, width=800, bg=self.bg_color, highlightthickness=0)
        self.canvas_bg = self.canvas.create_image(0, 0, image=self.card_front_img, anchor="nw")
        self.canvas.grid(column=1, row=1, columnspan=2, padx=50, pady=(50, 20))

        self.yes_image = tk.PhotoImage(file='./images/right.png')
        self.yes_btn = tk.Button(self, image=self.yes_image, highlightthickness=0, bg=self.bg_color, bd=0, command=lambda: [self.is_known()])
        self.yes_btn.grid(column=1, row=2, pady=(0, 20))

        self.no_image = tk.PhotoImage(file='./images/wrong.png')
        self.no_btn = tk.Button(self, image=self.no_image, highlightthickness=0, bg=self.bg_color, bd=0, command=lambda: [self.next_card()])
        self.no_btn.grid(column=2, row=2, pady=(0, 20))

        self.question_text = self.canvas.create_text(
            400, 150,
            font=('Arial', 40, 'italic'),
            text=self.card.french
        )
        self.answer_text = self.canvas.create_text(
            400, 263,
            font=('Arial', 60, 'bold'),
            text=self.card.english
        )

    def next_card(self):
        self.parent.after_cancel(self.timer)
        self.control.get_card()
        self.card = self.control.card
        self.canvas.itemconfig(self.question_text, text='French')
        self.canvas.itemconfig(self.answer_text, text=self.card.french)
        self.canvas.itemconfig(self.canvas_bg, image=self.card_front_img)
        self.canvas.itemconfig(self.question_text, text='French', fill='black')
        self.timer = self.parent.after(3000, lambda: self.flip_card())

    def flip_card(self):
        self.canvas.itemconfig(self.canvas_bg, image=self.card_back_img)
        self.canvas.itemconfig(self.question_text, text='English', fill='white')
        self.canvas.itemconfig(self.answer_text, text=self.card.english)

    def is_known(self):
        self.control.remove_card(self.card)
        self.control.write_csv()
        self.next_card()

