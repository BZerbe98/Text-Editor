import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)

    window.title(f"Open File: {filepath}")

def wrap_text(text_edit):
    pass


#Used to help with scrollbar, might not be needed now
#def scroll_text_view(*args):
    #text_edit.yview(*args)
    

def main():
    window = tk.Tk()
    window.title("Bryce's Epic Text Editor")

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1) #window.grid_rowconfigure((1,1), weight=1, uniform=1)
 
    #ADD DARK MODE OPTION

    #Frame
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    frame.grid(row=0, column=0, sticky="w")

    #Text box
    text_edit = tk.Text(window, font="Helvetica 14")
    text_edit.grid(row=1, column=0, sticky="nsew")

    #Scrollbar
    scroll = tk.Scrollbar(window, command=text_edit.yview)
    scroll.grid(row=1, column=1, sticky="ns")
    text_edit.config(yscrollcommand=scroll.set)

    #Save button
    save_btn = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    save_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")  

    #open button
    open_btn = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    open_btn.grid(row=0, column=2, padx=5, sticky="ew")

    #wrap button
    #wrap_btn = tk.Button(frame, text="Wrap Text", command=lambda: wrap_text(text_edit))
    #wrap_btn.grid(row=0, column=5, padx=5, sticky="ew")


    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()