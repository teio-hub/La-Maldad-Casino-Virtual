import random

class Casino:
    def black_jack(self):
        cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                          'K': 10}
        mano = random.sample(cartas, 2)
        puntos = 0
        ases = mano.count('A')

        for carta in mano:
            if carta == 'A':
                continue
            puntos += valores_cartas[carta]

        for i in range(ases):
            if puntos + 11 <= 21:
                puntos += 11
            else:
                puntos += 1

        return f"cartas: {mano}, {puntos}"

    def ruleta(self):
        colores = ['Rojo', 'Negro', 'Verde']
        numeros = list(range(0, 37))
        tirar_bola = random.choice(numeros)

        if tirar_bola == 0:
            color = 'Verde'
        elif tirar_bola % 2 == 0:
            color = 'Negro'
        else:
            color = 'Rojo'

        return f"Bola: {tirar_bola}, ({color})"