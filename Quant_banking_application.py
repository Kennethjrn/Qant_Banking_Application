import tkinter as tk
from tkinter import messagebox

#balance 
balance = 0
def create_account():
    global name, account_no, balance
    name = name_entry.get()
    account_no = account_entry.get()
    balance = float(deposit_entry.get())
    info.config(text=f"Account: {account_no}\nName: {name}\nBalance: ₦{balance:,.2f}")
def deposit():
    global balance
    balance += float(amount_entry.get())
    info.config(text=f"Account: {account_no}\nName: {name}\nBalance: ₦{balance:,.2f}")
def withdraw():
    global balance
    amount = float(amount_entry.get())
    if amount <= balance:
        balance -= amount
        info.config(text=f"Account: {account_no}\nName: {name}\nBalance: ₦{balance:,.2f}")
    else:
        messagebox.showerror("Error ", "Insufficient funds, please enter a valid amount")
def check_balance():
    messagebox.showinfo("Account Balance", f"₦{balance:,.2f}")
def exit_app():
    window.destroy()
window = tk.Tk()
window.title("QUANT Banking Application")
window.geometry("500x500")
tk.Label(window, text="QUANT Banking" ,
         font=("Arial", 20, "bold")).pack(pady=15)
tk.Label(window, text="Customer Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()
tk.Label(window, text="Account Number").pack()
account_entry = tk.Entry(window)
account_entry.pack()
tk.Label(window, text="Initial Deposit").pack()
deposit_entry = tk.Entry(window)
deposit_entry.pack()
tk.Button(window, text="Create Account",
          command=create_account).pack(pady=10)
info = tk.Label(window, text="No account created",
                font=("Arial", 11))
info.pack(pady=10)
tk.Label(window, text="Transaction Amount").pack()
amount_entry = tk.Entry(window)
amount_entry.pack()
tk.Button(window, text="Deposit",
          command=deposit, width=15).pack(pady=5)
tk.Button(window, text="Withdraw",
          command=withdraw, width=15).pack(pady=5)
tk.Button(window, text="Check Balance",
          command=check_balance, width=15).pack(pady=5)
tk.Button(window, text="Exit",
          command=exit_app, width=15).pack(pady=5)
window.mainloop()