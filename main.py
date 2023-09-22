import PySimpleGUI as sg

#from  classes.py import Gains as rep
#from  classes.py import Jamm as jamm

#Layout for main menu 
layoutMain = [  [sg.Text("Log or read here:")],
                [sg.Button("Add stock"), sg.Button("View invenory")],
                [sg.Button("Done")]]

#Layout for input section
layoutInput = [ [sg.Text("Log your fruit.")],
                [sg.Text("Spiecies: "), sg.InputText()],
                [sg.Text("Amount: "), sg.Slider(range = (1,256), orientation = 'h'), sg.Text("kg")],
                [sg.Text("Is it a fruit or vegetable?: "), sg.Radio("Fruit", group_id="fruit"), sg.Radio("Vegetable", group_id="fruit")],
                [sg.Button("Add"), sg.Button("Back")] ]

#layout for Output section
layoutOutput = [[sg.Button("Back")]]

layout = [[sg.Column(layoutMain, key="Main"), sg.Column(layoutInput, visible=False, key="Input"), sg.Column(layoutOutput, visible=False, key="Output")]]

window = sg.Window('Gain reporter', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Done': #If the window is closed or the user is done it closes the window
            break

    if event == 'Add stock':
        window[f'Input'].update(visible=True)
        window[f'Main'].update(visible=False)

    if event == 'View inventory':
        window[f'Output'].update(visible=True)
        window[f'Main'].update(visible=False)
         
    if event == 'Back':
        window[f'Input'].update(visible=False)
        window[f'Output'].update(visible=False)
        window[f'Main'].update(visible=True)
          

window.close()
