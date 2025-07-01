import tkinter as tk

def button_click(value):
    current = input_display.get()
    input_display.delete(0, tk.END)
    input_display.insert(0, current + value)                                 
def clear_display():
    input_display.delete(0, tk.END)
    result_display.delete(0, tk.END)

def backspace():
    current = input_display.get()
    input_display.delete(0, tk.END)
    input_display.insert(0, current[:-1])

def calculate():
    try:
        result = eval(input_display.get())
        result_display.delete(0, tk.END)
        result_display.insert(0, str(result))    
    except:
        result_display.delete(0, tk.END)
        result_display.insert(0, "Error")

window = tk.Tk()
window.title("옥계")
window.configure(bg='white')
window.geometry("360x520")
window.resizable(False, False)

input_display = tk.Entry(window, font=('Arial', 20), bg='yellow', fg='black', bd=3, relief='solid', justify='right')
input_display.grid(row=0, column=0, columnspan=5, padx=15, pady=(20, 5), ipadx=10, ipady=10, sticky="nsew")

result_display = tk.Entry(window, font=('Arial', 20), bg='lightgreen', fg='black', bd=3, relief='solid', justify='right')
result_display.grid(row=1, column=0, columnspan=5, padx=15, pady=(5, 15), ipadx=10, ipady=10, sticky="nsew")

buttons = [
    ['7', '8', '9', '*', '/'],
    ['4', '5', '6', '+', '-'],
    ['1', '2', '3', '(', ')'],
    ['0', '.', '=', 'C', 'bs']
]

def create_button(text, command, row, column):
    btn = tk.Button(
        window,
        text=text,
        command=command,
        font=('Arial', 16),
        bg='white',
        fg='black',
        relief='ridge',
        bd=1,
        activebackground='#f0f0f0',
        activeforeground='black',
        padx=10,
        pady=10
    )
    btn.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")

for r, row in enumerate(buttons, start=2):
    for c, char in enumerate(row):
        if char == '=':
            cmd = calculate
        elif char == 'C':
            cmd = clear_display
        elif char == 'bs':
            cmd = backspace
        else:
            cmd = lambda x=char: button_click(x)
        create_button(char, cmd, r, c)

for i in range(5):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
