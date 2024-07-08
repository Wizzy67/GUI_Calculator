import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display input/output
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons with a loop
        for button_text, row, column in buttons:
            tk.Button(root, text=button_text, padx=40, pady=20,
                      command=lambda text=button_text: self.handle_click(text)).grid(row=row, column=column)

        # Initialize the calculator state
        self.reset_calculator()

    def reset_calculator(self):
        self.current_number = ""
        self.operator = None
        self.first_number = None
        self.entry.delete(0, tk.END)

    def handle_click(self, value):
        if value.isdigit() or value == '.':
            self.current_number += value
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_number)
        elif value in ['+', '-', '*', '/']:
            self.operator = value
            if self.first_number is None:
                self.first_number = float(self.current_number)
            else:
                self.calculate_result()
            self.current_number = ""
        elif value == '=':
            if self.operator and self.current_number:
                self.calculate_result()

    def calculate_result(self):
        second_number = float(self.current_number)
        if self.operator == '+':
            result = self.first_number + second_number
        elif self.operator == '-':
            result = self.first_number - second_number
        elif self.operator == '*':
            result = self.first_number * second_number
        elif self.operator == '/':
            if second_number == 0:
                result = "Error: Division by zero"
            else:
                result = self.first_number / second_number

        self.entry.delete(0, tk.END)
        self.entry.insert(0, result)

        # Update first_number for chaining operations
        self.first_number = result
        self.current_number = ""

# Create the main window
root = tk.Tk()
app = CalculatorApp(root)

# Run the main loop
root.mainloop()
