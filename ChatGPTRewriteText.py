''' Documentación biblioteca
pip install --upgrade openai
pip install pyperclip
https://pyperclip.readthedocs.io/en/latest/
Si da "Not implemented Error"
sudo apt-get install curl #to install curl
sudo apt-get install xsel #to install the xsel utility.
sudo apt-get install xclip #to install the xclip utility.
pip install gtk #to install the gtk Python module.
pip install PyQt4 #to install the PyQt4 Python module
'''


# Configura tu clave de API de OpenAI
import time
import pyperclip as pc
import openai
# Aqui ti API de OpenAI
openai.api_key = 'XXXXXXXXXX'


while True:
    tmp_value = pc.waitForNewPaste()
    time.sleep(0.1)

    # Obtén datos del portapapeles
    datos = pc.paste().strip()
    print(datos)
    # Hacemos la peticion de re-escritura
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Actua como un profesor experto en informatica. Intenta ser claro y utilizar un vocabulario apropiado para estudiantes de ciclos formativos de informática"
            },
            {
                "role": "user",
                "content": " Re-escribe el siguiente texto con un estilo adecuado para alumnado de ciclos formativos, como si fuera para un libro de texto: " + datos
            }
        ]
    )

    # Obtiene la respuesta reescrita de OpenAI
    respuestaChatGPT = completion.choices[0].message.content
    print(respuestaChatGPT)
    pc.copy(respuestaChatGPT)
