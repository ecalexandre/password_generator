import random
def strong_password_generator(get_value_entry, display_place_entry) -> None:
    """
    Displays a chosen amount of random characters for a strong password in the window

    """
    characters : list[str] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                                   'o', 'p', 'q' 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                                   '#','$','%','*','(',')','@','!']
    
    amount_of_characters = get_value_entry.get()

    val : int = int(amount_of_characters)
    
    random_characters : random = random.choices(characters, k=val)
    
    random_password : join = "".join(random_characters)
    
    display_place_entry.delete(0,END)
    
    display_place_entry.insert(0, random_password)




import tkinter as tk; from tkinter import *


#creating the window
window = Tk()

#window background color
window.configure(bg='black')

#window Title
window.title('Password generator app')

#window's dimensions
window.geometry('600x300')

#app icon image
app_icon : PhotoImage = tk.PhotoImage(file='C:\\Users\\ecalexandre\\Downloads\\padlorfe.png')
window.iconphoto(True, app_icon)

#text image
photo : PhotoImage = PhotoImage(file="C:\\Users\\ecalexandre\\Downloads\\password.png")

#displayed text in the window on top
text : Label = tk.Label(window,
	             text='Password generator',
	             bg='black',
	             fg='#699e24',
	             font=('Arial', 10, 'bold'),
	             image=photo,
	             compound='bottom')
text.grid(row=0, column=0)






#'Amount of characters' text
label : Label = tk.Label(window,
	             text='Put the amount of characters that you want your password to have here (HAS TO BE A NUMBER):',
	             font=('Arial', 15, 'bold'),
	             bg='black',
	             fg='#699e24')
label.grid(row=1, column=0)

#amount of characters's entry
character_amount_entry : entry = Entry(window,
	                                   font=('Arial', 50))
character_amount_entry.grid(row=2,column=0)

#Button for generating a random password
generate_password_button : Button = tk.Button(window, 
	                                 text='Generate a random password',
	                                 bg='white',
	                                 command=lambda: strong_password_generator(character_amount_entry, password_displayed_entry))

generate_password_button.grid(row=2,column=1)

label2 : Label = tk.Label(window,
	                      text='Password:',
	                      font=('Arial', 20),
	                      bg='black',
	                      fg='#699e24')
label2.grid(row=4,column=0)

#Password displayed entry
password_displayed_entry : Entry = Entry(window,
	                                    font=('Arial', 50))
password_displayed_entry.grid(row=5,column=0)


window.mainloop()