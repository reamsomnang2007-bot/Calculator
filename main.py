import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light")

app = ctk.CTk()
app.title("Calculator")
app.geometry("300x420")
app.resizable(False, False)

expr = ""
display = ctk.CTkEntry(app, font = ("Arial", 20), justify = "right", height = 60)
display.pack(fill = "x", padx = 10, pady = 10)

def press(key):
    global expr
    if key == "C":
        expr = ""
    elif key == "⌫":  # FIX 3: backspace now works
        expr = "" if expr == "Error" else expr[:-1]
    elif key == "=":
        try:
            expr = str(eval(expr))
        except Exception:
            expr = "Error"
    else:
        if expr == "Error":
            expr = ""
        expr += key
    display.delete(0, "end")
    display.insert(0, expr)

frame = ctk.CTkFrame(app, fg_color = "transparent")
frame.pack(expand = True, fill = "both", padx = 10, pady = (0, 10))

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "⌫"]
]

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight = 1)
    for c, key in enumerate(row):
        frame.columnconfigure(c, weight = 1)
        if not key:
            continue
        if key == "C":
            color, hover = "#e74c3c", "#c0392b"  # clear
        elif key == "=":
            color, hover = "#2ecc71", "#27ae60"  # equal
        elif key in "+-*/":
            color, hover = "#f39c12", "#d68910"  # operators
        else:
            color, hover = "#3a3a3a", "#4a4a4a"  # numbers

        ctk.CTkButton(frame, text = key, fg_color = color, hover_color = hover, command = lambda k=key: press(k)).grid(row = r, column = c, padx = 3, pady = 3, sticky = "nsew")

app.mainloop()