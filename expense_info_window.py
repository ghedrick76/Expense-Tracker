import PySimpleGUI as sg
import functions

def get_expense_info():
    expense_info = functions.retrieve_expense()
    return expense_info


def create():
    expense_info_array = get_expense_info()
    headings = ['Expense', 'Cost', 'Date']

    expense_info_layout = [
        [sg.Table(values=expense_info_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')]
    ]

    expense_info_window = sg.Window("Contact Information Window", 
    expense_info_layout, modal=True)

    while True:
        event, values = expense_info_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    expense_info_window.close()