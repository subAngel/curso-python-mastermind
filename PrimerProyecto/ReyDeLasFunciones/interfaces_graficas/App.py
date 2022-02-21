import PySimpleGUI as sg

button_size = (7, 3)

layout = [[sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("He terminado")]]

window = sg.Window("Demo", layout)
value = window.read()
print(value)