import tkinter as tk
from tkinter import Label, messagebox
from PIL import ImageTk, Image
# starting of code 
selected_items = []#array to store items 
total = 0#total for totaling 
#function for login if user already registered 
def login():
    r10 = tk.Tk()
    r10.geometry("400x200")
    r10.title("LOGIN PLEASE")
    r10.eval('tk::PlaceWindow . center')
    mobile_label = tk.Label(r10, text="Enter Mobile Number:")
    mobile_label.pack()
    mobile_entry = tk.Entry(r10)
    mobile_entry.pack()
#function to login function
    def check_login():
        mobile_number = mobile_entry.get()
    
        with open("a.txt", "r") as file:
                registered_numbers = file.read().splitlines()
                if mobile_number in registered_numbers:
                    r10.destroy()
                    menu_window()
                else:
                    r10.destroy()
                    messagebox.showerror("Error", "Mobile number not registered")
       
    login_button = tk.Button(r10, text="LOGIN", bg='pink', command=check_login)
    login_button.pack(anchor='center')
# funtion to check signup 
def signup():
    r11 = tk.Tk()
    r11.geometry("400x200")
    r11.title("SIGNUP PLEASE")
    r11.eval('tk::PlaceWindow . center')

    mobile_label = tk.Label(r11, text="Enter Mobile Number:")
    mobile_label.pack()

    mobile_entry = tk.Entry(r11)
    mobile_entry.pack()
#function to register
    def register():
        mobile_number = mobile_entry.get()
        with open("a.txt", "a") as file:
            file.write(mobile_number + "\n")
            r11.destroy()
        messagebox.showinfo("Success", "Mobile number registered successfully")
        menu_window()

    signup_button = tk.Button(r11, text="SIGNUP", bg='pink', command=register)
    signup_button.pack(padx=10,pady=10, anchor='center')
# function to check menu_window 
def menu_window():
    global total_label
    root = tk.Tk()
    root.title("Menu")
    root.geometry("800x800")
    root.eval('tk::PlaceWindow . center')

    frame = tk.Frame(root, padx=10, pady=10, bg="Yellow")
    button1 = tk.Button(frame, text="Veg", bg='pink', command=func1)
    button1.pack(side=tk.LEFT, padx=100, pady=100)
    button2 = tk.Button(frame, text="NonVeg", bg='pink', command=func2)
    button2.pack(side=tk.RIGHT, padx=100, pady=100)
    frame.pack()

    total_label = tk.Label(root,
                           text="DEAR CUSTOMER YOUR TOTAL IS : 0",
                           anchor=tk.CENTER,
                           bg="lightblue",
                           height=3,
                           width=40,
                           bd=3,
                           font=("Arial", 16, "bold"),
                           cursor="hand2",
                           fg="red",
                           padx=15,
                           pady=15,
                           justify=tk.CENTER,
                           relief=tk.RAISED,
                           underline=0
    )
   
    submit_button = tk.Button(root, text="Submit", command=display_total)
    submit_button.pack()
    
    total_label.pack()
    root.mainloop()
#function  for vegetarians 
def func1():
    root1 = tk.Tk()
    root1.geometry("400x400")
    root1.title("Vegetarians")
    root1.eval('tk::PlaceWindow . center')

    frame1 = tk.Frame(root1, padx=10, pady=10, bg="GREEN")
    button3 = tk.Button(root1, text="VEG STARTERS", bg='pink', command=lambda: button_click(120, "VEG STARTERS"))
    button3.grid(row=0, column=0)

    button4 = tk.Button(root1, text="NOODLES", bg='pink', command=lambda: button_click(180, "NOODLES"))
    button4.grid(row=1, column=0)
    

    button5 = tk.Button(root1, text="RICE", bg='pink', command=lambda: button_click(210, "RICE"))
    button5.grid(row=2, column=0)
    button6 = tk.Button(root1, text="SOUP", bg='pink', command=lambda: button_click(300, "SOUP"))
    button6.grid(row=3, column=0)
    button7 = tk.Button(root1, text="COMBOS", bg='pink', command=lambda: button_click(350, "COMBOS"))
    button7.grid(row=4, column=0)
    button8 = tk.Button(root1, text="FRENCH FRIES", bg='pink', command=lambda: button_click(350, "FRENCH FRIES"))
    button8.grid(row=5, column=0)
    button9 = tk.Button(root1, text="PIZZA", bg='pink', command=lambda: button_click(100, "PIZZA"))
    button9.grid(row=6, column=0)
    button10 = tk.Button(root1, text="PASTA", bg='pink', command=lambda: button_click(100, "PASTA"))
    button10.grid(row=7, column=0)
    button11 = tk.Button(root1, text="GARLIC BREAD", bg='pink', command=lambda: button_click(100, "GARLIC BREAD"))
    button11.grid(row=8, column=0)
    button12 = tk.Button(root1, text="MAGGI", bg='pink', command=lambda: button_click(100, "MAGGI"))
    button12.grid(row=9, column=0)
    button13 = tk.Button(root1, text="BURGER", bg='pink', command=lambda: button_click(100, "BURGER"))
    button13.grid(row=10, column=0)
    button14 = tk.Button(root1, text="SANDWICHES", bg='pink', command=lambda: button_click(100, "SANDWICHES"))
    button14.grid(row=11, column=0)
    button16 = tk.Button(root1, text="MOMOS", bg='pink', command=lambda: button_click(100, "MOMOS"))
    button16.grid(row=12, column=0)
    frame1.pack()
#function for Non Vegetarians
def func2():
    root2 = tk.Tk()
    root2.geometry("400x400")
    root2.title("NON VEGETARIANS")
    root2.eval('tk::PlaceWindow . center')

    frame2 = tk.Frame(root2, padx=100, pady=100)
    button19 = tk.Button(root2, text="NON VEG STARTERS", bg="pink", command=lambda: button_click(100, "NON VEG STARTERS"))
    button19.grid(row=0, column=0)
    button20 = tk.Button(root2, text="NOODLES", bg="pink", command=lambda: button_click(100, "NOODLES"))
    button20.grid(row=1, column=0)
    button21 = tk.Button(root2, text="RICE", bg="pink", command=lambda: button_click(100, "RICE"))
    button21.grid(row=2, column=0)
    button22 = tk.Button(root2, text="SOUP", bg="pink", command=lambda: button_click(100, "SOUP"))
    button22.grid(row=3, column=0)
    button23 = tk.Button(root2, text="COMBOS", bg="pink", command=lambda: button_click(100, "COMBOS"))
    button23.grid(row=4, column=0)
    button25 = tk.Button(root2, text="PIZZA", bg="pink", command=lambda: button_click(100, "PIZZA"))
    button25.grid(row=6, column=0)
    button26 = tk.Button(root2, text="PASTA", bg="pink", command=lambda: button_click(100, "PASTA"))
    button26.grid(row=7, column=0)
    button27 = tk.Button(root2, text="GARLIC BREAD", bg="pink", command=lambda: button_click(100, "GARLIC BREAD"))
    button27.grid(row=8, column=0)
    button28 = tk.Button(root2, text="MAGGI", bg="pink", command=lambda: button_click(100, "MAGGI"))
    button28.grid(row=9, column=0)
    button29 = tk.Button(root2, text="BURGER", bg="pink", command=lambda: button_click(100, "BURGER"))
    button29.grid(row=10, column=0)
    button30 = tk.Button(root2, text="SANDWICHES", bg="pink", command=lambda: button_click(100, "SANDWICHES"))
    button30.grid(row=11, column=0)
    button32 = tk.Button(root2, text="MOMOS", bg="pink", command=lambda: button_click(100, "MOMOS"))
    button32.grid(row=12, column=0)
    frame2.pack()
#function to check add price according to item 
def button_click(price, item):
    global total
    total += price
    selected_items.append(item)
    total_label.config(text="DEAR CUSTOMER YOUR TOTAL IS : " + str(total))
#function to display total 
def display_total():

    messagebox.showinfo("Total", "DEAR CUSTOMER YOUR TOTAL IS : " + str(total))
#function to display login and signup
def m():
    r = tk.Tk()
    r.title("Welcome")
    r.geometry('500x300')
    r.eval('tk::PlaceWindow . center')

    t = tk.StringVar()
    button25 = tk.Button(r, text="LOGIN", bg='pink', command=login)
    button25.pack(anchor='center')
    button26 = tk.Button(r, text="SIGNUP", bg='pink', command=signup)
    button26.pack(anchor='center')

    r.mainloop()
#function for intro 
def intro():
    r6 = tk.Tk()
    r6.title("APNA FOOD ADDA")
    r6.geometry("600x500")
    r6.eval('tk::PlaceWindow . center')
    frame = tk.Frame(r6, width=500, height=400)
    frame.place(anchor='center')
    img = ImageTk.PhotoImage(Image.open("/home/aayushi/Downloads/food1.jpg"))  
    label = Label(frame, image=img)
    frame.pack()
    label.pack()
    button100 = tk.Button(r6, text="GO", bg='pink', command=m)
    button100.pack(anchor='center')
    r6.mainloop()

intro()

