import PySimpleGUI as sg
from  classes.py import Gains as rep

layout = [  [sg.Text("Log your fruit.")],
            [sg.Text("Spiecies: "), sg.InputText()],
            [sg.Text("The age: "), sg.InputText()],
            [sg.Text("The sex: "), sg.InputText()],
            [sg.Button("Confirm"), sg.Button("Cancel")] ]

log = True

# Create the Window
window = sg.Window('Human creator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        log = False
        break

window.close()