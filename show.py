import webbrowser
import os
import time

def show_pics(html, nombre):
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('Las información de pokédex se mostrará en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(2)
    os.remove(f'{nombre}.html')
    