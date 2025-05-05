import tkinter 
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog 
import PIL.ImageGrab as ImageGrab 
whiteboard  = Tk()

current_value = tkinter.DoubleVar(whiteboard, 1)

def get_current_value():
    return '{: .2}'.format(current_value.get())

def set_color(new_color):
    global color, line_width, cursor_color

    color = new_color
    line_width = get_current_value() 

def locate_xy(work):
    global current_x, current_y

    current_x = work.x
    current_y = work.y


def eraser():
    set_color('white')

def draw(work):
    global current_x, current_y

    line_width = get_current_value()

    whiteboard_canvas.create_oval((current_x, current_y, work.x, work.y), outline= color, width=line_width)
    current_x = work.x
    current_y = work.y


def create_colour(position_y, c_opt):

    color = ''

    if c_opt == 1 :
        color = 'black'
    elif c_opt == 2 :
        color = 'red'
    elif c_opt == 3:
        color = 'brown'
    elif c_opt == 4:
        color = 'blue'
    elif c_opt == 5:
        color = 'yellow'
    elif c_opt == 6:
        color = 'green'
    elif c_opt == 7:
        color = '#FFFFFE' 


    id = colour_palette_canvas.create_rectangle((12,position_y,42,position_y+30), fill=color)
    colour_palette_canvas.tag_bind(id, '<Button-1>', lambda x: set_color(color))

def clear_all():
    c_opt = 1
    position_y = 10
    counter = 1

    whiteboard_canvas.delete('all')
    for counter in range(1, 8):
        create_colour(position_y, c_opt)
        c_opt += 1
        position_y += 40

def saveImage():

    fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")

    x = whiteboard.winfo_rootx()+100
    y = whiteboard.winfo_rooty()+35

    img = ImageGrab.grab(bbox=(x,y,x+900,y+470))

    img.show()

    img.save(fileLocation)


whiteboard.title("Whiteboard")

whiteboard.geometry("1050x570+150+50")


whiteboard.resizable(False, False)

whiteboard.configure(bg="#d3d3d3") 



whiteboard.iconbitmap(default="icon/whiteboard.ico")


color_sidebar_image = PhotoImage(file="images/color_sidebar.png")
eraser_image = PhotoImage(file="images/eraser.png")
garbage_image = PhotoImage(file="images/garbage.png")
save_image = PhotoImage(file="images/save.png")


slider = ttk.Scale(whiteboard, from_=2, to=100, orient='horizontal', variable= current_value)
slider.place(x=100, y=525)

color_sidebar_label = Label(whiteboard, image=color_sidebar_image, bg="#d3d3d3")
color_sidebar_label.place(x=10, y=15)
slider_value_label = ttk.Label(whiteboard, text="thickness")
slider_value_label.place(x=210, y=530)


colour_palette_canvas = Canvas(whiteboard, bg="#ffffff", width=50, height=290, bd=0)
colour_palette_canvas.place(x=20, y=40)
whiteboard_canvas = Canvas(whiteboard, width=900, height=470, bg="#ffffff", cursor="dot blue")
whiteboard_canvas.place(x=100, y=35)


eraser_button = Button(whiteboard, image=eraser_image, bg="#f2f3f5", command=eraser)
eraser_button.place(x=25, y=340)
garbage_button = Button(whiteboard, image=garbage_image, bg="#f2f3f5", command=clear_all)
garbage_button.place(x=25, y=395)
save_button = Button(whiteboard, image=save_image, bg="#f2f3f5", command=saveImage)
save_button.place(x=25, y=450)

c_opt = 1 
position_y = 10
counter = 1
for counter in range(1, 8):
    create_colour(position_y, c_opt)
    c_opt += 1
    position_y += 40

set_color('black')

whiteboard_canvas.bind('<Button-1>', locate_xy)
whiteboard_canvas.bind('<B1-Motion>', draw)
whiteboard.mainloop()
