import tkinter as tk
import requests
from threading import Thread

api = "https://api.quotable.io/random"
qoutes = []
qoute_number = 0

window = tk.Tk()
window.geometry ("900x260")
window.title("LIFE QOUTES")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="gray")

def preload_qoutes():
    global qoutes
    
    print("*** Loading more qoutes***")
    for x in range(10):
        random_qoute = requests.get(api).json()
        content = random_qoute["content"]
        author = random_qoute["author"]
        qoute = content + "\n\n" + "BY" + author
        print(content)
        
        qoutes.append(qoute)
    print("***Finish loading more qoutes***")

preload_qoutes()

def get_random_qoute():
    global qoute_lable
    global qoutes 
    global qoute_number
    qoute_lable.configure(text=qoutes[qoute_number])
    qoute_number = qoute_number+1
    
    print(qoute_number)


if qoutes [qoute_number] == qoutes[-3]:
    Thread = Thread(target=preload_qoutes)
    
    Thread.start()

#UI
qoute_lable = tk.Label(window, text= "click on the button to generate random number!",
                       height=6, pady= 20, wraplength=800, 
                       font=("Helvetica",14))
qoute_lable.grid(row=0, column=0, sticky="WE", padx=30, pady=10)
button = tk.Button(text="generate",command= get_random_qoute, bg='#e86666', fg='#ffffff',
                   activebackground="green",  font=("Helvetica",14))
button.grid(row=1, column=0, sticky="WE", padx=400, pady=10)

if __name__ == "__main__" :
    window.mainloop()
