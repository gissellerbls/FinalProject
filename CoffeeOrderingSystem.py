"""

Author: Gisselle Robles
Date written: 9/29/2024
Assignment:   Final Project
Short Desc:  This GUI is a coffee ordering system that gives the user options of toppings and types of coffee.
The program will show the total.

"""

import tkinter as tk
from tkinter import messagebox

# Main application window/ needing to work on other window with pictures
root = tk.Tk()
#root.configure( bg= ) still thinking of color
root.title("Coffee Ordering System")
root.geometry("700x500")

# Coffee types and prices
coffee_types = {
    "Espresso": 2.5,
    "Latte": 3.5,
    "Cappuccino": 4.0,
    "Americano": 3.0
}

# Add-ons and prices
addons = {
    "Milk": 0.5,
    "Sugar": 0.2,
    "Whipped Cream": 0.7,
    "Caramel": 0.8,
    "Chocolate": 0.8,
    "Cinnamon": 0.8
}

# Create a label for the coffee selection
coffee_label = tk.Label(root, text="Select Coffee Type:", font=("Bubblegum Sans", 14))
coffee_label.pack(pady=10)

# Create a variable to store the selected coffee type
selected_coffee = tk.StringVar(value="Espresso")

# Create radio buttons for coffee types
for coffee, price in coffee_types.items():
    coffee_radio = tk.Radiobutton(root, text=f"{coffee} - ${price:.2f}", variable=selected_coffee, value=coffee)
    coffee_radio.pack(anchor="w")

# Create a label for the add-ons
addons_label = tk.Label(root, text="Select Add-ons:", font=("Bubblegum Sans", 14))
addons_label.pack(pady=10)

# Create variables for add-ons
addon_vars = {}
for addon, price in addons.items():
    var = tk.BooleanVar()
    addon_vars[addon] = var
    addon_checkbox = tk.Checkbutton(root, text=f"{addon} - ${price:.2f}", variable=var)
    addon_checkbox.pack(anchor="w")

# Function to calculate total price
def calculate_total():
    # Get the price of the selected coffee
    coffee_price = coffee_types[selected_coffee.get()]

    # Calculate the add-on prices
    total_addon_price = sum(price for addon, price in addons.items() if addon_vars[addon].get())

    # Calculate the total price
    total_price = coffee_price + total_addon_price

    # Show the total price
    messagebox.showinfo("Total Price", f"Your total is: ${total_price:.2f}")

# Create the "Order" button
order_button = tk.Button(root, text="Order Now", command=calculate_total, font=("Bubblegum Sans", 14), bg="#E6E6FA", fg="white")
order_button.pack(pady=20)

# Run the main loop
root.mainloop()