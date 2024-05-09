from random import sample, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from tkinter import Tk, IntVar, Checkbutton, Label, Entry, Button, END, messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_set = ''
    
    if use_upper:
        character_set += ascii_uppercase
    if use_lower:
        character_set += ascii_lowercase
    if use_digits:
        character_set += digits
    if use_symbols:
        character_set += punctuation

    # Ensure that at least one character type is selected
    if len(character_set) == 0:
        return 'Please select at least one character type'

    # Generate the password
    password_chars = sample(character_set, length)

    # Shuffle the characters to ensure randomness
    shuffle(password_chars)

    # Join the characters to form the password
    password = ''.join(password_chars)

    return password

def on_button_click():
    # Get the user-selected options and password length
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()
    
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number for the password length.")
        return

    # Check if the password length is within the allowed range
    if length < 1 or length > 10:
        messagebox.showwarning("Invalid Length", "Password length must be between 1 and 10.")
    else:
        # Call the password generator function and save the result
        generated_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        password_entry.delete(0, END)  # Clear the entry
        password_entry.insert(0, generated_password)  # Insert the generated password

# Create the main window
root = Tk()
root.title('Password Generator')
root.geometry('314x314')
root.resizable(1,0)

# Create variables to hold the states of the checkboxes
upper_var = IntVar()
lower_var = IntVar()
digits_var = IntVar()
symbols_var = IntVar()

# Create checkboxes for character type selection
upper_check = Checkbutton(root, text='Uppercase', variable=upper_var, anchor='w')
upper_check.pack(fill='x')
lower_check = Checkbutton(root, text='Lowercase', variable=lower_var, anchor='w')
lower_check.pack(fill='x')
digits_check = Checkbutton(root, text='Digits', variable=digits_var, anchor='w')
digits_check.pack(fill='x')
symbols_check = Checkbutton(root, text='Symbols', variable=symbols_var, anchor='w')
symbols_check.pack(fill='x')

# Create a label and an entry widget for password length input
length_label = Label(root, text="Password Length", anchor='w')
length_label.pack(fill='x')
length_entry = Entry(root)
length_entry.pack(fill='x', pady=(0, 10))  # Reduced padding below length entry

# Create an entry widget to display the password
password_entry = Entry(root, font=('Arial', 14), bd=2, relief='groove')
password_entry.pack(pady=20)

# Create a button to trigger password generation
generate_button = Button(root, text='Generate Password', command=on_button_click)
generate_button.pack(pady=10)

root.mainloop()
