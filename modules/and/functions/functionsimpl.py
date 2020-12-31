import tkinter
import math


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    width = (80 - len(text)) // 2
    return " " * width + text


def center_text2(*args, sep_char=' ', end_char='\n', file_name=None, flush_me=False):
    text = " ".join(str(args))
    width = (80 - len(text)) // 2
    print(" " * width, text, sep=sep_char, end=end_char, file=file_name, flush=flush_me)


def circle(page, radius, g, h):
    for x_cor in range(g, (g + radius)):
        y_cor = h + (math.sqrt(radius ** 2 - ((x_cor - g) ** 2)))
        plot(page, x_cor, y_cor)
        plot(page, x_cor, 2 * h - y_cor)
        plot(page, 2 * g - x_cor, y_cor)
        plot(page, 2 * g - x_cor, 2 * h - y_cor)


def parabola(page, size):
    for x_cor in range(0, size):
        y_cor = x_cor * x_cor
        plot(page, x_cor, -y_cor)
        plot(page, -x_cor, -y_cor)


def draw_axes(canvas_current):
    canvas_current.update()
    x_origin = canvas_current.winfo_width() / 2
    y_origin = canvas_current.winfo_height() / 2
    canvas_current.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_current.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas_current.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas_current, x_cor, y_cor):
    canvas_current.create_line(x_cor, y_cor, x_cor+1, y_cor+1, fill="red")


with open("menu", "w") as menu:
    s1 = center_text(1, 2)
    print(s1, file=menu)
    print(center_text("Eggs, Eggs"), file=menu)
    print(center_text("Spam", "Eggs", "Spam", sep=":"), file=menu)
    s2 = center_text(12, 13, 14, 15, 16,)
    print(s2, file=menu)

mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)

parabola(canvas, 100)
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)

mainWindow.mainloop()
