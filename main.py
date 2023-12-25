from tkinter import *
shape = 0
pixel_size = 5
connected_lines = True
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
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for i in range(steps):
        x1 += xinc
        y1 += yinc
        canvas.image.put('black', (round(x1)-pixel_size, round(y1)-pixel_size, round(x1)+pixel_size, round(y1)+pixel_size))

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
canvas.bind('<Button-1>', draw_line)

click_num = 0

window.mainloop()
