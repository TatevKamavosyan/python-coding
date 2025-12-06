import tkinter as tk


def respond():
    txt=entry.get()
    chat.insert(tk.END, "You: " + txt + "\n")


root=tk.Tk()
chat=tk.Text(root,width=50,height=20)    
chat.pack()
entry=tk.Entry(root,width=50)
entry.pack()
tk.Button(root,text="Send",command=respond).pack()
root.mainloop()