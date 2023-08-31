import tkinter as tk
import tkinter.font as tkFont
from typing import Type

# globals
labels = ["Male", "Age", "Education*", "Current Smoker", "Cigs Per Day", "Takes Blood Pressure Meds", "Prevalent Stroke", "Prevalent Hypertensive", "Total Cholesterol", "Systolic Blood Pressure", "Diastolic Blood Pressure", "BMI", "Heart Rate", "Glucose", "TenYearCHD**", "Prediction"]
entries = []
dataWeight = [.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1,.1] # will get the weights from the ML

MinReq = .7 # will probably stay about the same

# simplifies the creation of a frame
def basicFrame(window):
    return tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)

# Predict button's function
def predictClick(lbl):
    PredictionData = []
    ProbabiltyOfData = 0
    for i in range(len(entries)):
       PredictionData.append(entries[i].get())
       print(entries[i].get())
       if PredictionData[i] != "":
            ProbabiltyOfData += dataWeight[i]
    if ProbabiltyOfData > MinReq:
        lbl.config(text="No ML Yet!!")
        return PredictionData # will instead call for a prediction using the prediction data
    else:
        lbl.config(text="Not enough data!")
        return

# exit button's code
def exitClick():
    quit()

def genWindow():
    # Creates new window
    window = tk.Tk()
    fontObj = tkFont.Font(size=12)
    predictionLabel = tk.Label()
    # Sets column and row settings
    for i in range(9):
        window.columnconfigure(i, weight=1, minsize=75)
    for i in range(7):
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
            if(i == 0 or i == 3 or i == 5 or i == 6 or i == 7):
                Variable1 = tk.IntVar()
                ent = tk.Checkbutton(master=entFrame, variable=Variable1)    
                entries.append(Variable1)
                ent.pack()
            else:
                ent = tk.Entry(master=entFrame, font=fontObj)    
                entries.append(ent)
                ent.pack()
        else:
            predictionLabel = tk.Label(master=entFrame, text="No Prediction Yet", font=fontObj)
            predictionLabel.pack()
        lbl.pack()
        
    # Creates the title label
    frame1 = basicFrame(window)
    frame1.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
    newLabel = tk.Label(master=frame1, text="Dx Assistant", font=fontObj)
    newLabel.pack()
    
    addendumFrame = basicFrame(window)
    addendumFrame.grid(row=5, column=0, columnspan=8, padx=5, pady=5)
    addendumLabel = tk.Label(master=addendumFrame, text="*Some high school (1), high school/GED (2), some college/vocational school (3), college (4)\n**The 10 year risk of coronary heart disease(CHD).")
    addendumLabel.pack()

    # Creates the exit button
    frame2 = basicFrame(window)
    frame2.grid(row=6, column=8, padx=5, pady=5)
    exitButton = tk.Button(master=frame2, text="EXIT", font=fontObj, command=exitClick)
    exitButton.pack()
    
    # Creates the "predict" button
    frame3 = basicFrame(window)
    frame3.grid(row=6, column=3,columnspan=2, padx=5, pady=5)
    predictButton = tk.Button(master=frame3, text="PREDICT", font=fontObj, command=lambda: predictClick(predictionLabel))
    predictButton.pack()

    window.mainloop()
    


genWindow()