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





def help():
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


first_time = True
first_option = "Choose 'option', y and press INTRO to continue: "
option = "Press INTRO"


#BUCLE
while True:
    print()
    if first_time:
        #habla(opcion_inicial)
        option = input(first_option)
        command = option
        first_time = False
    else:
        command = input("-- Press intro -- ")
        if command == "q": quit()
        elif command == "h": help()

    if len(option) > 1:
        continue

    elif option == "e":
        silent_mode = True
        input_text = True
    elif option == "h":
        help()
        continue
    else:
        silent_mode = False
        input_text = False

    os.system("cls")

    start_ai(command)