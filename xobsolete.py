from tkinter import *
from tkinter import messagebox
# NOTE: anyone else with app will be unable to use
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
ERROR_FONT = ("Arial", 20, "bold")


LABEL_FONT = ("Arial", 10)
LABEL_TEXT_COLOR = "black"
LABEL_BG_COLOR = "light blue"
LABEL_COLUMN_START = 0
LABEL_ROW_START = 1

BUTTON_PAD_Y = 5
BUTTON_PAD_X = 5

FORM_BG_COLOR = "light yellow"
FORM_ENTRY_WIDTH = 46

PASSWORD_ENTRY_WIDTH = 27

ADD_BUTTON_WIDTH = 36

FONT_NAME = "Courier"
BOLDED_FONT = ("Arial", 26, "bold")
LOGO_FILE = "logo.png"

DATA_FILE = "pw_data.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    print("pw clicked")

# ---------------------------- SAVE PASSWORD ------------------------------- #


# create pw_data.txt file
def create_data_file():
    """checks if a file exists. And if it doesn't create a text file using global constant DATA_FILE
    and fills in the column names as top row separated by spacer"""
    try:
        open(DATA_FILE).close()
    except FileNotFoundError:
        print(f"creating new {DATA_FILE} file")
        with open("pw_data.txt", mode="a") as new_file:
            new_file.write("WEBSITE | EMAIL_OR_USER | PASSWORD\n")


#   save that new string in a variable
def save_information_to_string():
    """gets values from form validates they are filled in.
    if yes returns formatted string"""
    user_entry_website = website_entry.get()
    user_entry_email = email_user_entry.get()
    user_entry_pw = password_entry.get()
    # validate all fields filled
    if user_entry_website == "" or user_entry_email == "" or user_entry_pw == "":
        print("empty fields")
    else:
        # format the info with " | " between each field
        new_entry = f"{user_entry_website} | {user_entry_email} | {user_entry_pw}\n"
        return new_entry


def add_entry():
    """Validates that all forms contain values
    then Creates a formatted string to append onto file"""
    new_entry = save_information_to_string()
    create_data_file()
    if type(new_entry) == str:
        #   take the new string and append it to the pw_data.txt file
        with open(DATA_FILE, mode="a") as data_file:
            data_file.write(new_entry)
            data_file.close()
            print("new entry added")
            reset_forms()
    else:
        create_message('All Fields Must Be Entered')
        return


def create_message(message):
    error_message.config(text=message)
    error_message.grid(row=0, column=0, columnspan=3)


# reset the UI
def reset_forms():
    """clear website (set website to focus) and clear password entries.
    Reset email to default. Remove error if it exists"""
    # clear out forms and reset email to default
    website_entry.delete(0, END)
    website_entry.focus()
    password_entry.delete(0, END)
    email_user_entry.delete(0, END)
    email_user_entry.insert(0, EMAIL_WORK)

    # hide invalid message after successful add
    error_message.grid_remove()
    return


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
                                  fg=LABEL_TEXT_COLOR, font=LABEL_FONT, command=generate_pw)
generate_password_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START+2,)

add_button = Button(text="Add", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                    font=LABEL_FONT, width=ADD_BUTTON_WIDTH, command=add_entry)
add_button.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+3, columnspan=2,
                pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X, sticky="w")


# Error message
error_message = Message(text="", background=COLOR_ERRORS,
                        font=ERROR_FONT, fg="white")
window.mainloop()
