from tkinter import *

def execute():
    try:
        if output.get().endswith("+") or output.get().endswith("-") or output.get().endswith("*") or output.get().endswith("/"):
            output.delete(len(output.get()) - 1)
        elif len(output.get()) > 0:
            result = eval(output.get())
            output.delete(0, END)
            output.insert(0, result)
    except:
        output.delete(0, END)
        output.insert(0, "Error")

def input(angka):
    operator = ["+", "-", "*", "/"]
    if (output.get().endswith("/") and angka in operator) or (output.get().endswith("*") and angka in operator )or (output.get().endswith("-") and angka in operator ) or (output.get().endswith("+") and angka in operator ):
        output.delete(len(output.get()) - 1)
        output.insert(END, angka)
    else:
        output.insert(END, angka)
        
        
root = Tk()
root.title("Kalkulator by Rafly")
koorx = (root.winfo_screenwidth() // 2) - (300 // 2) - 50
koory = (root.winfo_screenheight() // 2) - (400 // 2) - 50
root.geometry(f"400x400+{koorx}+{koory}")
root.resizable(False, False)
root.config(bg="#000000")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
output = Entry(border=2, font=("Arial, 16"), justify=RIGHT)
output.grid(sticky="news", row=0, column=0, columnspan=5, ipadx=10, ipady=15)

button1 = Button(text="1", border=2, font=("Arial, 12"), command=lambda: input("1"))
button1.grid(sticky="news", row=1, column=0)
button2 = Button(text="2", border=2, font=("Arial, 12"), command=lambda: input("2"))
button2.grid(sticky="news", row=1, column=1)
button3 = Button(text="3", border=2, font=("Arial, 12"), command=lambda: input("3"))
button3.grid(sticky="news", row=1, column=2)
button4 = Button(text="4", border=2, font=("Arial, 12"), command=lambda: input("4"))
button4.grid(sticky="news", row=2, column=0)
button5 = Button(text="5", border=2, font=("Arial, 12"), command=lambda: input("5"))
button5.grid(sticky="news", row=2, column=1)
button6 = Button(text="6", border=2, font=("Arial, 12"), command=lambda: input("6"))
button6.grid(sticky="news", row=2, column=2)
button7 = Button(text="7", border=2, font=("Arial, 12"), command=lambda: input("7"))
button7.grid(sticky="news", row=3, column=0)
button8 = Button(text="8", border=2, font=("Arial, 12"), command=lambda: input("8"))
button8.grid(sticky="news", row=3, column=1)
button9 = Button(text="9", border=2, font=("Arial, 12"), command=lambda: input("9"))
button9.grid(sticky="news", row=3, column=2)
buttonc = Button(text="Del", border=2, font=("Arial, 12"), command=lambda: output.delete(len(output.get()) - 1))
buttonc.grid(sticky="news", row=4, column=0)
button0 = Button(text="0", border=2, font=("Arial, 12"), command=lambda: input("0"))
button0.grid(sticky="news", row=4, column=1)
button0 = Button(text="C", border=2, font=("Arial, 12"), command=lambda: output.delete(0, END))
button0.grid(sticky="news", row=4, column=2)

buttonplus = Button(text="+", border=2, font=("Arial, 12"), command=lambda: input("+"))
buttonplus.grid(sticky="news", row=1, column=3)
buttonminus = Button(text="-", border=2, font=("Arial, 12"), command=lambda: input("-"))
buttonminus.grid(sticky="news", row=2, column=3)
buttonmul = Button(text="*", border=2, font=("Arial, 12"), command=lambda: input("*"))
buttonmul.grid(sticky="news", row=3, column=3)
buttondiv = Button(text="/", border=2, font=("Arial, 12"), command=lambda: input("/"))
buttondiv.grid(sticky="news", row=4, column=3)

buttonex = Button(text="=", border=2, font=("Arial, 12"), command=lambda: execute())
buttonex.grid(sticky="news", row=1, rowspan=5, column=4)



root.mainloop()