# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
import json
import pickle
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

def write_text():
    waiting_for_input = True
    with open("sample.txt", mode="w") as file:
        while waiting_for_input:
            text = input("Enter text (q to quit): ")
            if text == "q":
                waiting_for_input = False
                continue
            file.write(text)
            file.write("\n")


def read_text():
    with open("sample.txt", mode = "r") as file:
        print(file.readlines())


# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

def write_text_pickle():
    waiting_for_input = True
    data_to_store =[]
    with open("sample.p", mode="wb") as file:
    #with open("sample.txt", mode="w") as file:
        while waiting_for_input:
            text = input("Enter text (q to quit): ")
            if text == "q":
                waiting_for_input = False
                continue
            data_to_store.append(text)
        #file.write(json.dumps(data_to_store))
        file.write(pickle.dumps(data_to_store))


def read_text_pickle():
    #with open("sample.txt", mode = "r") as file:
    with open("sample.p", mode = "rb") as file:
        file_content = pickle.loads(file.read())
        for line in file_content:
            print(line)
            
#----------------------------------------------------------------------------------------------------#

def write_text_json():
    waiting_for_input = True
    data_to_store =[]
    with open("sample.txt", mode="w") as file:
        while waiting_for_input:
            text = input("Enter text (q to quit): ")
            if text == "q":
                waiting_for_input = False
                continue
            data_to_store.append(text)
        file.write(json.dumps(data_to_store))


def read_text_json():
    with open("sample.txt", mode = "r") as file:
        file_content = json.loads(file.read())
        for line in file_content:
            print(line)

# 4) Adjust the logic to load the file content to work with pickled/ json data.

def user_choice():
    print("Please choose")
    print("'w': To write to file")
    print("'r': To read file")
    choice = input("Your choice: ")
    if choice =="w":
        write_text_json()
    elif choice == "r":
        read_text_json()

user_choice()