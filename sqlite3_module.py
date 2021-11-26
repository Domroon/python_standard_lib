import sqlite3
from pathlib import Path
import sys
import tkinter as tk
from datetime import datetime as DateTime

PATH = Path()
CURRENT = PATH.cwd()
DATABASES = CURRENT / 'databases'


def create_stocks_table(con, cur, command):
    # Create table
    cur.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')

    # Save (commit) the changes
    con.commit()


def insert_user_data(con, cur):
    date = input('date (iso-format): ')
    trans = input('BUY/SELL: ')
    symbol = input('symbol (e.g. "IBM": ')
    qty = input('qty (e.g. "100"): ')
    price = input('price (float): ')

    cur.execute("INSERT INTO stocks VALUES (CURRENT_TIMESTAMP ,?, ?, ?, ?)", (trans, symbol, int(qty), float(price)))


def show_data(cur, order='price'):
    for row in cur.execute(f'SELECT * FROM stocks ORDER BY {order}'):
        print(row)


def connect():
    con = sqlite3.connect(DATABASES / 'example.db')
    cur = con.cursor()

    return con, cur


def show_cli_menu(con, cur):
    while True:
        user_input = input('\n1 - ADD new share\n2 - SHOW stock (order by price)\n3 - SHOW stock (order by date)\n4 - DELETE share\n5 - QUIT\n')
        if user_input == '1':
            insert_user_data(con, cur)
        elif user_input == '2':
            show_data(cur)
        elif user_input == '3':
            show_data(cur, 'date')
        elif user_input == '4':
            user_input = input('date (iso-format): ')
            cur.execute("DELETE FROM stocks WHERE date=:user_input", {"user_input": user_input})
        elif user_input == '5':
            while True:
                if con.in_transaction:
                    commit = input('Do you want to commit your changes? y/n: ')
                    if commit == 'y':
                        con.commit()
                        break
                    elif commit == 'n':
                        break
                    else:
                        print('Please enter valid input')
                else:
                    break
            con.close()
            sys.exit()    
        else:
            print('Please enter valid input.')

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.now = DateTime.now()
        self.row = 0
        self.column = 0
        self.input_frame, self.input_entrys = self._init_input_frame()
        self.add_widgets()

    def _init_input_frame(self):
        tk_entrys = []
        stock_entrys = [
                        {'name': "date", 'default': f'{self.now.date()}'},
                        {'name': "trans", 'default': 'BUY/SELL'},
                        {'name': "symbol", 'default': 'e.g. "IBM"'},
                        {'name': "qty", 'default': '100'},
                        {'name': "price", 'default': '42.5'},
                        ]
        frm_input = tk.Frame(master=self.window, height=150, width=150, borderwidth=20)
        lbl_input = tk.Label(master=frm_input, text='Add new share')
        lbl_input.grid(row=self.row, column=self.column)
        self.row += 1
        for entry in stock_entrys:
            self.column = 0
            label = tk.Label(master=frm_input, text=f'{entry["name"]}')
            label.grid(row=self.row, column=self.column)
            self.column += 1
            tk_entry = tk.Entry(master=frm_input)
            tk_entry.insert(0, entry['default'])
            tk_entry.grid(row=self.row, column=self.column)
            self.row += 1
            tk_entrys.append(tk_entry)
        btn_submit = tk.Button(master=frm_input, text='submit', command=self.submit_input)
        btn_submit.grid(row=self.row + 1, column=0)

        return frm_input, tk_entrys

    def submit_input(self):
        for entry in self.input_entrys:
            entry.delete(0, tk.END)

    def add_widgets(self):
        self.input_frame.pack(side=tk.LEFT)

    def show(self):
        self.window.mainloop()


def main():
    con, cur = connect()
    user_input = input('1 - CLI Interface\n2 - GUI Interface\n')

    if user_input == '1':
        show_cli_menu(con, cur)
    elif user_input == '2':
        gui = GUI()
        gui.show()
    else:
        print('Enter valid input')


if __name__ == '__main__':
    main()