import datetime as dt
import PySimpleGUI as sg

def what_age(input_text):
    born_date = dt.datetime.strptime(input_text, '%d-%m-%Y')
    now = dt.datetime.now()
    birthday = dt.datetime.strptime(f'{born_date.day}-{born_date.month}-{now.year}', '%d-%m-%Y')
    if now >= birthday:
        return now.year - born_date.year
    else:
        return now.year - born_date.year - 1

def what_stag(age):
    if int(age) < 25:
        return 'I'
    elif 25 <= int(age) < 30:
        return 'II'
    elif 30 <= int(age) < 35:
        return 'III'
    elif 35 <= int(age) < 40:
        return 'IV'
    return 'V'

layout = [
    [sg.Text('Дата рождения дд-мм-гггг: ', font=(12))],
    [sg.Input('', size=(29, 1), key='input')],
    [sg.Button('Age'), sg.Button('Stag'), sg.Button('Clear')],
    [sg.Text('', size=(15, 1), font=('Helvetica', 18),text_color='red', key='out')],
          ]

window = sg.Window('Keypad', layout,
                   default_button_element_size=(5, 2),
                   auto_size_buttons=False,
                   grab_anywhere=False)

while True:
    event, values = window.read()  
    if event == sg.WIN_CLOSED: 
        break
    if event == 'Clear':  
        window['input'].update('')
        window['out'].update('')
    elif event == 'Age':
        window['out'].update(what_age(values['input']))
    elif event == 'Stag':
        res = '{}  {}'.format(what_age(values['input']), what_stag(what_age(values['input'])))
        window['out'].update(res)

window.close()
