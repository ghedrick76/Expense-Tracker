import PySimpleGUI as sg

# Change the color of windows
sg.theme('BluePurple')

# Create layout for the main window
layout = [  [sg.Text("What would you like to do?")],
            [sg.Button("Input Expense")],
            [sg.Button("Input Income")],
            [sg.Button("Analyze")],
            [sg.Button("Exit")]  ]

# Resize window layout
layout = [[sg.Sizer(0,250), sg.Column([[sg.Sizer(250,0)]] + layout, element_justification='c', pad=(0,0))]]

# Create windows
window_1 = sg.Window("Expense Tracker", layout)

win2_active = False

win3_active = False

win4_active = False

# Event Loop to process events and get the values of inputs
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
        layout_expense = [  [sg.Text("Window 2"),
                            [sg.Button("Exit")]]]
        
        win2 = sg.Window("Input Expense", layout_expense)
        while True:
            ev2, val2 = win2.read()
            if ev2 is None or ev2 == "Exit":
                win2_active = False
                win2.Close()
                window_1.UnHide()
                break

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