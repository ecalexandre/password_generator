import random, customtkinter as ctk
import tkinter as tk
from tkinter import *

# Strong password generator function
def strong_password_generator(get_value_entry:Entry,symbol_option:IntVar,number_option:IntVar,display_place_entry:Entry) -> None:
    """
    Displays a chosen amount of random chosen types of characters for a strong password in the 'display_place_entry'

    
    params:
    1. 'get_value_entry' is the user's entry box so that he can type the amount of characters for his password.
    2. 'symbol_option' is a variable for two options (symbols or no symbols).
    3. 'number_option' is a variable for two options (numbers or no numbers)
    4. 'display_place_entry' is the entry for the displayed password

    """
    
    characters_without_numbers : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                   '#','$','%','*','(',')','@','!']

    characters_without_symbols_and_numbers : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    characters_without_symbols : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    characters_with_numbers_and_symbols : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                   '#','$','%','*','(',')','@','!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    amount_of_characters = get_value_entry.get()
    
    val : int = int(amount_of_characters)
    
    # Results for symbols and numbers options
    match symbol_option.get(), number_option.get():
        
        # If Yes for both symbols and numbers ---> Password will mostly contain symbols and numbers
        case 1,1:
          random_characters_with_numbers_and_symbols : random = random.choices(characters_with_numbers_and_symbols, k=val)
          
          random_password_with_numbers_and_symbols : join = "".join(random_characters_with_numbers_and_symbols)
          
          display_place_entry.delete("0.0","end")
          
          display_place_entry.insert("0.0",random_password_with_numbers_and_symbols)
        
        # If Yes to symbols but No to numbers ---> Password will contain symbols but not numbers
        case 1,2:
          random_characters_without_numbers : random = random.choices(characters_without_numbers, k=val)
          
          random_password_without_numbers : join = "".join(random_characters_without_numbers)
          
          display_place_entry.delete("0.0","end")
          
          display_place_entry.insert("0.0", random_password_without_numbers)
        
        # If No to symbols but Yes to numbers ---> Password will contain numbers but not symbols
        case 2,1:
          random_characters_without_symbols : random = random.choices(characters_without_symbols, k=val)
          
          random_password_without_symbols : join = "".join(random_characters_without_symbols)
          
          display_place_entry.delete("0.0","end")
          
          display_place_entry.insert("0.0", random_password_without_symbols)
        
        # If No to both symbols and numbers ---> Password will not contain symbols or numbers
        case 2,2:
          random_characters_without_symbols_and_numbers : random = random.choices(characters_without_symbols_and_numbers, k=val)
          
          random_password_without_symbols_and_numbers : join = "".join(random_characters_without_symbols_and_numbers)
          
          display_place_entry.delete("0.0","end")
          
          display_place_entry.insert("0.0", random_password_without_symbols_and_numbers)
        
        # If no option was chosen, the password will contain only letters
        case _: 
          random_characters_without_symbols_and_numbers : random = random.choices(characters_without_symbols_and_numbers, k=val)
          
          random_password_without_symbols_and_numbers : join = "".join(random_characters_without_symbols_and_numbers)
          
          display_place_entry.delete("0.0","end")
          
          display_place_entry.insert("0.0", random_password_without_symbols_and_numbers)


import customtkinter as ctk
from customtkinter import *

# Create a window
window = CTk()

# Makes window unresizable
window.resizable(False, False) # height and width

# window title
window.title("Random Password Generator")

# window dimensions
window.geometry("900x300") # width and height

# app icon
app_icon : PhotoImage = tk.PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\password.png")
window.after(200, lambda: window.iconphoto(False, app_icon))

frame_1 : Frame = ctk.CTkFrame(window,
	                            width=200,
	                            bg_color='#3c0a3d')
frame_1.grid(row=1,column=0)

# 'symbols/no symbols' text
symbols_label : Label = ctk.CTkLabel(frame_1, 
                                    text='Do you want symbols in your password',
                                    font=('Arial', 15),
                                    pady=10,
                                    padx=10)
symbols_label.grid(row=1,column=0)

# symbols/no symbols options variable
symbol_or_no_symbols = IntVar()

# Yes option
yes_option_symbols : Radiobutton = ctk.CTkRadioButton(frame_1,
                                                      text='Yes 👍',
                                                      variable=symbol_or_no_symbols,
                                                      value=1,
                                                      font=('Arial', 15))
yes_option_symbols.grid(row=2,column=0)

# No option
no_option_symbols : Radiobutton = ctk.CTkRadioButton(frame_1,
                                                     text='No 👎',
                                                     variable=symbol_or_no_symbols,
                                                     value=2,
                                                     font=('Arial', 15))
no_option_symbols.grid(row=3,column=0)

frame_2 : Frame = ctk.CTkFrame(window,
	                           width=200,
	                           bg_color='#0c0a3d')
frame_2.grid(row=1, column=1)

# Numbers option text
numbers_label : Label = ctk.CTkLabel(frame_2,
                                    text='Do you want numbers in your password',
                                    font=('Arial', 15),
                                    padx=10)
numbers_label.grid(row=1,column=1)

# Numbers/no numbers options variable
numbers_or_no_numbers = IntVar()

# Yes option
yes_option_numbers : Radiobutton = ctk.CTkRadioButton(frame_2,
                                                      text='Yes 👍',
                                                      variable=numbers_or_no_numbers,
                                                      value=1,
                                                      font=('Arial', 15))
yes_option_numbers.grid(row=2,column=1)

# No option
no_option_numbers : Radiobutton = ctk.CTkRadioButton(frame_2,
                                                    text='No 👎',
                                                    variable=numbers_or_no_numbers,
                                                    value=2,
                                                    font=('Arial', 15))
no_option_numbers.grid(row=3,column=1)

# 'Amount of characters' text
Aof_label : Label = ctk.CTkLabel(window,
                                text='Amount of characters (number) for password (Press enter when finished):',
                                font=('Arial', 14))
Aof_label.grid(row=10, column=0)

# 'Amount of characters's entry'
character_amount_entry : Entry = ctk.CTkEntry(window,
                                              font=('Arial', 35),
                                              width=200,
                                              height=50,
                                              bg_color='green')
character_amount_entry.grid(row=11, column=0)


# enabling entry function after user did not put integer
def enable_entry(secondary_window: tkinter) -> None:
    """
    Enables the character_amount_entry's state
    and makes the error window disappear from the user's screen

    param: 'secondary_window' is the 'error window' that will appear if the user does not put an integer number in the entry box
    
    """

    character_amount_entry.configure(state='normal')
    secondary_window.destroy()


# error_window displayer
def error_window_displayer() -> None:
    """
    Creates a window that displays the user input value error

    """
    
    error_window = ctk.CTkToplevel(window)
    error_window.attributes("-topmost", True) # To make window appear in front of every other windows
    
    # error window's title
    error_window.title("Value Type Error")
    
    # Setting up error window icon image
    error_window_icon_image = tk.PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\errorimage.png")
    error_window.after(250, lambda: error_window.iconphoto(False, error_window_icon_image))
    
    # Error window dimensions
    error_window.geometry('400x100') # width and height
    
    # Making error window unsizable
    error_window.resizable(False, False) # width and height
    
    # Label text for error
    error_label : Label = ctk.CTkLabel(error_window,
                                       text='Error: this is not an integer number')
    error_label.pack()
    
    # Button to enable user entry box in main window
    enabling_user_input_button : Button = ctk.CTkButton(error_window,
                                                        text='Enable text box',
                                                        command=lambda: enable_entry(error_window))
    enabling_user_input_button.pack()

# 'Check entry's value' function 
def check_entry_value() -> None:
    """
    Checks if the value of the user's entry is an integer
    otherwise, it displays another window for the error

    param: 'get_value_entry' is the user input entry
    
    """
    user_value = character_amount_entry.get()
    try:
        int_val = int(user_value)
        strong_password_generator(character_amount_entry, symbol_or_no_symbols, numbers_or_no_numbers, password_displayed_entry)
    except:
        character_amount_entry.configure(state='disabled')
        error_window_displayer()

# '<Return>' detector
def enter_pressed(event: tkinter) -> None:
    """
    Gets the value of the entry of the character amount and calls the strong_password_generator() function to show the password
    only if the entry's state is enabled

    param: 'event' is an object that Tkinter automatically creates and passes to your function 
           whenever a bound action (like a key press or mouse click) occurs
    
    """
    character_amount_entry_state = character_amount_entry.cget("state")
    match character_amount_entry_state:
        case "disabled":
           pass
        case "normal":
         character_amount_entry.get()
         check_entry_value()

character_amount_entry.bind('<Return>', enter_pressed) #checks if user pressed Enter will call enter_pressed() function          

# 'Password' text
password_label : Label = ctk.CTkLabel(window,
                                      text='Random password 🔐:',
                                      font=('Courier', 15))
password_label.grid(row=10, column=1)

# Password displayed entry
password_displayed_entry : textbox = ctk.CTkTextbox(window,
                                                width=300,
                                                height=100,
                                                bg_color='#3d0a12',
                                                font=('Arial', 16))
password_displayed_entry.grid(row=11,column=1)

# copy password function for button
def copy_password() -> None:
   password = password_displayed_entry.get("0.0", "end-1c") 
   # 1. Clears the system clipboard
   window.clipboard_clear()
   # 2. Append the text from the password display entry
   window.clipboard_append(password)
   # 3. Optional : keeps clipboard alive after window closes
   window.update()

copy_password_button : Button = ctk.CTkButton(window,
                                          text='Copy password',
                                          command=copy_password,
                                          fg_color='#4d2aeb',
                                          bg_color='#3d0a12')
copy_password_button.grid(row=13, column=1)

# Keeps window active until closed
window.mainloop()