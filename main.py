import PySimpleGUI as sg

from  classes import Gains as rep
from  classes import Jamm as jamm

#Layout for main menu 
layoutMain = [  [sg.Text("Log or read here:")],
                [sg.Button("Add stock"), sg.Button("View inventory"), sg.Button("All")],
                [sg.Button("Done")]]

#Layout for input section
layoutInput = [ [sg.Text("Log your fruit.")],
                [sg.Text("Spiecies: "), sg.InputText()],
                [sg.Text("Amount: "), sg.Slider(range = (1,256), orientation = 'h'), sg.Text("kg")],
                [sg.Text("Is it a fruit or vegetable?: "), sg.Radio("Fruit", group_id="fruit", default=True), sg.Radio("Vegetable", group_id="fruit")],
                [sg.Button("Add"), sg.Button("Back")] ]

#Layout for output section
layoutOutput = [[sg.Listbox(values=[],key="output", size=(40,20)),
                sg.Button("Clear"), sg.Button("Back.")]]

#Combine all the layouts into one, so it can be displayed in one window
layout = [[sg.Column(layoutMain, key="Main"), sg.Column(layoutInput, visible=False, key="Input"), sg.Column(layoutOutput, visible=False, key="Output")]]

Stack=[]

window = sg.Window('Gain reporter', layout)
while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Done': #If the window is closed or the user is done it closes the window
                break

        if event == "Add stock":                        #changes window to show input
                window[f'Input'].update(visible=True)
                window[f'Main'].update(visible=False)

        if event == "View inventory":                   #changes window to show output
                window[f'Output'].update(visible=True)
                window[f'Main'].update(visible=False)

        if event == "All":                   #changes window to show output
                window[f'Input'].update(visible=True)
                window[f'Output'].update(visible=True)
                window[f'Main'].update(visible=False)

        if event == "Clear":
                selected_items = values["output"]
                if selected_items:
                        for item in selected_items:
                                Stack.remove(item)
                window["output"].update(values=Stack)
                
        if event == "Back":                             #changes window to show main menu
                window[f'Input'].update(visible=False)
                window[f'Main'].update(visible=True)
        if event == "Back.":                             #changes window to show main menu
                window[f'Output'].update(visible=False)
                window[f'Main'].update(visible=True)
        
        if event == "Add":                              #Adds the input to the output screen
                item = rep(values[0], values[1], values[2])
                if item:
                        Stack.append(item)
                        stack=[]
                        for i in range(len(Stack)):
                                stack.append(Stack[i].val)
                        window["output"].update(values=stack)

          

window.close()
