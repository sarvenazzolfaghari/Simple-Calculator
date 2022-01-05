from tkinter import *


def click(num):
    global operator
    operator = operator + str(num)
    text_input.set(operator)


def clear():
    global operator
    operator = ""
    text_input.set("")


def equal():
    global operator
    result = str(eval(operator))
    text_input.set(result)


win = Tk()
win.title("calculator")
operator = ""
text_input = StringVar()

txt = Entry(win, font=("arial", 25, "bold"), textvariable=text_input, bd=30, insertwidth=4,bg="gray10", fg="snow",
            justify="right").grid(columnspan=4)
btn7 = Button(win, text="7", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(7)).grid(row=1, column=0)
btn8 = Button(win, text="8", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(8)).grid(row=1, column=1)
btn9 = Button(win, text="9", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(9)).grid(row=1, column=2)
multiply = Button(win, text="x", padx=20, pady=15, bd=8, fg="snow", bg="darkOrange1",
                  font=("arial", 25, "bold"), command=lambda: click("*")).grid(row=1, column=3)

btn4 = Button(win, text="4", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(4)).grid(row=2, column=0)
btn5 = Button(win, text="5", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(5)).grid(row=2, column=1)
btn6 = Button(win, text="6", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(6)).grid(row=2, column=2)
minus = Button(win, text="- ", padx=20, pady=15, bd=8, fg="snow", bg="darkOrange1",
               font=("arial", 25, "bold"), command=lambda: click("-")).grid(row=2, column=3)

btn1 = Button(win, text="1", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(1)).grid(row=3, column=0)
btn2 = Button(win, text="2", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(2)).grid(row=3, column=1)
btn3 = Button(win, text="3", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(3)).grid(row=3, column=2)
addition = Button(win, text="+", padx=20, pady=15, bd=8, fg="snow", bg="darkOrange1",
                  font=("arial", 25, "bold"), command=lambda: click("+")).grid(row=3, column=3)

btn0 = Button(win, text="0", padx=20, pady=15, bd=8, fg="snow", bg="gray35",
              font=("arial", 25, "bold"), command=lambda: click(0)).grid(row=4, column=0)
btnClear = Button(win, text=" C ", padx=7.5, pady=15, bd=8, fg="snow", bg="gray60",
                  font=("arial", 25, "bold"), command=clear).grid(row=4, column=1)
equal = Button(win, text="=", padx=20, pady=15, bd=8, fg="snow", bg="gray60",
               font=("arial", 25, "bold"), command=equal).grid(row=4, column=2)
division = Button(win, text="/ ", padx=20, pady=15, bd=8, fg="snow", bg="darkOrange1",
                  font=("arial", 25, "bold"), command=lambda: click("/")).grid(row=4, column=3)


win.mainloop()
