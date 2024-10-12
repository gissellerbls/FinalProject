"""

Author: Gisselle Robles
Date written: 9/29/2024
Updated: 10/12/2024
Assignment:   Final Project
Short Desc:  This GUI is a coffee ordering system that gives the user options of toppings and types of coffee.
The program will show the total.

"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Main application window
root = tk.Tk()
root.title("Coffee Ordering System")
root.geometry("800x600")
root.config(bg="#dbc1ac")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Load the image
image = Image.open("IceCoffee.png")
image1= Image.open("HotCoffee.png")

# Resize the image
smaller_ice_image = image.resize((70, 70)) 
smaller_hot_image = image1.resize((70, 70))

ice_image_tk = ImageTk.PhotoImage(smaller_ice_image)
hot_image_tk = ImageTk.PhotoImage(smaller_hot_image)

# Make labels for image
image_label = tk.Label(root, image=ice_image_tk, bg="#dbc1ac",)
image_label.grid(row=10, column=0, columnspan=2, pady=10)

# Function to swap hot and cold images when ice/hot is selected
def update_image():
    if selected_temp.get() == "Ice":
        image_label.config(image=ice_image_tk, text="Image of Ice Coffee", compound="top", font=("Bubblegum Sans", 9))
    else:
        image_label.config(image=hot_image_tk, text="Image of Hot Coffee", compound="top", font=("Bubblegum Sans", 9))

# Coffee types and prices
coffee_types = {
    "Espresso": 2.5,
    "Latte": 3.5,
    "Cappuccino": 4.0,
    "Americano": 3.0
}

# Temperature types and prices
temp_types = {
    "Ice": 0,
    "Hot" : 0
}

# Create a label for the coffee selection
coffee_label = tk.Label(root, text="Select Coffee Type:", font=("Bubblegum Sans", 14), bg='#dbc1ac')
coffee_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

# Create a variable to store the selected coffee type
selected_coffee = tk.StringVar(value="Espresso")

# Create radio buttons for coffee types
for i, (coffee, price) in enumerate(coffee_types.items()):
    coffee_radio = tk.Radiobutton(root, text=f"{coffee} - ${price:.2f}", variable=selected_coffee, value=coffee, font=("Bubblegum Sans", 9), bg = "#a3826c", fg = "#fffbf2", 
                                  activebackground="#816451",  activeforeground="#fffbf2", selectcolor="#816451", indicatoron=0,width = 20)
    coffee_radio.grid(row=2 + i, column=0, columnspan=2, pady=5)

# Create a label for the temp selection
Types_label = tk.Label(root, text="Select Type:", font=("Bubblegum Sans", 14), bg="#dbc1ac")
Types_label.grid(row=len(coffee_types) + 2, column=0, columnspan=2, pady=10, sticky='ew')

# Create a variable to store the selected temp type
selected_temp = tk.StringVar(value="Ice")

# Create radio buttons for temp types
for i, (temp, price) in enumerate(temp_types.items()):
    Types_radio = tk.Radiobutton(root, text=f"{temp}", variable=selected_temp, value=temp,
                                  font=("Bubblegum Sans", 9), bg="#a3826c", fg="#fffbf2",
                                  activebackground="#816451", activeforeground="#fffbf2",
                                  selectcolor="#816451", indicatoron=0, width=20, command= update_image)
    Types_radio.grid(row=len(coffee_types) + 3 + i, column=0, columnspan=2, pady=5)

class OrderName:
    def __init__(self, root):
        self.root = root
        self.name_entry = None  # Placeholder for the Entry widget

        # Create label and entry for the user's name
        self.create_widgets()

    # Function to clear the default text when the user clicks on the entry field
    def clear_placeholder(self, event):
        if self.name_entry.get() == "Order Name Here":
            self.name_entry.delete(0, tk.END)  # Remove the placeholder
            self.name_entry.config(fg="black")  # Set the text color to black

    # Function to insert the placeholder text if the entry field is empty
    def add_placeholder(self, event):
        if not self.name_entry.get():  # If the field is empty
            self.name_entry.insert(0, "Order Name Here")  # Add the placeholder text back
            self.name_entry.config(fg="gray")  # Set the text color to gray

    # Function to validate input
    def validate_name(self):
        name = self.name_entry.get().strip()
        if name == "" or name == "Order Name Here":  # Check if the name is empty or still contains the placeholder
            messagebox.showerror("Invalid Input", "Please enter a valid name for the order.")
            return False
        return True

    # Create the label and entry widgets
    def create_widgets(self):
        # Label for the order name
        name_label = tk.Label(self.root, text="Enter Order Name:", font=("Bubblegum Sans", 12), bg='#dbc1ac')
        name_label.grid(row=11, column=0, pady=10, sticky='e')

        # Entry field for the user to input their name
        self.name_entry = tk.Entry(self.root, font=("Bubblegum Sans", 10), width=15, fg="gray")
        self.name_entry.insert(0, "Order Name Here")  # Placeholder text
        self.name_entry.grid(row=11, column=1, pady=10, sticky='w')

        # Bind the entry field to events to clear/add the placeholder
        self.name_entry.bind("<FocusIn>", self.clear_placeholder)  # Clears the text when clicked
        self.name_entry.bind("<FocusOut>", self.add_placeholder)   # Adds the placeholder back if left empty

    # Function to get the order name 
    def get_order_name(self):
        return self.name_entry.get()

# Used to get name for order
order_name_obj = OrderName(root)

# AddoneWindow set to None
AddonWindow = None

# Function for the second window
class AddonWindow:
    def __init__(self, master):
        self.master = master
        self.addon_window = None  # Placeholder for the add-on window
        self.addon_vars = {}  # Dictionary to store the state of add-on checkboxes
        self.addons = {
            "Milk": 0.5,
            "Sugar": 0.2,
            "Whipped Cream": 0.7,
            "Caramel": 0.8,
            "Chocolate": 0.8,
            "Cinnamon": 0.8,
            "French Vanilla": 0.5,
            "Hazelnut": 0.5,
            "Pumpkin Spice": 0.8
        }

    def open_addon_window(self):
        # Checks if window is already open
        if self.addon_window is None or not self.addon_window.winfo_exists():
            self.addon_window = tk.Toplevel(self.master)
            self.addon_window.title("Add-ons")
            self.addon_window.geometry("700x500")
            self.addon_window.config(bg="#dbc1ac")
            self.addon_window.lift()  # Bring this window to the front
            
            # Load the add-on image
            addon_image = Image.open("CoffeeCup.png") 
            resized_addon_image = addon_image.resize((100, 100))  
            addon_image_tk = ImageTk.PhotoImage(resized_addon_image)  # Convert to PhotoImage

            # Create a label to display the add-on image
            addon_image_label = tk.Label(self.addon_window, image=addon_image_tk, bg="#dbc1ac")  # Match the background color
            addon_image_label.image = addon_image_tk  # Keep a reference to avoid garbage collection
            addon_image_label.grid(row=11, column=1, columnspan=2, pady=10)  # Position the label in the grid

            # Create a label for the addons selection
            addons_label = tk.Label(self.addon_window, text="Select Add-ons:", font=("Bubblegum Sans", 14), bg='#dbc1ac')
            addons_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='ew')
            
            self.addon_window.grid_columnconfigure(0, weight=1)
            self.addon_window.grid_columnconfigure(1, weight=1)

            # Creates a addons checkbutton
            for i, (addon, price) in enumerate(self.addons.items()):
                var = tk.BooleanVar()
                self.addon_vars[addon] = var
                addon_checkbox = tk.Checkbutton(self.addon_window, text=f"{addon} - ${price:.2f}", variable=var,
                                                 font=("Bubblegum Sans", 9), bg="#a3826c", fg="#fffbf2",
                                                 activebackground="#816451", activeforeground="#fffbf2", 
                                                 selectcolor="#816451")
                addon_checkbox.grid(row=i + 1, column=1, columnspan=2, pady=4, sticky='w')

            # Create the "Order" button
            order_button = tk.Button(self.addon_window, text="Order Now", command=self.calculate_total,
                                     font=("Bubblegum Sans", 14), bg="#634832", fg="#fffbf2", 
                                     activebackground="#3c2f2f", activeforeground="#fffbf2")
            order_button.grid(row=len(self.addons) + 1, column=0, columnspan=2, pady=10)

            # Create the exit button
            exit_button_addon = tk.Button(self.addon_window, text="Exit Add-ons", command=self.addon_window.destroy,
                                           font=("Bubblegum Sans", 14), bg="#634832", fg="#fffbf2",
                                           activebackground="#3c2f2f", activeforeground="#fffbf2")
            exit_button_addon.grid(row=len(self.addons) + 2, column=0, columnspan=2, pady=10)
        else:
            # Displays error if window is open 
            messagebox.showwarning("Input Error", "Window is already opened.")

    #Gets the total of the order
    def calculate_total(self):
        coffee_price = coffee_types[selected_coffee.get()]
        total_addon_price = sum(price for addon, price in self.addons.items() if self.addon_vars[addon].get())
        total_price = coffee_price + total_addon_price
        
        # Makes the list for the added addons if any
        selected_addons = [addon for addon in self.addons if self.addon_vars[addon].get()]
        addon_list = ", ".join(selected_addons) if selected_addons else "None"

        # Checks to make sure name is valid
        if order_name_obj.validate_name():
            order_name = order_name_obj.get_order_name()

            # Makes list of order & displays order price
            order_summary = (f"Name: {order_name}\n"
                             f"Coffee Type: {selected_coffee.get()}\n"
                             f"Type: {selected_temp.get()}\n"
                             f"Add-ons: {addon_list}\n"
                             f"Total Price: ${total_price:.2f}")
            messagebox.showinfo("Order Summary", order_summary)

# To use to run the addonwindow
addon_window_obj = AddonWindow(root)

# Button to go to the second window    
tk.Button(root, text="NEXT", command=addon_window_obj.open_addon_window, font=("Bubblegum Sans", 14),bg="#634832", fg="#fffbf2", activebackground="#3c2f2f",  
          activeforeground="#fffbf2").grid(row=len(temp_types) + 11, column=0, columnspan=2, pady=20)

# Button to exit the application
exit_button = tk.Button(root, text="Exit", command=root.quit, font = ("Bubblegum Sans", 14),bg="#634832", fg="#fffbf2", activebackground="#3c2f2f",
                         activeforeground="#fffbf2").grid(row=len(temp_types) + 11, column=1, columnspan=2, pady=20)


# Run the main loop
root.mainloop()
