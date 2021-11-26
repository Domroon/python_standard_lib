import tkinter as tk


def show_hello():
        print("The Button was pressed!")


def show_entry():
    if entry.get():
        print(entry.get())
        entry.delete(0, tk.END)
    else:
        print("Entry is empty!")


def insert_text():
    entry.insert(0, "Python")


def insert_to_textbox():
    txt_box.insert(tk.END, f'\n{entry.get()}')
    entry.delete(0, tk.END)


def show_textbox():
    txt_value = txt_box.get('1.0', tk.END)
    print(txt_value)


def del_text():
    txt_box.delete('1.0', tk.END)


window = tk.Tk()

# Widgets
first_label = tk.Label(text="first label :)")
greeting = tk.Label(text="Hello, Tkinter", background="#34A2FE")
rocks = tk.Label(text="Python rocks!", fg="white", bg="orange")
hello_world = tk.Label(
    text="Hello world!",
    fg='white',
    bg='purple',
    width='10',
    height='10')
button = tk.Button(text='Click me!', command=show_hello)
entry = tk.Entry(fg='yellow', bg='blue', width=50)
entry_btn = tk.Button(text='Show entry', command=show_entry)
btn_insert = tk.Button(text='insert "Python"', command=insert_text)
btn_txt_insert = tk.Button(text='insert to textbox', command=insert_to_textbox)
btn_txt_get = tk.Button(text='show textbox value', command=show_textbox)
btn_del_txt = tk.Button(text='delete textbox value', command=del_text)
txt_box = tk.Text()

# Make frames to organize a group of widgets
frame_a = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
frame_b = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=10)

label_a = tk.Label(master=frame_a, text='I am in Frame A')
label_a.pack()

label_b = tk.Label(master=frame_b, text='I am in Frame B')
label_b.pack()

frame_b.pack()
frame_a.pack()

# Put Widgets on window
first_label.pack()
greeting.pack()
rocks.pack()
hello_world.pack()
button.pack()
entry.pack()
entry_btn.pack()
btn_insert.pack()
btn_txt_insert.pack()
txt_box.pack()
btn_txt_get.pack()
btn_del_txt.pack()


window.mainloop()
