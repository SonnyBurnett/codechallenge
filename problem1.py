#!/usr/bin/python
import tkinter as tk
import threading


# Finds the nearest triangular numbers position based on the number provided, and returns the position + the
# actual triangular number. The equation used is number = n(n+1)/2 where n is the position of the triangular number
def find_nearest_triangle_number(number):
    triangle_position = int(((8 * number + 1) ** 0.5 - 1) / 2)  # Reversal of the equation "number = n(n+1)/2"
    triangle_number = int(triangle_position * (triangle_position + 1) / 2)
    return triangle_position, triangle_number


# Finds the amount of factors of a given number and returns it. It does not handle something other than positive
# numbers well, but it shouldn't encounter that problem at the moment.
def find_factor(number):
    number = int(number)
    if number ** 0.5 % 1 == float(0):  # checks whether the given number is a perfect square
        factor_amount = -1  # because of how my code works, perfect squares get one factor too many, this'll fix it
    else:
        factor_amount = 0
    for i in range(1, int(number ** 0.5) + 1):  # this code assumes a found factor, has a corresponding bigger
        if number % i == 0:  # factor that is different from the found factor. This is not the
            factor_amount += 2  # case for the square root of a perfect square, hence above correction
    return factor_amount


# Finds the first triangular number with more then the given number of factors given as an argument and returns the
# position of the triangular number in the triangular number sequence, the triangular number itself, and the amount
# of factors found.
def find_triangle_with_factor(factor_target):
    if factor_target < 1:  # it shouldn't get these, but just
        raise ValueError("The amount of factors should be a positive integer!")  # to be sure
    factor_amount = 1
    triangle_minimum_dots = factor_target ** 2  # The amount of factors of a number is higher than the square root
    triangle_position, triangle_number = find_nearest_triangle_number(triangle_minimum_dots)
    while factor_amount <= factor_target:  # bit of a brute force, and takes a bit of time when
        factor_amount = find_factor(triangle_number)  # factor_target starts to exceed 300
        triangle_position += 1
        triangle_number += triangle_position
    triangle_number -= triangle_position  # this wouldn't be necessary if the lines above were
    triangle_position -= 1  # coded more efficiently
    return triangle_position, triangle_number, factor_amount


# Creates a class that forms the basis of an application around the triangular number functions
# Because apparently I had nothing better to do this weekend
class TriangleCalculatorInator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.variable_status = tk.StringVar()   # stores feedback to the user
        self.variable_wrong_input_counter = tk.IntVar()  # if you're reading this, you'll probably find out what this is
        self.variable_input = tk.StringVar()    # This stores the input in the entrybox self.entry (inspiring name)
        self.master = master
        self.variable_wrong_input_counter.set(0)
        self.master.bind("<Return>", self.event_user_pressed_return)
        self.pack()
        self.create_widgets()  # Where all the amazing gui magic happens

    # gui design magic. My friend with a Masters in graphics design would probably have some remarks about this
    def create_widgets(self):
        self.frame_entry = tk.Frame(self)
        self.frame_entry.pack(padx=10, pady=5, side="top")

        self.frame_buttons = tk.Frame(self, height=30, width=420)
        self.frame_buttons.pack(side="bottom")
        self.frame_buttons.pack_propagate(0)

        self.frame_message = tk.Frame(self, height=100, width=400)
        self.frame_message.pack(padx=10, pady=10, side="left", anchor="n")
        self.frame_message.pack_propagate(0)

        self.message_status = tk.Message(self.frame_message, textvariable=self.variable_status,
                                         font=('Çonsolas', 10), width=400, anchor="w")
        self.message_status.pack(side="left")

        self.label_entry = tk.Label(self.frame_entry, text="Desired amount of factors:")
        self.label_entry.pack(side="left")

        self.button_calculate = tk.Button(self.frame_entry)
        self.button_calculate["text"] = "calculate-inate"
        self.button_calculate["command"] = self.command_user_input_cleanup
        self.button_calculate.pack(side="right")

        self.entry = tk.Entry(self.frame_entry, textvariable=self.variable_input)
        self.entry.pack(side="right")
        self.entry.focus_set()

        self.quit = tk.Button(self.frame_buttons, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="right", anchor="e", padx=5, pady=5)

    # Uses the string entered in the entrybox self.entry, "cleans it up" a bit and feeds it to find_triangle_with_factor
    # It then stores the returned values in designated class variables
    def command_user_input_cleanup(self):
        wrong_input_counter = self.variable_wrong_input_counter.get()
        user_input = self.variable_input.get()
        self.variable_input.set("")
        self.button_calculate.configure(state="disabled")
        if user_input == "":
            self.variable_status.set("You should probably enter at least something...")
            self.button_calculate.configure(state="normal")
            wrong_input_counter += 1
            self.variable_wrong_input_counter.set(wrong_input_counter)
            self.update_idletasks()
        elif ";" in user_input:
            self.variable_status.set("Are you trying to use code injection? How rude!")
            self.button_calculate.configure(state="normal")
            wrong_input_counter += 1
            self.variable_wrong_input_counter.set(wrong_input_counter)
            self.update_idletasks()
        else:
            try:
                factor_target = int(user_input)
            except ValueError:
                self.variable_status.set("This should be a number... an integer to be precise")
                self.button_calculate.configure(state="normal")
                self.update_idletasks()
                wrong_input_counter += 1
                self.variable_wrong_input_counter.set(wrong_input_counter)
            else:
                if factor_target < 1:
                    self.variable_status.set("The amount of factors should be a positive integer")
                    self.button_calculate.configure(state="normal")
                    wrong_input_counter += 1
                    self.variable_wrong_input_counter.set(wrong_input_counter)
                    self.update_idletasks()
                else:
                    if factor_target == 500:
                        self.variable_status.set(
                            "The little hamsters in my code are processing your request,\nthis'll take a few seconds")
                        self.update_idletasks()
                    elif factor_target > 300:
                        self.variable_status.set(
                            "If you can read this, that means you've entered such a big number,\nmy poor code needs "
                            "some time to process your outrageous request.\nPlease be patient... you monster")
                        self.update_idletasks()
                    wrong_input_counter = 0
                    self.variable_wrong_input_counter.set(wrong_input_counter)
                    calculation_thread = threading.Thread(name="calculation_thread", target=self.command_calculate,
                                                          args=(6, factor_target),  # the 6 isn't used, but necessary
                                                          daemon=True)
                    calculation_thread.start()
        if wrong_input_counter == 3:
            self.variable_input.set("")
            self.variable_status.set("Could you stop testing my input string cleanup?")
            wrong_input_counter = 0
            self.variable_wrong_input_counter.set(wrong_input_counter)

    # creates a thread to do the calculations, as it may take some time with large numbers.
    # Had some problems with passing the arguments via the threading module, as it wanted an iterable item as arguments
    # Added "dummy"-argument as a quick fix
    def command_calculate(self, dummy, factor_target):      # dummy isn't used, but is needed to keep things working
        calculated_triangle_data = find_triangle_with_factor(factor_target)
        self.variable_status.set("Position:                    %-10i\nTriangular number:      %-10i\nFactors:"
                                 "                     %-10i"
                                 % calculated_triangle_data)
        self.button_calculate.configure(state="normal")

    def event_user_pressed_return(self, event):
        self.command_user_input_cleanup()


# The following part starts the gui
root = tk.Tk()
root.title("Triangular_Number_Finder-inator 3000")  # Its a cool name, don't judge!
root.geometry("420x150+300+300")
root.resizable(0, 0)
app = TriangleCalculatorInator(master=root)
app.mainloop()
