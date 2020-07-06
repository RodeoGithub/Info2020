from tkinter import *


#region Config main window

calc = Tk()
calc.title("Calculator")
calc.geometry("415x200")
calc.iconbitmap(".\Calculadora_Tk\Calculator.ico")

#endregion

#region Calculator logic
result = StringVar()
result.set('')
def sum():
    result.set(str(int(firstNum.get()) + int(secondNum.get())))
    calc.update()
def substraction():
    result.set(str(int(firstNum.get()) - int(secondNum.get())))
    calc.update()
def product():
    result.set(str(int(firstNum.get()) * int(secondNum.get())))
    calc.update()
def division():
    fn=int(firstNum.get())
    sn=int(secondNum.get())
    if(sn==0):
        result.set("Impossible!")
    else:
        r=round(fn/sn,2)
        result.set(str(r))
    calc.update()


#endregion

#region User Interface


firstLabel = Label(calc, 
                text = "Enter first number: ",
                font=18,
                justify="left",
                pady=10,
                bg="grey"
                )
firstLabel.grid(sticky="w",row=0,column=0,
                )
secondLabel = Label(calc, 
                text = "Enter second number: ", 
                font=18,
                justify=LEFT,
                pady=10,
                bg="grey"
                )
secondLabel.grid(sticky="w",row=1,column=0,
                )
resultLabel = Label(calc,
                    text="Result: ",
                    font=18,
                    justify=LEFT,
                    pady=10,
                    bg="grey",
                    )
resultLabel.grid(row=2, column=0)

firstNum = Entry(calc,borderwidth=3,width=15,font=16,)
firstNum.focus()
firstNum.grid(row=0,column=1,)

secondNum = Entry(calc,borderwidth=3,width=15,font=16,)
secondNum.grid(row=1,column=1,)

plusButton = Button(calc, 
                    text = "+",
                    padx=10,
                    pady=5,
                    font=15,
                    command=sum)
plusButton.grid(row=0,column=2, padx=10,pady=10)

multiplicationButton=Button(calc,
                            text="x",
                            padx=10,
                            pady=5,
                            font=12,
                            command=product)
multiplicationButton.grid(row=0,column=3)

minusButton = Button(calc,
                    text="-",
                    padx=10,
                    pady=5,
                    font=15,
                    command=substraction)
minusButton.grid(row=1,column=2)

divisionButton = Button(calc, 
                        text="/",
                        padx=10,
                        pady=5,
                        font=15,
                        command=division)
divisionButton.grid(row=1,column=3)

resultOfOperation = Label(calc,bg="white",borderwidth=3,
                    relief="sunken",textvariable=result,
                    width=15,font=16)
resultOfOperation.grid(row=2,column=1)
#endregion

calc.configure(bg="grey")
calc.mainloop()