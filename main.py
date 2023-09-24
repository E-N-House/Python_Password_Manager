from tkinter import *
import math
# NOTE: anyone else downloading app will be unable to use
from EMAIL import EMAIL_WORK

# ----------------------------      CONSTANTS      ------------------------------- #
PROJECT_NAME = "Password Manager"
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 200
PADDING_WINDOW = 50
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
user_entry_website = "WEBSITE"
user_entry_email = EMAIL_WORK
user_entry_pw = "PASSWORD"
new_entry = f"{user_entry_website} | {user_entry_email} | {user_entry_pw} \n"
DATA_FILE = "pw_data.txt"


# create pw_data.txt file
def create_data_file():
    try:
        open(DATA_FILE).close()
        print("there")
        return True
    except FileNotFoundError:
        print("creating new pw_data file")
        with open("pw_data.txt", mode="w") as new_file:
            new_file.write("WEBSITE | EMAIL_OR_USER | PASSWORD\n")
            new_file.close()
        return False


#   format the info with " | " between each field
new_entry = f"{user_entry_website} | {user_entry_email} | {user_entry_pw}\n"


def add_entry():
    create_data_file()
    if create_data_file():
        #   take the new string and append it to the pw_data.txt file
        with open("pw_data.txt", mode="a") as data_file:
            data_file.write(new_entry)
            data_file.close()
    else:
        print("not there")


# TODO: copy info from entries to a pw_data.txt file
#   save that new sting in a variable

# TODO: clear all entries of information


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
# TODO: double check entries line up correctly
website_entry = Entry(background=FORM_BG_COLOR, fg=LABEL_TEXT_COLOR,
                      font=LABEL_FONT, width=FORM_ENTRY_WIDTH)
website_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START, columnspan=2, sticky="w")
# center curser on website entry
website_entry.focus()

# IDEA: refactor email_user_entry to be a dropdown choice of users common emails
email_user_entry = Entry(background=FORM_BG_COLOR,
                         fg=LABEL_TEXT_COLOR, font=LABEL_FONT, width=FORM_ENTRY_WIDTH)
email_user_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+1, columnspan=2,  sticky="w")
# pre-fill in email with personal email
email_user_entry.insert(0, EMAIL_WORK)

password_entry = Entry(background=FORM_BG_COLOR, fg=LABEL_TEXT_COLOR,
                       font=LABEL_FONT, width=PASSWORD_ENTRY_WIDTH)
password_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START + 2,  sticky="w")


# BUTTONS
generate_password_button = Button(text="Generate Password", background=LABEL_BG_COLOR,
                                  fg=LABEL_TEXT_COLOR, font=LABEL_FONT)
generate_password_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START+2,)

add_button = Button(text="Add", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                    font=LABEL_FONT, width=ADD_BUTTON_WIDTH, command=add_entry)
add_button.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+3, columnspan=2,
                pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X, sticky="w")


window.mainloop()
