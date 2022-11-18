# Import libraries
import PySimpleGUI as sg
import pysimplesql as ss


# --------------------------------
# Create the database to work with
# --------------------------------

sql="""
CREATE TABLE Fixed Expenses("""




# Change the color of windows
sg.theme('BluePurple')

# Create layout for the main window
layout = [  [sg.Text("Choose what you would like to do!")],
            [],
            [sg.Button("Input Expense")],
            [sg.Button("Input Income")],
            [sg.Button("Analyze")],
            [sg.Button("Exit")]  ]

# Resize window layout
layout = [[sg.Sizer(0,200), sg.Column([[sg.Sizer(200,0)]] + layout, element_justification='c', pad=(0,0))]]

# Create each window
window_1 = sg.Window("Budgeting Application", layout)

win2_active = False

win3_active = False

win4_active = False

# Create the event loop to process events and values
# Main Window
while True:
    event, values = window_1.read()
    print(event, values)
    if event is None or event == "Exit":
        break

    # Expense window
    if not win2_active and event == "Input Expense":
        window_1.Hide()
        win2_active = True

        # Create layout for Expense window
        layout_expense = [  [sg.Push(), sg.Text("Enter expenses"), sg.Push()],
                            [sg.Push(), sg.Text("Input expense type"), sg.InputText()],
                            [sg.Push(), sg.Text("Input cost"), sg.InputText()],
                            [sg.Push(), sg.Text("Input date of expense"), sg.InputText()],
                            [sg.Button("Enter")], [sg.Button("Back")]  ]
        
        win2 = sg.Window("Input Expense", layout_expense)
        while True:
            ev2, val2 = win2.read()
            if ev2 is None or ev2 == "Back":
                win2_active = False
                win2.Close()
                window_1.UnHide()
                break
            if ev2 == "Enter":
                sg.Popup("Expense entered!", no_titlebar=True)

    # Income window
    if not win3_active and event == "Input Income":
        window_1.Hide()
        win3_active = True

        # Create layout for Expense window
        layout_income = [  [sg.Text("Window 3"),
                            [sg.Button("Exit")]]]
        
        win3 = sg.Window("Input Income", layout_income)
        while True:
            ev3, val3, = win3.read()
            if ev3 is None or ev3 == "Exit":
                win3_active = False
                win3.Close()
                window_1.UnHide()
                break

    # AnalyzE window
    if not win4_active and event == "Analyze":
        window_1.Hide()
        win4_active = True

        # Create layout for Expense window
        layout_analyze = [  [sg.Text("Window 4"),
                            [sg.Button("Exit")]]]
        
        win4 = sg.Window("Analyze Finances", layout_analyze)
        while True:
            ev4, val4, = win4.read()
            if ev4 is None or ev4 == "Exit":
                win4_active = False
                win4.Close()
                window_1.UnHide()
                break

window_1.close()