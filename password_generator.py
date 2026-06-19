import random
def strong_password_generator(get_value_entry, symbol_option, display_place_entry) -> None:
    """
    Displays a chosen amount of random characters for a strong password in the window

    """
    characters : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                   '#','$','%','*','(',')','@','!']

    characters_without_symbols : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    numbers : list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    amount_of_characters = get_value_entry.get()
    
    val : int = int(amount_of_characters)

    match symbol_option.get():
    	
    	case 1:
    	  random_characters : random = random.choices(characters, k=val)
    	  
    	  random_password : join = "".join(random_characters)
    	  
    	  display_place_entry.delete(0,END)
    	  
    	  display_place_entry.insert(0, random_password)
    	
    	case 2:
          random_characters_without_symbols : random = random.choices(characters_without_symbols, k=val)
          random_password_without_symbols : join = "".join(random_characters_without_symbols)
          display_place_entry.delete(0,END)
          display_place_entry.insert(0, random_password_without_symbols)




import tkinter as tk; from tkinter import *



#creating the window
window = Tk()

#window background color
window.configure(bg='black')

#window Title
window.title('Password generator app 🔒')

#window's dimensions
window.geometry('600x300')

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
	             font=('Arial', 30, 'bold'),
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

''' 'Symbols/No symbols' options'''
Symbol_or_no_Symbols = IntVar()

#yes option
yes_option = Radiobutton(window,
	                  text='Yes 👍',
	                  variable=Symbol_or_no_Symbols,
	                  value=1,
	                  fg='#1c7a21',
	                  bg='black',
	                  font=('Arial', 15, 'bold'),
	                  activebackground='black',
	                  activeforeground='#1c7a21')
yes_option.grid(row=1,column=0)

#no option
no_option = Radiobutton(window,
	                    text='No 👎',
	                    variable=Symbol_or_no_Symbols,
	                    value=2,
	                    fg='#fc3503',
	                    bg='black',
	                    font=('Arial', 15, 'bold'),
	                    activebackground='black',
	                    activeforeground='#fc3503')
no_option.grid(row=2,column=0)


#'Amount of characters' text
label : Label = tk.Label(window,
	             text='Amount of characters (number) for password (Press enter when finished):',
	             font=('Arial', 11, 'bold'),
	             bg='black',
	             fg='#2060a1')
label.grid(row=4, column=0)

#amount of characters's entry
character_amount_entry : entry = Entry(window,
	                                   font=('Arial', 50))
character_amount_entry.grid(row=5,column=0)



# Bind the Enter key to the entry box
def enter_pressed(event):
    character_amount_entry.get()
    strong_password_generator(character_amount_entry, Symbol_or_no_Symbols, password_displayed_entry)
character_amount_entry.bind('<Return>', enter_pressed) #checks if user pressed enter


#'Password' text
password_label : Label = tk.Label(window,
	                      text='Password 🔐:',
	                      font=('Courier', 20),
	                      bg='black',
	                      fg='#699e24')
password_label.grid(row=6,column=0)

#Password displayed entry
password_displayed_entry : Entry = Entry(window,
	                                    font=('Arial', 50),)
password_displayed_entry.grid(row=7,column=0)


window.mainloop()