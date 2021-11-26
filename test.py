

stock_entrys = [
        {'name': "date", 'default': f'2021-11-17'},
        {'name': "trans", 'default': 'BUY/SELL'},
        {'name': "symbol", 'default': 'e.g. "IBM"'},
        {'name': "qty", 'default': '100'},
        {'name': "price", 'default': '42.5'},
        ]
# frm_input = tk.Frame(master=self.window, height=150, width=150, borderwidth=20)
for entry in stock_entrys:
    print(entry)