from tkinter import *

def draw_line(event):
    global click_num
    global x1, y1
    if click_num == 0:
        x1 = event.x
        y1 = event.y
        click_num = 1
        pixel_size = 1  # Adjust this value based on the size you want for your pixel
        #canvas.image.put('black', (x1, y1))
    else:
        global x2
        global y2
        x2 = event.x
        y2 = event.y
        pixel_size = 1  # Adjust this value based on the size you want for your pixel
        ddaLine(x1,y1,x2,y2)
        click_num = 0

def ddaLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for i in range(steps):
        x1 += xinc
        y1 += yinc
        canvas.image.put('black', (round(x1), round(y1)))


window = Tk()
canvas = Canvas(window, width=400, height=400, background='white')
canvas.pack()
image = PhotoImage(width=400, height=400)
canvas.image = image
canvas.create_image((200, 200), image=image, state="normal")
canvas.bind('<Button-1>', draw_line)

click_num = 0

window.mainloop()
