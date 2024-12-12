from guizero import App, Text, PushButton, CheckBox
import requests
import json

a = [False]

def citatore():
    if a[0] == True:
        a[0] = False    
    else:
        a[0] = True
        
def change_message():
    x = requests.get('https://api.breakingbadquotes.xyz/v1/quotes')
    if x.status_code !=200:
        pass
    else:
        quote = json.loads(x.text)
        if a[0] == True:
            message.value = (quote[0]['quote'] + " - " + quote[0]['author'])
        else:
            message.value = (quote[0]['quote'])
            
app = App(title = 'Generatore di citazioni di Breaking Bad', width = 1600, height = 400)

testo = Text(app, text = 'Generatore di citazioni di Breaking Bad')

checkbox = CheckBox(app, text = "mostra di chi è la citazione", command = citatore)

message = Text(app, text = 'Premi il pulsante!')

button = PushButton(app, text = "Press me", image = "waltuh.png", width = 200, height = 200, command = change_message)

app.display()