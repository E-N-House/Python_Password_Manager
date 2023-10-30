from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import json
# allows for use of clipboard functionality
import pyperclip


# NOTE: anyone else with app will be unable to use
# from EMAIL import EMAIL_WORK

# for now temp email exists
EMAIL_WORK = "temp123@ab.com"


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
FORM_ENTRY_WIDTH = 47

PASSWORD_ENTRY_WIDTH = 27

ADD_BUTTON_WIDTH = 40
INSET_BUTTON_WIDTH = 15

FONT_NAME = "Courier"
BOLDED_FONT = ("Arial", 26, "bold")
LOGO_FILE = "logo.png"

DATA_FILE = "pw_data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw_click():
    """On generate password click clears password field, creates a password via password_generator function
    inserts the new password into the password entry field and last copies the new password to the clipboard
    DEPENDS on pyperclip install"""
    password_entry.delete(0, END)
    password = password_generator()
    password_entry.insert(0, password)
    # uses pyperclip to copy the password to computer
    pyperclip.copy(password)


# ---------------------------- SAVE ENTRY ------------------------------- #

def save_as_json():
    """gets values from form validates they are filled in correctly.
       if yes creates or updates a .json file
       if Update will create dict entry of {website.lower(): {"email": entry, "password": entry}}
       finally clears pw and website fields"""
    user_entry_website = website_entry.get()
    user_entry_email = email_user_entry.get()
    user_entry_pw = password_entry.get()
    new_data_dict_for_json = {user_entry_website.lower(): {
        "email": user_entry_email,
        "password": user_entry_pw,
    }
                         }
    # validate all fields filled
    if user_entry_website == "" or user_entry_email == "" or user_entry_pw == "":
        # prompt an error message
        messagebox.showerror(title='Blank Entries!', message='All Fields Must Be Entered')
    else:
        try:
            with open(DATA_FILE, "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(DATA_FILE, "w") as data_file:
                json.dump(new_data_dict_for_json, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data_dict_for_json)

            with open(DATA_FILE, "w") as data_file:
                # adding new data to data file
                json.dump(data, data_file, indent=4)
        finally:
            # clear fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def search_click_with_json():
    """On click of search
    reads data file json if it exists
    looks for requested website in all lowercase
    creates message box with latest email and password created for said site"""
    user_entry_website = website_entry.get()
    try:
        with open(DATA_FILE, mode="r") as data_file:
            # Loads dictionary of json
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data Found", message=f"No Data File Found")

    else:
        try:
            search_data = data[user_entry_website.lower()]
        except KeyError:
            messagebox.showinfo(title="No Data Found",
                                message=f"Stored data does not contain:      {user_entry_website}")
        else:
            stored_email = search_data["email"]
            stored_password = search_data["password"]
            messagebox.showinfo(title=f"Stored Data Found for {user_entry_website}",
                                message=f"Username/Email:     {stored_email}\nPassword:   {stored_password}\n")


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
website_entry = Entry(background=FORM_BG_COLOR, fg=LABEL_TEXT_COLOR,
                      font=LABEL_FONT, width=PASSWORD_ENTRY_WIDTH)
website_entry.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START, sticky="w")
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
generate_password_button = Button(text="Generate Password", background=LABEL_BG_COLOR, width=INSET_BUTTON_WIDTH,
                                  fg=LABEL_TEXT_COLOR, font=LABEL_FONT, command=generate_pw_click)
generate_password_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START+2,)

add_button = Button(text="Add", background=LABEL_BG_COLOR, fg=LABEL_TEXT_COLOR,
                    font=LABEL_FONT, width=ADD_BUTTON_WIDTH, command=save_as_json)
add_button.grid(column=LABEL_COLUMN_START+1, row=LABEL_ROW_START+3, columnspan=2,
                pady=BUTTON_PAD_Y, padx=BUTTON_PAD_X, sticky="w")

search_button = Button(text="Search", background=LABEL_BG_COLOR, width=INSET_BUTTON_WIDTH, fg=LABEL_TEXT_COLOR,
                       font=LABEL_FONT, command=search_click_with_json)
search_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START,  pady=BUTTON_PAD_Y,
                   padx=BUTTON_PAD_X,)

window.mainloop()
