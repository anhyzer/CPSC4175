import tkinter as tk
import tkinter.font as tkFont

# globals
labels = ["gender", "age", "education", "currentSmoker", "cigsPerDay", "BPMeds", "prevalentStroke", "prevalentHyp", "totChol", "sysBP", "diaBP", "BMI", "heartRate", "glucose", "TenYearCHD", "Prediction"]
entries = []          

# simplifies the creation of a frame
def basicFrame(window):
    return tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)

# Predict button's function
def predictClick(lbl):
    lbl.config(text="No ML Yet!!")

# exit button's code
def exitClick():
    quit()

def genWindow():
    # Creates new window
    window = tk.Tk()
    fontObj = tkFont.Font(size=16)
    predictionLabel = tk.Label()
    # Sets column and row settings
    for i in range(9):
        window.columnconfigure(i, weight=1, minsize=75)
    for i in range(6):
        window.rowconfigure(i, weight=1, minsize=60)
    # Creates the labels and entries for the data
    for i in range(len(labels)):
        lblFrame = basicFrame(window)
        if(i % 2 == 0):
            lblFrame.grid(row=1, column=i//2, padx=2, pady=5)
        else:
            lblFrame.grid(row=3, column=i//2, padx=2, pady=5)
        entFrame = basicFrame(window)
        if(i%2 ==0):
            entFrame.grid(row=2, column=i//2, padx=2, pady=5)
        else:
            entFrame.grid(row=4, column=i//2, padx=2, pady=5)
        lbl = tk.Label(master=lblFrame, text=labels[i], font=fontObj)
        if(i < len(labels)-1):
            ent = tk.Entry(master=entFrame, font=fontObj)
            ent.pack()
            entries.append(ent)
        else:
            predictionLabel = tk.Label(master=entFrame, text="No Prediction Yet", font=fontObj)
            predictionLabel.pack()
        lbl.pack()
        
    # Creates the title label
    frame1 = basicFrame(window)
    frame1.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
    newLabel = tk.Label(master=frame1, text="Dx Assistant", font=fontObj)
    newLabel.pack()
    
    # Creates the exit button
    frame2 = basicFrame(window)
    frame2.grid(row=5, column=8, padx=5, pady=5)
    exitButton = tk.Button(master=frame2, text="EXIT", font=fontObj, command=exitClick)
    exitButton.pack()
    
    # Creates the "predict" button
    frame3 = basicFrame(window)
    frame3.grid(row=5, column=3,columnspan=2, padx=5, pady=5)
    predictButton = tk.Button(master=frame3, text="PREDICT", font=fontObj, command=lambda: predictClick(predictionLabel))
    predictButton.pack()

    window.mainloop()
    


genWindow()