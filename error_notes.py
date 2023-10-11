# # FileNotFoundError
# with open("notfound.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# num_list = ["zero", "one", "two"]
# curr_num = num_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# can print out the error and have it contained in an except block
try:
    with open("notfound.txt") as file:
        file.read()
    num_list = ["zero", "one", "two"]
    curr_num = num_list[3]
    text = "abc"
    print(text + 5)
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existent_key"]
except KeyError as error_message:
    print(f"Key {error_message} doesn't exist")
except FileNotFoundError as error_message:
    print(f"the file {error_message} is missing")
except TypeError as error_message:
    print(f"incorrect type {error_message}")
except IndexError as error_message:
    print(f"index {error_message} is out of range")
else:
    print("all good")
finally:
    print("we are finished finding errors")
    print("and now we are raising our own error message")
    raise TypeError("this is a made up error")

