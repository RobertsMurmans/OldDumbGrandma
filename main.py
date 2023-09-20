from tkinter import HORIZONTAL
import PySimpleGUI as sg

#from  classes.py import Gains as rep
#from  classes.py import Jamm as jam

#Layout for main menu 
layoutMain = [  sg.Text("Log or read here:"),
                sg.Button("")]

#Layout for input section
layoutInput = [  [sg.Text("Log your fruit.")],
            [sg.Text("Spiecies: "), sg.InputText()],
            [sg.Text("Amount: "), sg.Slider(range = (1,256), orientation = 'h'), sg.Text("kg")],
            [sg.Text("Is it a fruit or vegetable?: "), sg.Radio("Fruit", group_id="fruit"), sg.Radio("Vegetable", group_id="fruit")],
            [sg.Button("Add"), sg.Button("Done")] ]

#layout for Output section
layoutOutput = []

window = sg.Window('Gain reporter', layoutMain)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Done': #If the window is closed or the user is done it closes the window
        break

window.close()
