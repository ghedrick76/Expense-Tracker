import PySimpleGUI as sg

# Change the color of windows
sg.theme('BluePurple')

# Format window
layout = [  [sg.Text("Enter expense")],
            [sg.Text("Input expense type"), sg.InputText()],
            [sg.Text("Input cost"), sg.InputText()],
            [sg.Text("Input date of expense"), sg.InputText()],
            [sg.Button("OK"), sg.Button("Exit")]  ]
            
# Create window
window = sg.Window("Expense Tracker", layout)

# Event Loop to process events and get the values of inputs
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "OK":
        sg.popup("This expense has been added!", title="Success")
    #print("You entered:", values[0])

window.close()