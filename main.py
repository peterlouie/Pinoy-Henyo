import os
import random
import time
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.font import BOLD
from PIL import ImageTk, Image

# Root set-up
root = Tk()
root.title("Pinoy Henyo")
root.geometry("750x950")
root.configure(bg="#1eaad2")
root.resizable(False, False)

def hide_all_frame():
     for widget in imageframe.winfo_children():
         widget.destroy()
     imageframe.pack_forget()

def info():
    top= Toplevel(root)
    top.geometry("300x150")
    top.title("Developer Info")
    message = """
    This is develop by Peter Louie Linatoc.
    Follow me: https://github.com/peterlouie
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
    imageframe.config(bg='#1eaad2')

    global selected_image
    selected_image = ImageTk.PhotoImage(Image.open(image_location).resize((600, 600)))
    global show_image
    show_image = Label(imageframe, image=selected_image)
    show_image.pack(pady=5)
    #print("game started")
    
    answer = random_image
    answer = answer.replace(".jpg", "")
    answer = answer.replace(".png", "")

    text_label1 = Label(imageframe, text=f"{answer}",
                        font=("Noto Sans", 20), bg='#9a411b').pack()

#Introduction on the application
close_button = Button(root, text="developer info", command=info, bg='#ba833d')
close_button.place(y=920, x=0)

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
imageframe = Frame(root)

# Timer
hour=StringVar()                                                       
minute=StringVar()
second=StringVar()
running=False

hour=StringVar()                                                       
minute=StringVar()
second=StringVar()
running=False

# setting the default value as 0
hour.set("00")
minute.set("02")
second.set("00")
  
# Use of Entry class to take input from the user
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=300,y=840)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=370,y=840)

clock_seperator_label = Label(root, text=":", font=("Arial",18,BOLD), bg="#1eaad2")
clock_seperator_label.place(x=352, y=840)
  
def update():
    global temp, running

    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:02d}".format(hours))
        minute.set("{0:02d}".format(mins))
        second.set("{0:02d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
  
        if running == False:
            break

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 1):
            top = Toplevel(root)
            top.geometry("330x50")
            top.title("Game Over!!!")
            message = "Times Up!!! Hope you WIN"
            Label(top, text=message, font=("Noto Sans", 18)).pack(
                    fill='both', expand=True)
        # after every one sec the value of temp will be decremented
        # by one

        temp -= 1
 
def start():
    global running
    running = True
    update()

def pause():
    global running
    if running:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        running = False

def reset():
    global running, hour, minute, second
    if running:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        running = False
    hour.set('00')
    minute.set('00')
    second.set('00')

# button widget
start = Button(root, text='Start', bd='5', bg='#53da43',
             command=start)
start.place(y=890, x=330)

pause = Button(root, text='Pause', bd='5', bg='#43dad1',
             command= pause)
pause.place(y=890, x=230)

reset = Button(root, text='Reset', bd='5', bg='#B54343',
             command= reset)
reset.place(y=890, x=420)

root.mainloop()
