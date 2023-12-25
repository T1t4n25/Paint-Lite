from tkinter import *
import math
shape = 0
pixel_size = 2
connected_lines = True
sides = 360

def draw_polygon(event):
    global click_num
    global center_x, center_y
    global sides

    if click_num == 0:
        center_x = event.x
        center_y = event.y
        click_num = 1
    else:
        radius = math.sqrt((event.x - center_x)**2 + (event.y - center_y)**2)
        draw_regular_polygon(center_x, center_y, radius, sides)
        click_num = 0

def draw_regular_polygon(center_x, center_y, radius, sides):
    angle_increment = 360 / sides  # Angle increment in degrees
    current_angle = 0

    x1, y1 = center_x + radius * math.cos(math.radians(current_angle)), center_y - radius * math.sin(math.radians(current_angle))

    for _ in range(sides):
        current_angle += angle_increment
        x2 = center_x + radius * math.cos(math.radians(current_angle))
        y2 = center_y - radius * math.sin(math.radians(current_angle))
        ddaLine(x1, y1, x2, y2, pixel_size)
        x1, y1 = x2, y2

def draw_line(event):
    global click_num
    global x1, y1
    if click_num == 0:
        x1 = event.x
        y1 = event.y
        click_num = 1
        
        #canvas.image.put('black', (x1-pixel_size, y1-pixel_size, x1+pixel_size, y1+pixel_size))
    else:
        global x2
        global y2
        x2 = event.x
        y2 = event.y
        ddaLine(x1, y1, x2, y2, pixel_size)
        click_num = 0
        if connected_lines:
            x1, y1 = x2, y2
            click_num = 1
        #canvas.image.put('black', (x1-pixel_size, y1-pixel_size, x1+pixel_size, y1+pixel_size))

def ddaLine(x1, y1, x2, y2, pixel_size):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    steps = steps if steps > 0 else 1
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for i in range(round(steps)):
        x1 += xinc
        y1 += yinc
        canvas.create_rectangle(round(x1)-pixel_size, round(y1)-pixel_size, round(x1)+pixel_size, round(y1)+pixel_size, fill='black', outline='')
def rectDraw(x1, y1, x2, y2, pixel_size):
    ddaLine(x1, y2, x2, y2, pixel_size)
    ddaLine(x2, y2, x2, y1, pixel_size)
    ddaLine(x2, y1, x1, y1, pixel_size)
    ddaLine(x1, y1, x1, y2, pixel_size)

def RegularPolygon(x1, y1, x2, y2, pixel_size):
    pass

window = Tk()
canvas = Canvas(window, width=600, height=600, background='white')
canvas.pack()
image = PhotoImage(width=600, height=600)
canvas.image = image
canvas.create_image((300, 300), image=image, state="normal")
canvas.bind('<Button-1>', draw_polygon)

click_num = 0

window.mainloop()
