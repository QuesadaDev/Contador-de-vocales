def contador_vocal(texti):

    frecuencia_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for letra in texti:
        if letra in frecuencia_vocales:
            frecuencia_vocales[letra] += 1

    return frecuencia_vocales


texto = input("Introduce el texto que quieras: ")
resul = contador_vocal(texto.lower())

for vocal, frecuencia in resul.items():
    print(f"La vocal {vocal} aparece {frecuencia} veces.")

