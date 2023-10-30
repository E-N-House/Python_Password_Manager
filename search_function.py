# First open the document password doctes

def search_function(website_entry):
    user_entry_website = website_entry.get()
    with open(DATA_FILE, mode="r") as data_file:
        data_file.read()
        print(data_file)
        data_file.close()
        messagebox.showinfo(title="New Data Accepted", message="Your new password was added.")
        reset_forms()
