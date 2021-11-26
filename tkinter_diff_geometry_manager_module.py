import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame4= tk.Frame(master=window, width=150, height=150)
frame4.pack(side=tk.LEFT)

lbl1 = tk.Label(master=frame4, text='I am at (0,0)', bg='red')
lbl1.place(x=0, y=0)

lbl2 = tk.Label(master=frame4, text='I am at (75,75)', bg='yellow')
lbl2.place(x=75, y=75)

frm_grid = tk.Frame(master=window, width=150, height=150)
frm_grid.pack(side=tk.LEFT)

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=frm_grid,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=10, pady=10)

window.mainloop()