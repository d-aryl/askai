import os
import openai
import json


openai.api_key = "YOUR GP3 SECRET API HERE"

def execute_AI(message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= message + "\nA:",
            temperature=0.1,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            # stop=["\n"]
        )

        i = json.loads(str(response))

        ai_response = i["choices"][0]["text"]

        # print(respuesta)
        # os.system("cls")
        print("Thinking...")
        print(ai_response)


    except:
        pass


def start_ai(command):

    if input_text:
        if command == "t":
            message = input("Text to translate: ")
            message = "Translate to english: " + message

        else:
            message = input("What is your question: ")
            os.system("cls")
            print("Text to process: \"" + message + "\"")

        print("Procesing...")
        execute_AI(message)
        return





def ayuda():
    print()
    print()
    print("******************************************")
    print("*             -- ASK_AI --               *")
    print("*                                        *")
    print("*           'E' (normal mode)            *")
    print("*           'T' (translate mode)         *")
    print("*           'H' (Help)                   *")
    print("*           'Q' (Quit app)               *")
    print("*                                        *")
    print("******************************************")
    print()

# INICIO DELPROGRAMA

os.system("cls")
print()
print()
print("******************************************")
print("*             -- ASK_AI --               *")
print("*                                        *")
print("* OPTIONS :                              *")
print("*           'E' (Normal mode)            *")
print("*           'H' (Help)                   *")
print("*           'Q' (quit)                   *")
print("*                                        *")
print("*               Developed by:            *")
print("*           RAUL TORRICO  ©2023          *")
print("*                                        *")
#print("*                                        *")
#print("*          (Dedicado a Míriam)           *")
#print("*                                        *")
print("******************************************")
print()
print()


primer_paso = True
opcion_inicial = "Choose 'option', y and press INTRO to continue: "
opcion = "Press INTRO"


#BUCLE
while True:
    print()
    if primer_paso:
        #habla(opcion_inicial)
        opcion = input(opcion_inicial)
        comando = opcion
        primer_paso = False
    else:
        comando = input("-- Pulsa intro -- ")
        if comando == "q": quit()
        elif comando == "h": ayuda()

    if len(opcion) > 1:
        continue

    elif opcion == "e":
        silent_mode = True
        input_text = True
    elif opcion == "h":
        ayuda()
        continue
    else:
        silent_mode = False
        input_text = False

    os.system("cls")

    start_ai(comando)