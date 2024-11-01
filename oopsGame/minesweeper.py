from tkinter import *
import Utils
import settings

root = Tk()
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='#F5F5DC',
    width=settings.WIDTH,
    height=Utils.width_prct(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame(
    root, 
    bg='#DAB49D',
    height=Utils.hight_prct(75),
    width=Utils.width_prct(25)
)

left_frame.place(x=0, y=180)

center_frame = Frame(
    root, 
    bg='#F8F8FF',
    height=Utils.hight_prct(75),
    width=Utils.width_prct(75)
)

center_frame.place(x=Utils.width_prct(25), y=Utils.hight_prct(25))

root.mainloop()