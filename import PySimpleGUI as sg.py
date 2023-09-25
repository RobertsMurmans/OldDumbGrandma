import PySimpleGUI as sg

layout = [
    [sg.Text("List of Items:")],
    [sg.Listbox(values=[], size=(40, 10), key="-LISTBOX-")],
    [sg.InputText(key="-ITEM-"), sg.Button("Add"), sg.Button("Remove")],
    [sg.Button("Clear"), sg.Button("Exit")]
]

window = sg.Window("PySimpleGUI List Example", layout)

item_list = []

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Add":
        item = values["-ITEM-"]
        if item:
            item_list.append(item)
            window["-LISTBOX-"].update(values=item_list)
            window["-ITEM-"].update("")  # Clear the input field
    elif event == "Remove":
        selected_items = values["-LISTBOX-"]
        if selected_items:
            for item in selected_items:
                item_list.remove(item)
            window["-LISTBOX-"].update(values=item_list)
    elif event == "Clear":
        item_list.clear()
        window["-LISTBOX-"].update(values=item_list)

window.close()
