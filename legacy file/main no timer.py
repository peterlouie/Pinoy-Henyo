import os
import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Root set-up
root = Tk()
root.title("Pinoy Henyo")
root.geometry("1000x1000")
root.resizable(False, False)

def info():
    top= Toplevel(root)
    top.geometry("300x150")
    top.title("Child Window")
    message = """
    This is develop by Peter Louie Linatoc
    If you like this application.
    You can buy me a beer
    GCASH = 0945 200 0712
    Thanks for the support 😀
    """
    Label(top, text= message, font=('Noto Sans', 10)).grid()

def choose_category():
    images_for_guess = []

    for photo in os.listdir("category/" + selected_category.get()):
        images_for_guess.append(photo)

    global random_image
    random_image = random.choice(images_for_guess)
   
    global image_location
    image_location = "category/" + selected_category.get() + "/" + random_image
    
    start_game()

    #print(image_location)
    #print(type(image_location))

def start_game():
    hide_all_frame()
    imageframe.pack(pady=5)

    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(image_location).resize((600, 600)))
    global show_image
    show_image = Label(imageframe, image=selected_image)
    show_image.pack(pady=5)
    #print("game started")
    
    answer = random_image
    answer = answer.replace(".jpg", "")
    answer = answer.replace(".png", "")

    text_label1 = Label(imageframe, text=f"Correct Answer: {answer}",
                        font=("Noto Sans", 20)).pack()

    timer_start = Button(imageframe, text="Start Timer", command=start_timer).pack()

    timerframe.pack()

    global minute
    minute=StringVar()
    global second
    second=StringVar()

    minute.set("02")
    second.set("00")

    minuteEntry= Entry(timerframe, width=3, font=("Arial",18,""),
                   textvariable=minute)
    minuteEntry.grid(row=0, column=0)

    secondEntry= Entry(timerframe, width=3, font=("Arial",18,""),
                   textvariable=second)
    secondEntry.grid(row=0, column=1)

def start_timer():
    try:
        temp = int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >- 1:

        secs = divmod(temp, 60)
    
    mins = 0

    if sec == 0:
        


#Introduction on the application
close_button = Button(root, text="developer info", command=info)
close_button.place(y=970, x=0)

label_intro = Label(root, text="Pinoy Henyo", 
                    font=("Noto Sans", 35),
                    bg="yellow")
label_intro.pack(pady=5, fill="both")


categories = []

for category in os.listdir("category"):
    categories.append(category)

#dropdown menu
selected_category = StringVar()
selected_category.set("Click to Select Category")
dropdown_menu = OptionMenu(root, selected_category, *categories) 
dropdown_menu.config( bg="light green", 
                     direction="below", font=("Noto Sans", 15))
dropdown_menu.pack(pady=10)

choose_category = Button(root, text="Click to choose Image", command=choose_category)
choose_category.pack()

def hide_all_frame():
     for widget in imageframe.winfo_children():
         widget.destroy()
     imageframe.pack_forget()

     for widget in timerframe.winfo_children():
         widget.destroy()
     timerframe.pack_forget()

imageframe = Frame(root)
timerframe = Frame(root)

root.mainloop()
