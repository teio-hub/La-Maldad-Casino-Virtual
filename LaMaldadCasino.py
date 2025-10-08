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
        numeros = list(range(0, 37))
        tirar_bola = random.choice(numeros)

        if tirar_bola == 0:
            color = 'Verde'
        elif tirar_bola % 2 == 0:
            color = 'Negro'
        else:
            color = 'Rojo'

        return f"Bola: {tirar_bola}, ({color})"

    def traga_monedas(self):
        simbolos = ['🍒', '🔔', '💎', '🍋', '7️⃣', '⭐']
        manivela = []
        for i in range(3):
            simbolo = random.choice(simbolos)
            manivela.append(simbolos)

        texto = ""
        for i in range(len(manivela)):
            texto += manivela[i]
            if i < len(manivela) - 1:
                texto += " | "

        if len(set(manivela)) == 1:
            resultado = "¡Jackpot! Ganaste el premio mayor, felicidades."
        elif len(set(manivela)) == 2:
            resultado = "Muy cerca... pero ganaste un premio menor."
        else:
            resultado = "Mala suerte, sigue intentando"
        return f"Manivela: {texto} -> {resultado}"

    def poker(self):
        simbolitos = ['♠', '♥', '♦', '♣']
        valoritos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        mano = []
        texto = ""

        for i in range(5):
            carta = random.choice(valoritos) + random.choice(simbolitos)
            mano.append(carta)
        for i in range(len(mano)):
            texto += ","
            if i < len(mano) - 1:
                texto += ","

        return f"Tu mano de poker: {texto}"

    def baccarat(self):
        jugador = random.randint(0, 9)
        casa = random.randint(0, 9)

        if jugador > casa:
            resultado = "Gana el jugador"
        elif casa > jugador:
            resultado = "Gana la casa"
        else:
            resultado = "Hay empate"
        return f"Jugador: {jugador}, Casa: {casa} -> {resultado}"

    def dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        return f"Dado 1: {dado1}, Dado 2: {dado2}, Total: {suma}"

    def bingo(self):
        carton = random.sample(range(1, 76), 25)
        sorteados = random.sample(range(1, 76), 30)
        aciertos = [num for num in carton if num in sorteados]
        cantidad = len(aciertos)

        if cantidad >= 5:
            resultado = "¡Ganaste al completar una línea!"
        else:
            resultado = "No completaste una línea. Sigue intentando."

        return f"Cartón: {carton[:5]}...\nNúmeros acertados: {cantidad} -> {resultado}"

    def carrera_caballos(self, apuesta: int):
        caballos = ['Caballo 1', 'Caballo 2', 'Caballo 3', 'Caballo 4', 'Caballo 5']
        ganador = random.randint(1, 5)

        if apuesta == ganador:
            resultado = "¡Felicidades! Tu caballo ganó. 🏇🏆"
        else:
            resultado = f"Perdiste. Ganó el {caballos[ganador - 1]}."

        return f"Apostaste al Caballo {apuesta}. Resultado: {resultado}"