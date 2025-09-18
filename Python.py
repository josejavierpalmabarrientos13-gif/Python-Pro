# Diccionario de palabras (memes y expresiones)
memes = {
    "gg": "Bien jugado",
    "cringe": "Algo excepcionalmente raro o vergonzoso",
    "nt": "Buen intento",
    "afk": "Lejos del teclado, ausente",
    "brb": "Vuelvo enseguida",
    "lol": "Reírse mucho",
    "wp": "Bien hecho",
    "noob": "Principiante"
}

# Saludo e instrucciones
print("¡Hola! Bienvenido al traductor de palabras gamer/meme 😎")
print("Escribe una palabra como 'gg', 'cringe', 'nt', 'lol'...")
print("Tienes 5 intentos para preguntar palabras.\n")

# Bucle para 5 intentos
intentos = 0
while intentos < 5:
    palabra = input("Dime una palabra que no entiendas: ")
    if palabra in memes:
        print("👉", memes[palabra])
    else:
        print("❌ Esa palabra no existe en el diccionario.")
    intentos += 1

print("\n¡Gracias por usar el traductor! 🚀")
