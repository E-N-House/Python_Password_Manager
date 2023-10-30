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

DATA_FILE = "pw_data.txt"


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_data_file():
    """checks if a file exists. And if it doesn't create a text file using global constant DATA_FILE
    and fills in the column names as top row separated by spacer"""
    try:
        file = open(DATA_FILE)
    except FileNotFoundError:
        messagebox.showinfo(title="Creating File", message=f"Creating a file named {DATA_FILE}\n"
                                                           f"to store your information.")
        file = open("pw_data.txt", mode="a")
        file.write("WEBSITE | EMAIL_OR_USER | PASSWORD\n")
    finally:
        file.close()


#   save that new string in a variable
def save_entries_to_string():
    """gets values from form validates they are filled in correctly.
    if yes returns formatted string"""
    user_entry_website = website_entry.get()
    user_entry_email = email_user_entry.get()
    user_entry_pw = password_entry.get()
    # validate all fields filled
    if user_entry_website == "" or user_entry_email == "" or user_entry_pw == "":
        # prompt an error message
        messagebox.showerror(title='Blank Entries!', message='All Fields Must Be Entered')
    else:
        # ask user if they want these settings
        is_ok = messagebox.askokcancel(title="Entry to be added", message=f"You have entered the following\n"
                                                                  f"Website:    {user_entry_website}\n"
                                                                  f"Username/Email: {user_entry_email}\n"
                                                                  f"Password:   {user_entry_pw}\n"
                                                                  f"Press OK to accept or CANCEL to try again.")
        if is_ok:
            # format the info with " | " between each field
            new_entry = f"{user_entry_website} | {user_entry_email} | {user_entry_pw}\n"
            # alt way to create a new entry
            # new_entry_using_join = " | ".join([user_entry_website, user_entry_email, user_entry_pw])
            # return f"{new_entry_using_join}\n"
            return new_entry


def save_as_json():
    """gets values from form validates they are filled in correctly.
       if yes returns formatted string"""
    user_entry_website = website_entry.get()
    user_entry_email = email_user_entry.get()
    user_entry_pw = password_entry.get()
    new_data_dict_for_json = {user_entry_website: {
        "email": user_entry_email,
        "password": user_entry_pw,
    }
                         }
    # validate all fields filled
    if user_entry_website == "" or user_entry_email == "" or user_entry_pw == "":
        # prompt an error message
        messagebox.showerror(title='Blank Entries!', message='All Fields Must Be Entered')
    else:
        with open("pw_data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
            # updating old data with new data
            data.update(new_data_dict_for_json)

        with open("pw_data.json", "w") as data_file:
            # adding new data to data file
            json.dump(data, data_file, indent=4)


            # clear fields
            website_entry.delete(0,END)
            password_entry.delete(0, END)


def add_entry():
    """Validates that all forms contain values
    then Creates a formatted string to append onto file"""
    new_entry = save_entries_to_string()
    if type(new_entry) == str:
        #   take the new string and append it to the pw_data.txt file
        with open(DATA_FILE, mode="a") as data_file:
            data_file.write(new_entry)
            data_file.close()
            messagebox.showinfo(title="New Data Accepted", message="Your new password was added.")
            reset_forms()
    else:
        return


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
    return


# search functionality
def search_click():
    user_entry_website = website_entry.get()
    with open(DATA_FILE, mode="r") as data_file:
        # returns list
        data = data_file.readlines()
        for line in data:
            dataline = line.split(" | ")
            if dataline[0] == user_entry_website.lower():
                stored_email = dataline[1]
                stored_password = dataline[2]
                messagebox.showinfo(title=f"Stored Data Found for {user_entry_website}",
                                    message=f"Username/Email:     {stored_email}\nPassword:   {stored_password}\n")
                return True
            else:
                continue
        messagebox.showinfo(title="No Data Found", message=f"Stored data does not contain:      {user_entry_website}")

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

search_button = Button(text="Search", background=LABEL_BG_COLOR, width=INSET_BUTTON_WIDTH,
                                  fg=LABEL_TEXT_COLOR, font=LABEL_FONT, command=search_click)
search_button.grid(column=LABEL_COLUMN_START+2, row=LABEL_ROW_START,  pady=BUTTON_PAD_Y,
                   padx=BUTTON_PAD_X,)
# checks for data file on launch and creates if not there on startup
create_data_file()

window.mainloop()
