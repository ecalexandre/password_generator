import random

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
    	  
    	  display_place_entry.delete(0,END)
    	  
    	  display_place_entry.insert(0,random_password_with_numbers_and_symbols)
    	
    	# If Yes to symbols but No to numbers ---> Password will contain symbols but not numbers
    	case 1,2:
          random_characters_without_numbers : random = random.choices(characters_without_numbers, k=val)
          
          random_password_without_numbers : join = "".join(random_characters_without_numbers)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_numbers)
    	
    	# If No to symbols but Yes to numbers ---> Password will contain numbers but not symbols
    	case 2,1:
          random_characters_without_symbols : random = random.choices(characters_without_symbols, k=val)
          
          random_password_without_symbols : join = "".join(random_characters_without_symbols)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_symbols)
    	
    	# If No to both symbols and numbers ---> Password will not contain symbols or numbers
    	case 2,2:
          random_characters_without_symbols_and_numbers : random = random.choices(characters_without_symbols_and_numbers, k=val)
          
          random_password_without_symbols_and_numbers : join = "".join(random_characters_without_symbols_and_numbers)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_symbols_and_numbers)    


import tkinter as tk; from tkinter import *

#creating the window
window = Tk()

window.resizable(0,0)

#window background color
window.configure(bg='black')

#window Title
window.title('Random Password Generator')

#window's dimensions
window.geometry('1200x400')

#app icon image
app_icon : PhotoImage = tk.PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\password.png")
window.iconphoto(True, app_icon)

#symbols/no symbols text
symbols_label : Label = tk.Label(window,
	                             text='Do you want symbols in your password',
	                             font=('Arial', 15, 'bold'),
	                             bg='black',
	                             fg='#a024f2')
symbols_label.grid(row=1,column=0)

#Symbols/No symbols options
symbol_or_no_Symbols = IntVar()

#yes option
yes_option_symbols : Radiobutton = Radiobutton(window,
	                                           text='Yes 👍',
	                                           variable=symbol_or_no_Symbols,
	                                           value=1,
	                                           fg='#1c7a21',
	                                           bg='black',
	                                           font=('Arial', 15, 'bold'),
	                                           activebackground='black',
	                                           activeforeground='#1c7a21')
yes_option_symbols.grid(row=2,column=0)

#no option
no_option_symbols : Radiobutton = Radiobutton(window,
	                                          text='No 👎',
	                                          variable=symbol_or_no_Symbols,
	                                          value=2,
	                                          fg='#fc3503',
	                                          bg='black',
	                                          font=('Arial', 15, 'bold'),
	                                          activebackground='black',
	                                          activeforeground='#fc3503')
no_option_symbols.grid(row=3,column=0)




#Numbers options text
numbers_label : Label = tk.Label(window,
	                            text='Do you want numbers in your password',
	                            font=('Helvetica', 15),
	                            bg='black',
	                            fg='#d48f28')
numbers_label.grid(row=1,column=1)

#Numbers options
numbers_or_no_numbers = IntVar()

#yes option
yes_option_numbers : Radiobutton = tk.Radiobutton(window,
	                                            text='Yes 👍',
	                                            variable=numbers_or_no_numbers,
	                                            value=1,
	                                            fg='#1c7a21',
	                                            bg='black',
	                                            font=('Arial', 15, 'bold'),
	                                            activebackground='black',
	                                            activeforeground='#1c7a21')
yes_option_numbers.grid(row=2, column=1)

#no option
no_option_numbers : Radiobutton = tk.Radiobutton(window,
	                                            text='No 👎',
	                                            variable=numbers_or_no_numbers,
	                                            value=2,
	                                            fg='#fc3503',
	                                            bg='black',
	                                            font=('Arial', 15, 'bold'),
	                                            activebackground='black',
	                                            activeforeground='#fc3503')
no_option_numbers.grid(row=3, column=1)





#'Amount of characters' text
label : Label = tk.Label(window,
	             text='Amount of characters (number) for password (Press enter when finished):',
	             font=('Arial', 11, 'bold'),
	             bg='black',
	             fg='#2060a1')
label.grid(row=7, column=0)

#amount of characters's entry
character_amount_entry : entry = Entry(window,
	                                   font=('Arial', 35))
character_amount_entry.grid(row=8,column=0)

# enabling entry function after user did not put integer
def enable_entry(secondary_window: tkinter) -> None:
	"""
	Enables the character_amount_entry's state
	and makes the error window disappear from the user's screen

	param: 'secondary_window' is the 'error window' that will appear if the user does not put an integer number in the entry box
	
	"""

	character_amount_entry.config(state='normal')
	secondary_window.destroy()


# 'Check entry's value' function 
def check_entry_value(get_value_entry: Entry) -> None:
    """
    Checks if the value of the user's entry is an integer
    otherwise, it displays another window for the error

    param: 'get_value_entry' is the user input entry
    
    """
    
    box = get_value_entry.get()
    try:
      # If the user puts an integer number, it calls the 'strong_password_generator' function to display a password	
      val = int(box)
      strong_password_generator(character_amount_entry, symbol_or_no_Symbols, numbers_or_no_numbers, password_displayed_entry)
    except: # Otherwise, it disables the user's entry box and displays the Error window
      get_value_entry.config(state="disabled")
      new_window = tk.Toplevel(window)
      new_window.title('Value type Error')
      Error_window_icon : PhotoImage = tk.PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\errorimage.png")
      new_window.iconphoto(False, Error_window_icon)
      new_window.geometry('400x400') 
      new_window.resizable(0,0)
      label = tk.Label(new_window, text="Error: this is not an integer number")
      verify_button = Button(new_window, text='Enable text box', command=lambda: enable_entry(new_window))
      verify_button.pack()
      label.pack()

# Bind the Enter key to the entry box
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
         check_entry_value(character_amount_entry)

character_amount_entry.bind('<Return>', enter_pressed) #checks if user pressed Enter will call enter_pressed() function


#'Password' text
password_label : Label = tk.Label(window,
	                      text='Password 🔐:',
	                      font=('Courier', 15),
	                      bg='black',
	                      fg='#699e24')
password_label.grid(row=9,column=0)



#Password displayed entry
password_displayed_entry : Entry = Entry(window,
	                                    font=('Arial', 50),)
password_displayed_entry.grid(row=10,column=0)



'''copy password function for button'''
def copy_text() -> None:
   # 1. Clears the system clipboard
   window.clipboard_clear()
   # 2. Append the text from the password display entry
   window.clipboard_append(password_displayed_entry.get())
   # 3. Optional : keeps clipboard alive after window closes
   window.update()

copy_password_button : Button = tk.Button(window,
	                                      text='Copy password',
	                                      bg='black',
	                                      fg='#f2e124',
	                                      activebackground='black',
	                                      activeforeground='#f2e124',
	                                      command=copy_text)
copy_password_button.grid(row=11, column=0)	                                         


#keeps window active until closed
window.mainloop()