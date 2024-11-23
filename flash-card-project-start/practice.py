from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('../flash-card-project-start/data/french_words.csv')
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(canvas_image, image=card_front_image)# Display French word initially
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')  # Display English word after clicking
    canvas.itemconfig(canvas_image, image=card_back_image)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='../flash-card-project-start/images/card_front.png')
card_back_image = PhotoImage(file='../flash-card-project-start/images/card_back.png')
right_image = PhotoImage(file='../flash-card-project-start/images/right.png')
wrong_image = PhotoImage(file='../flash-card-project-start/images/wrong.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()  # Initialize the first card

window.mainloop()
