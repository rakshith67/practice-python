import tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-0")
mainWindow["padx"] = 8

label = tkinter.Label(mainWindow, text="Grid demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox()
fileList.grid(row=1, column=0, sticky="nsew", rowspan=2)
fileList.config(border=2, relief="sunken")

for zone in os.listdir("/Windows/System32"):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
fileList["yscrollcommand"] = listScroll.set

optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(3)

radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Widget to display the result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# Time spinners
hoursSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minutesSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondsSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hoursSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minutesSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondsSpinner.grid(row=0, column=4)
timeFrame["padx"] = 36

# Frame for Date spinners
dateFrame = tkinter.LabelFrame(mainWindow, text="Time")
dateFrame.grid(row=4, column=0, sticky='new')

dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date spinners
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=0, to=59)
monthSpinner = tkinter.Spinbox(dateFrame, width=2, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpinner = tkinter.Spinbox(dateFrame, width=2, from_=2000, to=2099)
daySpinner.grid(row=1, column=0)
monthSpinner.grid(row=1, column=1)
yearSpinner.grid(row=1, column=2)

okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
print(rbValue.get())
