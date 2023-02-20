import os
import openai
import json


openai.api_key = "GP3 SECRET API HERE"




def execute_AI(mensaje):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=mensaje + "\nA:",
            temperature=0.1,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            # stop=["\n"]
        )

        i = json.loads(str(response))

        respuesta = i["choices"][0]["text"]

        # print(respuesta)
        # os.system("cls")
        print("Respondiendo...")
        print(respuesta)


    except:
        pass


def start_ai(comando):

    if input_text:
        if comando == "t":
            mensaje = input("Texto a traducir: ")
            mensaje = "Traduce al ingles: " + mensaje

        else:
            mensaje = input("Cual es la pregunta: ")
            os.system("cls")
            print("Texto a procesar: \"" + mensaje + "\"")

        print("Procesando...")
        execute_AI(mensaje)
        return





def ayuda():
    print()
    print()
    print("******************************************")
    print("*             -- ASK_AI --               *")
    print("*                                        *")
    print("*           'E' (modo normal)            *")
    print("*           'T' (modo traduccion)        *")
    print("*           'H' (Ayuda)                  *")
    print("*           'Q' (salir del sistema)      *")
    print("*                                        *")
    print("******************************************")
    print()
    print("Opcion 'E' (modo normal)")
    print("     Responde a lo que le escribamos por consola")
    print()
    print("Opcion 'T' (modo traduccion)")
    print("     Traduce lo que le escribamos por consola")
    print()
    print("Opcion 'H' (Ayuda)")
    print("     Se imprimira esta ayuda por consola")
    print()
    print("Opcion 'q' (Salir del sistema)")
    print("     El programa terminara y se cerrara la consola de comandos de la IA")
    print()
    print("------------------------------------------------------------------------------------")
    print()
# INICIO DELPROGRAMA

os.system("cls")
print()
print()
print("******************************************")
print("*             -- ASK_AI --               *")
print("*                                        *")
print("* OPCIONES:                              *")
print("*           'E' (Normal)                  *")
print("*           'H' (Ayuda)                  *")
print("*           'Q' (salir del sistema)      *")
print("*                                        *")
print("*       Programa desarrollado por:       *")
print("*           RAUL TORRICO  ©2023          *")
print("*                                        *")
#print("*                                        *")
#print("*          (Dedicado a Míriam)           *")
#print("*                                        *")
print("******************************************")
print()
print()


pregunta_nombre = "Cuál es tu nombre?: "
intro = "Hola, bienvenido al sistema de ayuda ask ai. Para comenzar teclee la opción de interacción, s para modo silencioso, e para modo escritura y n para modo normal, y a continuación la tecla intro"

#habla(intro)

#habla(pregunta_nombre)
#nombre = input(pregunta_nombre)

primer_paso = True
opcion_inicial = "Elige 'opcion', y pulsa INTRO para continuar: "
opcion = "Pulsa INTRO"


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