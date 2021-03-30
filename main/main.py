import PySimpleGUI as sg 
import random 


error_message = ""
sg.ChangeLookAndFeel('DarkBlue')
layout= [
    [sg.Checkbox('Uppercase Letters?', key='Upper', default=True)],
    [sg.Checkbox('Lowercase Letters?', key='Lower', default=True)],
    [sg.Checkbox('Numbers?', key='Numbers', default=True)],
    [sg.Checkbox('Symbols?', key='Symbols', default=True)],
    [sg.Text('How long should the password be? (positive numbers only)'), sg.InputText(key = 'length')],
    [sg.Text(error_message)],
    [sg.Button('Submit'), sg.Button('Cancel')]
   
]
mainscreen = sg.Window('Password Generator', layout, resizable=True, element_justification='c', location = (0, 0)).Finalize()

mainscreen.Maximize()

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "@#=+_"
upper, lower, nums, syms = True, True, True, True
amount = 1
all = ""



while True:
    
    event, value = mainscreen.Read()
    if event in (None, 'Cancel'):
        break
    if event in (None, 'Submit'):
        
        while True:
            lengthstr = value['length']
            
            try:
                lengthint = int(lengthstr)
                if lengthint < 0:

                    error_message = "Please enter a positive integer between 0 and 68."
                    mainscreen.close()
                    layout= [
                        [sg.Checkbox('Uppercase Letters?', key='Upper', default=True)],
                        [sg.Checkbox('Lowercase Letters?', key='Lower', default=True)],
                        [sg.Checkbox('Numbers?', key='Numbers', default=True)],
                        [sg.Checkbox('Symbols?', key='Symbols', default=True)],
                        [sg.Text('How long should the password be? (positive numbers only)'), sg.InputText(key = 'length')],
                        [sg.Text(error_message)],
                        [sg.Button('Submit'), sg.Button('Cancel')]
                    ]
                    mainscreen = sg.Window('Password Generator', layout, resizable=True, element_justification='c', location = (0, 0)).Finalize()

                    mainscreen.Maximize()
                    event, value = mainscreen.Read()
                if lengthint > 0:
                    uppercase_stuff = value['Upper']
                    lowercase_stuff = value['Lower']
                    numbers_stuff = value['Numbers']
                    symbols_stuff = value['Symbols']
                    length_stuff = value['length']
                    if event in (None, 'Cancel'):
                        break
                    if uppercase_stuff == False:
                        upper = False
                    if lowercase_stuff == False:
                        lower = False
                    if numbers_stuff == False:
                        nums = False
                    if symbols_stuff == False:
                        syms = False
                    if upper == False and lower == False and nums == False and syms == False:
                        upper = True
                    if upper:
                        all += uppercase_letters
                    if lower:
                        all += lowercase_letters
                    if nums:
                        all += digits
                    if syms:
                        all += symbols
                    for x in range(amount):
                        password2 = "".join(random.sample(all, lengthint))
                        print(password2)
                    
                        
                    layout1 = [
                        [sg.Text('Your generated password is: ' + password2, font=("Helvetica", 12) )],
                        [sg.Text("")],


                    ]
                    window1 = sg.Window(password2, layout1, resizable=True, element_justification='c', keep_on_top=True).Finalize()
                    window1.Maximize()

                    while True:
                        if event1 == None:
                           break
                        #mainscreen.Close()
                        event1, value1 = window1.Read()
                        
                        

                
                
            except:
                error_message = "Please enter a positive integer between 0 and 68."
                mainscreen.close()
                layout= [
                    [sg.Checkbox('Uppercase Letters?', key='Upper', default=True)],
                    [sg.Checkbox('Lowercase Letters?', key='Lower', default=True)],
                    [sg.Checkbox('Numbers?', key='Numbers', default=True)],
                    [sg.Checkbox('Symbols?', key='Symbols', default=True)],
                    [sg.Text('How long should the password be? (positive numbers only)'), sg.InputText(key = 'length')],
                    [sg.Text(error_message)],
                    [sg.Button('Submit'), sg.Button('Cancel')]
                
                    ]
                mainscreen = sg.Window('Password Generator', layout, resizable=True, element_justification='c', location = (0, 0)).Finalize()
                mainscreen.Maximize()
                event, value = mainscreen.Read()
