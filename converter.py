from tkinter import *

# Tk class

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


# Label class
label_one = Label(text="is equal to")
label_one.grid(column=0, row=1)

label_two = Label(text="Miles")
label_two.grid(column=2, row=0)

label_three = Label(text = "Km")
label_three.grid(column=2, row=1)

label_four = Label(text = 0)
label_four.grid(column=1, row=1)

# Entry class
input = Entry(width=10)
input.grid(column=1, row=0)

# Button class
def buttonclick():
    label_four["text"] = float(input.get()) * 1.609344

cal_button = Button(text="Calculate", command=buttonclick)
cal_button.grid(column=1, row =2)




window.mainloop()