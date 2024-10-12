# FinalProject
User Manual for Coffee Ordering System GUI
Table of Contents


1.	Introduction
2.	System Requirements
3.	Installation
4.	Getting Started
5.	User Interface Overview
6.	How to use Application
7.	Input Validation
8.	Exiting the Application
9.	Troubleshooting



1. Introduction
The Coffee Ordering System is a graphical user interface (GUI) application designed to allow users to select their preferred coffee type, temperature, and additional toppings or add-ons. The application calculates the total price of the order and provides an order summary for the user.
2. System Requirements
•	Python 3.x installed on your system
•	Required libraries:
o	tkinter: Standard GUI toolkit for Python
o	PIL (Pillow): Required for image handling
3. Installation
1.	Install Python 3.x from python.org.
2.	Install the required library using pip:
pip install Pillow
3.	Ensure you have the necessary image files (IceCoffee.png, HotCoffee.png, CoffeeCup.png) in the same directory as the Python script.
4. Getting Started
1.	Download the provided code and save it as coffee_ordering_system.py.
2.	Open a terminal or command prompt.
3.	Navigate to the directory where the script is saved.
4.	Run the application using the command:
python coffee_ordering_system.py
5. User Interface Overview
The application consists of two main windows:
Main Window
•	Coffee Type Selection: Choose from various coffee types (Espresso, Latte, Cappuccino, Americano) using radio buttons.
•	Temperature Type Selection: Choose between Ice and Hot coffee using radio buttons.
•	Order Name Input: Enter the name for your order in the designated text entry box.
•	Next Button: Navigate to the add-ons selection window.
•	Exit Button: Close the application.
Add-ons Window
•	Add-ons Selection: Check boxes for various add-ons (e.g., Milk, Sugar, Whipped Cream) with their respective prices.
•	Order Now Button: Calculate and display the order summary with the total price.
•	Exit Add-ons Button: Close the add-ons window and return to the main window.
6. How to Use the Application
1.	Select Coffee Type: Click on the radio button corresponding to your preferred coffee type.
2.	Select Temperature: Choose either Ice or Hot by clicking the respective radio button.
3.	Enter Order Name: Click in the text entry box labeled "Enter Order Name" and type your desired order name. The placeholder text will disappear when you click inside the box.
4.	Navigate to Add-ons: Click the "NEXT" button to open the add-ons window.
5.	Select Add-ons: In the add-ons window, check the boxes for any additional toppings you would like to include with your order.
6.	Place Order: Click the "Order Now" button to calculate your total order price and view the order summary in a message box.
7.	Return to Main Window: If you wish to go back to the main window, click the "Exit Add-ons" button.
8.	Exit Application: Click the "Exit" button on the main window to close the application.
7. Input Validation
•	The application ensures that the order name is not empty or the placeholder text "Order Name Here."
•	If validation fails, an error message will prompt you to enter a valid name.
8. Exiting the Application
•	To exit the application, click the "Exit" button located on the main window. This will terminate the application.
9. Troubleshooting
•	Issue: The application does not run.
o	Solution: Ensure Python and required libraries are installed correctly.
•	Issue: Images do not display.
o	Solution: Verify that the image files are located in the same directory as the Python script.
