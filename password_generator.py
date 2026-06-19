import random
def strong_password_generator(get_value_entry, symbol_option, number_option, display_place_entry) -> None:
    """
    Displays a chosen amount of random characters for a strong password in the window

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
    
    #Results for each options
    match symbol_option.get(), number_option.get():
    	
    	case 1,1:
    	  random_characters_with_numbers_and_symbols : random = random.choices(characters_with_numbers_and_symbols, k=val)
    	  
    	  random_password_with_numbers_and_symbols : join = "".join(random_characters_with_numbers_and_symbols)
    	  
    	  display_place_entry.delete(0,END)
    	  
    	  display_place_entry.insert(0,random_password_with_numbers_and_symbols)
    	
    	case 1,2:
          random_characters_without_numbers : random = random.choices(characters_without_numbers, k=val)
          
          random_password_without_numbers : join = "".join(random_characters_without_numbers)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_numbers)
    	
    	case 2,1:
          random_characters_without_symbols : random = random.choices(characters_without_symbols, k=val)
          
          random_password_without_symbols : join = "".join(random_characters_without_symbols)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_symbols)
    	
    	case 2,2:
          random_characters_without_symbols_and_numbers : random = random.choices(characters_without_symbols_and_numbers, k=val)
          
          random_password_without_symbols_and_numbers : join = "".join(random_characters_without_symbols_and_numbers)
          
          display_place_entry.delete(0,END)
          
          display_place_entry.insert(0, random_password_without_symbols_and_numbers)    


import tkinter as tk; from tkinter import *



#creating the window
window = Tk()

#window background color
window.configure(bg='black')

#window Title
window.title('Password generator app 🔒')

#window's dimensions
window.geometry('1000x600')

#app icon image
app_icon : PhotoImage = tk.PhotoImage(file='C:\\Users\\ecalexandre\\Downloads\\padlorfe.png')
window.iconphoto(True, app_icon)

#text image
photo : PhotoImage = PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\password.png")

#displayed text in the window on top
text : Label = tk.Label(window,
	             text='Password generator 🔒',
	             bg='black',
	             fg='#8803fc',
	             font=('Arial', 15, 'bold'),
	             image=photo,
	             compound='bottom')
text.grid(row=3, column=2)





#symbols/no symbols text
symbols_label : Label = tk.Label(window,
	                             text='Do you want symbols in your password or not',
	                             font=('Arial', 15, 'bold'),
	                             bg='black',
	                             fg='#fc035a')
symbols_label.grid(row=0,column=0)

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
yes_option_symbols.grid(row=1,column=0)

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
no_option_symbols.grid(row=2,column=0)




#Numbers options text
numbers_label : Label = tk.Label(window,
	                            text='Do you want numbers in your password or not',
	                            font=('Arial', 15, 'bold'),
	                            bg='black',
	                            fg='#fc035a')
numbers_label.grid(row=3,column=0)

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
yes_option_numbers.grid(row=4, column=0)

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
no_option_numbers.grid(row=5, column=0)





#'Amount of characters' text
label : Label = tk.Label(window,
	             text='Amount of characters (number) for password (Press enter when finished):',
	             font=('Arial', 11, 'bold'),
	             bg='black',
	             fg='#2060a1')
label.grid(row=6, column=0)

#amount of characters's entry
character_amount_entry : entry = Entry(window,
	                                   font=('Arial', 50))
character_amount_entry.grid(row=7,column=0)



# Bind the Enter key to the entry box
def enter_pressed(event) -> None:
    """
    Gets the value of the entry of the character amount and calls the strong_password_generator() function to show the password
    """

    character_amount_entry.get()
    strong_password_generator(character_amount_entry, symbol_or_no_Symbols, numbers_or_no_numbers, password_displayed_entry)
character_amount_entry.bind('<Return>', enter_pressed) #checks if user pressed Enter


#'Password' text
password_label : Label = tk.Label(window,
	                      text='Password 🔐:',
	                      font=('Courier', 15),
	                      bg='black',
	                      fg='#699e24')
password_label.grid(row=8,column=0)



#Password displayed entry
password_displayed_entry : Entry = Entry(window,
	                                    font=('Arial', 50),)
password_displayed_entry.grid(row=9,column=0)



#copy password function for button
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
copy_password_button.grid(row=9, column=1)	                                         

window.mainloop()