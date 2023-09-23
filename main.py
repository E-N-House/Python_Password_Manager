from tkinter import *
import math

# ----------------------------      CONSTANTS      ------------------------------- #
PROJECT_NAME = "Password Manager"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200
PADDING_WINDOW = 20
COLOR_PRIMARY = "white"
COLOR_SECOND = "yellow"
COLOR_THIRD = "#e2979c"
COLOR_ERRORS = "#e7305b"

LABEL_FONT = ("Arial", 10)
LABEL_TEXT_COLOR = "black"
LABEL_BG_COLOR = "light blue"
LABEL_COLUMN_START = 0
LABEL_ROW_START = 1

BUTTON_PAD_Y = 5
BUTTON_PAD_X = 5

FORM_BG_COLOR = "light yellow"
FORM_ENTRY_WIDTH = 45

PASSWORD_ENTRY_WIDTH = 27

ADD_BUTTON_WIDTH = 36

FONT_NAME = "Courier"
BOLDED_FONT = ("Arial", 26, "bold")
LOGO_FILE = "logo.png"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# creating tk window
window = Tk()
window.config(bg=COLOR_PRIMARY, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pady=PADDING_WINDOW,
              padx=PADDING_WINDOW)
window.title(PROJECT_NAME)

# Creating canvas
canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background=COLOR_PRIMARY, 
                highlightthickness=0)
# adding IMAGE logo to middle of screen using a grid system
logo_img = PhotoImage(file=LOGO_FILE)
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=logo_img)
canvas.grid(column=1, row=0)

# FORM LABELS
website_label = Label(text="Website:", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                      font=LABEL_FONT)
website_label.grid(column=LABEL_COLUMN_START, row=LABEL_ROW_START, pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X)

email_user_label = Label(text="Email/Username:", background=LABEL_BG_COLOR,
                         fg=LABEL_TEXT_COLOR, font=LABEL_FONT)
email_user_label.grid(column=LABEL_COLUMN_START, row=LABEL_ROW_START+1, pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X)

password_label = Label(text="Password:", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                       font=LABEL_FONT)
password_label.grid(column=LABEL_COLUMN_START, row=LABEL_ROW_START+2, pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X)


# FORM ENTRIES
# TODO: fix entries so they line up correctly
website_entry = Entry(background=FORM_BG_COLOR, fg=LABEL_TEXT_COLOR,
                      font=LABEL_FONT, width=FORM_ENTRY_WIDTH)
website_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START, columnspan=2, sticky="w")

email_user_entry = Entry(background=FORM_BG_COLOR,
                         fg=LABEL_TEXT_COLOR, font=LABEL_FONT, width=FORM_ENTRY_WIDTH)
email_user_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+1, columnspan=2,  sticky="w")

password_entry = Entry(background=FORM_BG_COLOR, fg=LABEL_TEXT_COLOR,
                       font=LABEL_FONT, width=PASSWORD_ENTRY_WIDTH)
password_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START + 2,  sticky="w")


# BUTTONS
generate_password_button = Button(text="Generate Password", background=LABEL_BG_COLOR,
                                  fg=LABEL_TEXT_COLOR, font=LABEL_FONT)
generate_password_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START+2,)

add_button = Button(text="Add", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                    font=LABEL_FONT, width=ADD_BUTTON_WIDTH)
add_button.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+3, columnspan=2,
                pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X, sticky="w")


window.mainloop()
