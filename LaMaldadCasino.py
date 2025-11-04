from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from random import shuffle
import random

class Jugador:
    def __init__(self, jugador: str, billetera: int):
        self.nombre: str = jugador
        self.billetera: int = billetera
        self.chips: dict[int, int] = {1: 0, 5: 0, 25: 0, 100: 0, 500: 0, 1000: 0}

    def mostrar_saldo(self):
        print(f"\nTu sueldo actual es de ${self.billetera}")
        if self.chips:
            for i in self.chips:
                cantidad = self.chips[i]
                if cantidad > 0:
                    print(f"Tienes {cantidad} ficha(s) de ${i}")
        else:
            print("Actualmente no tienes fichas")

class CashiersCage:
    def __init__(self, jugador: Jugador):
        self.jugador = jugador
        self.valores_fichas: list = [1, 5, 25, 100, 500, 1000]  # Corregido: antes tenía 10 y 50 que no existen

    def convertir_dinero(self):
        print("Conversión de dinero")
        print(f"Saldo disponible: ${self.jugador.billetera} ")
        print(f"Valores de fichas disponibles: {self.valores_fichas}")
        total_compra = 0

        while True:
            valor = input("Ingrese un valor de ficha (0 para salir): ")
            if valor == "0":
                print("Conversión cancelada")
                break
            if not valor.isdigit() or int(valor) not in self.valores_fichas:
                print("Valor incorrecto, por favor ingresa un valor válido")
                continue
            valor = int(valor)

            cantidad = input(f"¿Cuántas fichas de valor ${valor} desea comprar? ")
            if not cantidad.isdigit():
                print("Debe ingresar un número")
                continue
            cantidad = int(cantidad)
            if cantidad <= 0:
                print("Cantidad inválida")
                continue

            costo = valor * cantidad
            if costo > self.jugador.billetera - total_compra:
                print("Saldo insuficiente")
                continue

            total_compra += costo
            self.jugador.chips[valor] += cantidad
            self.jugador.billetera -= costo

            continuar = input("¿Desea comprar más fichas? (1 para sí, 2 para no): ")
            if continuar == "2":
                break

        print(f"\nCompra finalizada. Total gastado: ${total_compra}")

    def convertir_chips(self):
        print("\nConvertir chips a dinero")
        if all(c == 0 for c in self.jugador.chips.values()):
            print("Error, no posees chips")
            return
        total_canjeado = 0
        chips_a_vender = {}
        for valor in self.jugador.chips:
            cantidad = self.jugador.chips[valor]
            if cantidad == 0:
                continue
            print(f"Tienes {cantidad} ficha(s) de ${valor}")
            vender = input(f"¿Cuántas deseas vender de ${valor}? (0 para omitir): ")
            if not vender.isdigit():
                print("Entrada inválida")
                continue
            vender = int(vender)
            if vender < 0 or vender > cantidad:
                print("Cantidad inválida")
                continue
            if vender > 0:
                chips_a_vender[valor] = vender

        for valor, cant in chips_a_vender.items():
            total_canjeado += valor * cant
            self.jugador.chips[valor] -= cant
            if self.jugador.chips[valor] == 0:
                del self.jugador.chips[valor]

        self.jugador.billetera += total_canjeado
        print(f"\nDinero total intercambiado: ${total_canjeado}")

class Baraja:
    def __init__(self):
        self.cartas: dict[str, int] = {
            "A♠": [1, 11], "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10,
            "A♥": [1, 11], "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,
            "A♦": [1, 11], "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,
            "A♣": [1, 11], "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10
        }

class Casino:
    def __init__(self):
        self.jugador: Jugador | None = None

    def iniciar_sesion(self):
        nombre = input("Ingrese su nombre de usuario: ").strip()
        if not nombre:
            print("No puede ser un nombre vacío")
            return False
        saldo = input("Ingrese su saldo inicial (dólares): ")
        if not saldo.isdigit() or int(saldo) <= 0:
            print("El saldo debe ser un número mayor que 0")
            return False
        self.jugador = Jugador(nombre, int(saldo))
        print(f"\nBienvenido {self.jugador.nombre}, disfruta de tu estadía!\n")
        return True

    def menu(self):
        while True:
            print("\n=== MENÚ DEL CASINO ===")
            print("1. Cajero (comprar/vender fichas)")
            print("2. Blackjack")
            print("3. Ruleta")
            print("4. Tragamonedas")
            print("5. Póker")
            print("6. Baccarat")
            print("7. Dados")
            print("8. Bingo")
            print("9. Carrera de Caballos")
            print("0. Salir")
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                cage = CashiersCage(self.jugador)
                print("\n1. Comprar fichas\n2. Vender fichas")
                sub = input("Elige: ")
                if sub == "1":
                    cage.convertir_dinero()
                elif sub == "2":
                    cage.convertir_chips()
            elif opcion == "2":
                baraja = Baraja()
                Blackjack(casino.jugador, baraja).iniciar_juego()
            elif opcion == "3":
                Ruleta(self.jugador).jugar()
            elif opcion == "4":
                intentos = input("¿Cuántas tiradas quieres? ")
                if intentos.isdigit() and int(intentos) > 0:
                    Tragamonedas(self.jugador).jugar(int(intentos))
            elif opcion == "5":
                baraja = Baraja()
                afichas = AFichas(self.jugador)
                Poker(self.jugador, baraja, afichas).iniciar_juego()
            elif opcion == "6":
                baraja = Baraja()
                apuesta = AFichas(self.jugador)
                Baccarat(self.jugador, baraja, apuesta).iniciar_juego()
            elif opcion == "7":
                apuesta = AFichas(self.jugador)
                JuegoDados(self.jugador, apuesta).iniciar_juego()
            elif opcion == "8":
                apuesta = AFichas(self.jugador)
                Bingo(self.jugador, apuesta).iniciar_juego()
            elif opcion == "9":
                apuesta = AFichas(self.jugador)
                CarreraCaballos(self.jugador, apuesta).iniciar_juego()
            elif opcion == "0":
                print("¡Gracias por jugar! Vuelve pronto.")
                break
            else:
                print("Opción inválida")

            self.jugador.mostrar_saldo()

class Apuesta(ABC):
    @abstractmethod
    def cantidad_apuesta(self): ...

class AFichas(Apuesta):
    def __init__(self, jugador: Jugador):
        self.jugador: Jugador = jugador
        self.achips: dict[int, int] = {}

    def cantidad_apuesta(self) -> dict[int, int]:
        self.achips.clear()

        while True:
            total = input("¿Cuánto vas a apostar en total? (solo números): ")
            if total.isdigit() and int(total) > 0:
                total = int(total)
                break
            print("Ingresa un monto válido")

        if total == 0:
            return {}

        print(f"\nTienes que cubrir ${total} con tus fichas.")
        print(f"Fichas disponibles: { {k: v for k, v in self.jugador.chips.items() if v > 0} }")

        restante = total
        temp_apuesta = {}

        while restante > 0:
            chip = input(f"\nValor de ficha (o 0 para cancelar): ")
            if chip == "0":
                print("Apuesta cancelada. Fichas devueltas.")
                return {}
            if not chip.isdigit():
                print("Ingresa un número")
                continue
            chip = int(chip)
            if chip not in self.jugador.chips or self.jugador.chips[chip] == 0:
                print("No tienes fichas de ese valor")
                continue

            max_disp = self.jugador.chips[chip]
            cant = input(f"¿Cuántas fichas de ${chip} (máx {max_disp})? ")
            if not cant.isdigit():
                print("Ingresa un número")
                continue
            cant = int(cant)
            if cant <= 0 or cant > max_disp:
                print("Cantidad inválida")
                continue

            usar = min(cant, (restante + chip - 1) // chip)
            temp_apuesta[chip] = temp_apuesta.get(chip, 0) + usar
            restante -= usar * chip
            print(f"Agregadas {usar} ficha(s) de ${chip}. Restante: ${restante}")

        print(f"\nApuesta lista: {temp_apuesta}")
        print(f"Total apostado: ${total}")
        confirma = input("¿Confirmas? (1 = sí, 2 = no): ")
        if confirma != "1":
            print("Apuesta cancelada.")
            return {}

        for valor, cantidad in temp_apuesta.items():
            self.jugador.chips[valor] -= cantidad
            self.achips[valor] = cantidad

        print("Apuesta confirmada y fichas descontadas.")
        return self.achips

class ADinero(Apuesta):
    def cantidad_apuesta(self) -> int:
        while True:
            apuesta = input("¿Cuánto vas a apostar? (solo números): ")
            if apuesta.isdigit() and int(apuesta) > 0:
                return int(apuesta)
            print("Ingresa un monto válido")

# ------JUEGOS------
class Blackjack:
    def __init__(self, jugador, baraja):
        self.jugador = jugador
        self.baraja = baraja.cartas
        self.mano_jugador = {}
        self.mano_crupier = {}
        self.apuesta = {}

    def valor_mano(self, mano):
        total = 0
        ases = 0
        for v in mano.values():
            if isinstance(v, list):
                total += 11
                ases += 1
            else:
                total += v
        while total > 21 and ases:
            total -= 10
            ases -= 1
        return total

    def iniciar_juego(self):
        print("\n=== BLACKJACK ===\n")


        afichas = AFichas(self.jugador)
        self.apuesta = afichas.cantidad_apuesta()
        if not self.apuesta:
            print("No se hizo apuesta. Volviendo al menú.")
            return

        print(f"\nApuesta confirmada: {sum(v * c for v, c in self.apuesta.items())}$ en fichas\n")

        todas = list(self.baraja.keys())
        shuffle(todas)
        usadas = 0
        self.mano_jugador = {todas[usadas]: self.baraja[todas[usadas]],
                             todas[usadas + 1]: self.baraja[todas[usadas + 1]]}
        usadas += 2
        self.mano_crupier = {todas[usadas]: self.baraja[todas[usadas]],
                             todas[usadas + 1]: self.baraja[todas[usadas + 1]]}
        usadas += 2

        print("Tus cartas:", " | ".join(self.mano_jugador.keys()))
        print("Valor:", self.valor_mano(self.mano_jugador))
        print("Crupier muestra:", list(self.mano_crupier.keys())[0])


        if self.valor_mano(self.mano_jugador) == 21:
            print("\nBLACKJACK! Ganaste 2.5x tu apuesta!")
            for v, c in self.apuesta.items():
                self.jugador.chips[v] += c * 2 + c  # apuesta devuelta + 1.5x ganancia
            return

        while self.valor_mano(self.mano_jugador) < 21:
            accion = input("\n1 = Pedir | 2 = Plantarte → ").strip()
            if accion == "2":
                break
            if accion != "1":
                print("Elige 1 o 2")
                continue

            nueva = todas[usadas]
            self.mano_jugador[nueva] = self.baraja[nueva]
            usadas += 1
            print(f"Recibiste: {nueva}")
            print("Tus cartas:", " | ".join(self.mano_jugador.keys()))
            print("Valor:", self.valor_mano(self.mano_jugador))

            if self.valor_mano(self.mano_jugador) > 21:
                print("\nTE PASASTE DE 21! Perdiste.")
                return

        print(f"\n--- Revelando mano del crupier ---")
        print("Crupier tiene:", " | ".join(self.mano_crupier.keys()))
        print("Valor:", self.valor_mano(self.mano_crupier))

        while self.valor_mano(self.mano_crupier) < 17:
            nueva = todas[usadas]
            self.mano_crupier[nueva] = self.baraja[nueva]
            usadas += 1
            print(f"Crupier pide: {nueva}")
            print("→ Valor actual:", self.valor_mano(self.mano_crupier))


        print("\n" + "=" * 40)
        print("RESULTADO FINAL")
        print("=" * 40)
        print(f"TU MANO → {' | '.join(self.mano_jugador.keys())} = {self.valor_mano(self.mano_jugador)}")
        print(f"CRUPIER → {' | '.join(self.mano_crupier.keys())} = {self.valor_mano(self.mano_crupier)}")

        j = self.valor_mano(self.mano_jugador)
        c = self.valor_mano(self.mano_crupier)

        if j > 21:
            print("PERDISTE → Te pasaste de 21")
        elif c > 21 or j > c:
            print("GANASTE → Tu mano es mejor!")
            for v, cant in self.apuesta.items():
                self.jugador.chips[v] += cant * 2
        elif j < c:
            print("PERDISTE → El crupier ganó")
        else:
            print("EMPATE → Recuperas tu apuesta")
            for v, cant in self.apuesta.items():
                self.jugador.chips[v] += cant

class Ruleta:
    def __init__(self, jugador):
        self.jugador = jugador
        self.numeros_rojos = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
        self.numeros_negros = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

    def jugar_num(self):
        apuesta = ADinero().cantidad_apuesta()
        if apuesta > self.jugador.billetera:
            print("Fondos insuficientes.")
            return
        numero_elegido = input("Selecciona un número del 0 al 36: ")
        if not numero_elegido.isdigit() or not 0 <= int(numero_elegido) <= 36:
            print("Número fuera de rango (0-36).")
            return
        numero_elegido = int(numero_elegido)
        numero_ganador = random.randint(0, 36)
        print(f"El número ganador es: {numero_ganador}")

        if numero_elegido == numero_ganador:
            ganancia = apuesta * 35
            self.jugador.billetera += ganancia
            print(f"¡FELICIDADES! Ganaste ${ganancia}")
        else:
            self.jugador.billetera -= apuesta
            print(f"Perdiste ${apuesta}")

    def jugar_color(self):
        apuesta = ADinero().cantidad_apuesta()
        if apuesta > self.jugador.billetera:
            print("Saldo insuficiente.")
            return
        color_elegido = input("Elige un color (rojo o negro): ").lower()
        if color_elegido not in ["rojo", "negro"]:
            print("Color inválido.")
            return
        numero_ganador = random.randint(0, 36)
        if numero_ganador == 0:
            color_ganador = "verde"
        elif numero_ganador in self.numeros_rojos:
            color_ganador = "rojo"
        else:
            color_ganador = "negro"

        print(f"El número ganador es {numero_ganador} ({color_ganador})")

        if color_elegido == color_ganador:
            self.jugador.billetera += apuesta
            print(f"Ganaste ${apuesta}")
        else:
            self.jugador.billetera -= apuesta
            print(f"Perdiste ${apuesta}")

    def jugar(self):
        print("\nBienvenido a la Ruleta")
        print("1. Apostar a un número (paga 35:1)")
        print("2. Apostar a un color (paga 1:1)")
        tipo = input("Elige una opción (1 o 2): ").strip()

        if tipo == "1":
            self.jugar_num()
        elif tipo == "2":
            self.jugar_color()
        else:
            print("Opción inválida.")

@dataclass
class Tragamonedas:
    jugador: Jugador
    simbolos: list[str] = field(default_factory=lambda: ["Cherry", "Lemon", "Bell", "Star", "Diamond", "Seven"])
    filas: int = 3
    columnas: int = 3
    costo_tirada: int = 100
    matriz: list[list[str]] = field(init=False, default_factory=list)

    def generar_matriz(self):
        self.matriz = [[random.choice(self.simbolos) for _ in range(self.columnas)] for _ in range(self.filas)]

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(" | ".join(fila))
        print()

    def comprobar_ganancias(self) -> int:
        ganancias = 0
        for fila in self.matriz:
            if len(set(fila)) == 1:
                ganancias += 300
        diagonal1 = [self.matriz[i][i] for i in range(self.filas)]
        diagonal2 = [self.matriz[i][self.columnas - i - 1] for i in range(self.filas)]
        if len(set(diagonal1)) == 1:
            ganancias += 500
        if len(set(diagonal2)) == 1:
            ganancias += 500
        return ganancias

    def jugar(self, num_de_intentos: int):
        total_costo = num_de_intentos * self.costo_tirada
        if self.jugador.billetera < total_costo:
            print("Saldo insuficiente para esa cantidad de tiradas.")
            return
        self.jugador.billetera -= total_costo
        total_ganancias = 0

        print(f"\nComenzando {num_de_intentos} tirada(s) del tragamonedas")
        print(f"Costo total: ${total_costo}\n")

        for intento in range(1, num_de_intentos + 1):
            print(f"Tirada #{intento}")
            self.generar_matriz()
            self.mostrar_matriz()
            ganancias = self.comprobar_ganancias()
            if ganancias > 0:
                print(f"¡Ganaste ${ganancias}!")
                total_ganancias += ganancias
            else:
                print("No hubo coincidencias")

        self.jugador.billetera += total_ganancias
        print(f"\nJuego terminado. Ganancia total: ${total_ganancias}")

class Poker:
    def __init__(self, jugador: Jugador, baraja: Baraja, afichas: AFichas):
        self.jugador: Jugador = jugador
        self.baraja: Baraja = baraja
        self.afichas: AFichas = afichas
        self.mano: list[str] = []
        self.mano_crupier: list[str] = []
        self.maxcambio: int = 3

    def iniciar_juego(self):
        print("\nBienvenido a la mesa de póker\n")
        apuesta = self.afichas.cantidad_apuesta()
        if not apuesta:
            return

        todas_cartas = list(self.baraja.cartas.keys())
        shuffle(todas_cartas)
        self.mano = todas_cartas[:5]
        self.mano_crupier = todas_cartas[5:10]

        print("\nTus cartas son:")
        for i in self.mano:
            print(f"- {i}")
        self.cambiar_cartas()
        self.determinar_ganador(apuesta)

    def cambiar_cartas(self):
        if self.maxcambio <= 0:
            return
        print(f"Puedes cambiar hasta 3 cartas ({self.maxcambio} intentos restantes)")
        cambio = input("Ingresa las cartas a cambiar separadas por espacio (o Enter para no cambiar): ")
        if not cambio.strip():
            return

        ccartas = [c.strip() for c in cambio.split() if c.strip() in self.mano]
        if len(ccartas) > 3:
            ccartas = ccartas[:3]

        restantes = [c for c in self.baraja.cartas.keys() if c not in self.mano + self.mano_crupier]
        shuffle(restantes)

        for carta in ccartas:
            idx = self.mano.index(carta)
            self.mano[idx] = restantes.pop()
        self.maxcambio -= 1

    def evaluar_mano(self, mano):
        valores = [c[:-1] for c in mano]
        palos = [c[-1] for c in mano]
        cont = {}
        for v in valores:
            cont[v] = cont.get(v, 0) + 1
        counts = sorted(cont.values(), reverse=True)
        if counts == [5]:
            return 8, "Escalera Real" if len(set(palos)) == 1 else "Escalera"
        if counts == [4, 1]:
            return 7, "Póker"
        if counts == [3, 2]:
            return 6, "Full House"
        if counts == [3, 1, 1]:
            return 3, "Trío"
        if counts == [2, 2, 1]:
            return 2, "Doble Par"
        if counts == [2, 1, 1, 1]:
            return 1, "Par"
        return 0, "Carta Alta"

    def determinar_ganador(self, apuesta):
        val_j, tipo_j = self.evaluar_mano(self.mano)
        val_c, tipo_c = self.evaluar_mano(self.mano_crupier)

        print(f"\nTu mano: {self.mano} → {tipo_j}")
        print(f"Mano del crupier: {self.mano_crupier} → {tipo_c}")

        if val_j > val_c:
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 2
            print("¡Ganaste! Fichas duplicadas.")
        elif val_j < val_c:
            print("Perdiste la ronda.")
        else:
            for v, c in apuesta.items():
                self.jugador.chips[v] += c
            print("Empate. Recuperas tu apuesta.")

class Baccarat:
    def __init__(self, jugador: Jugador, baraja: Baraja, apuesta: AFichas):
        self.jugador = jugador
        self.baraja = baraja
        self.apuesta = apuesta
        self.mazo = list(baraja.cartas.keys())

    def valor_carta(self, carta):
        valor = self.baraja.cartas[carta]
        if isinstance(valor, list):
            return 1
        elif valor >= 10:
            return 0
        return valor

    def valor_mano(self, mano):
        total = sum(self.valor_carta(c) for c in mano)
        return total % 10

    def iniciar_juego(self):
        print("\nBienvenido a la mesa de Baccarat\n")
        tipo = input("¿A qué apuestas? (jugador / banca / empate): ").lower()
        if tipo not in ["jugador", "banca", "empate"]:
            print("Opción inválida. Se cancela la partida.")
            return

        apuesta = self.apuesta.cantidad_apuesta()
        if not apuesta:
            return

        shuffle(self.mazo)
        mano_jugador = [self.mazo.pop(), self.mazo.pop()]
        mano_banca = [self.mazo.pop(), self.mazo.pop()]

        print(f"\nCartas del Jugador: {mano_jugador}")
        print(f"Cartas de la Banca: {mano_banca}")

        # Regla simple: tercera carta solo si < 6
        valor_j = self.valor_mano(mano_jugador)
        valor_b = self.valor_mano(mano_banca)

        if valor_j <= 5:
            mano_jugador.append(self.mazo.pop())
        if valor_b <= 5:
            mano_banca.append(self.mazo.pop())

        valor_j = self.valor_mano(mano_jugador)
        valor_b = self.valor_mano(mano_banca)

        print(f"\nJugador: {mano_jugador} → {valor_j}")
        print(f"Banca:   {mano_banca} → {valor_b}")

        if valor_j > valor_b:
            ganador = "jugador"
        elif valor_b > valor_j:
            ganador = "banca"
        else:
            ganador = "empate"

        print(f"\n¡Gana el {ganador.upper()}!")

        if tipo == ganador:
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 2
            print("¡GANASTE! Fichas duplicadas.")
        else:
            print("Perdiste la apuesta.")


class JuegoDados:
    def __init__(self, jugador: Jugador, apuesta: AFichas):
        self.jugador = jugador
        self.apuesta = apuesta

    def iniciar_juego(self):
        print("\nBienvenido al Juego de los Dados\n")
        print("7 u 11 → ganas al instante")
        print("2, 3 o 12 → pierdes al instante")
        print("Cualquier otro → se vuelve a tirar hasta sacar el punto o un 7\n")

        apuesta = self.apuesta.cantidad_apuesta()
        if not apuesta:
            return

        input("\nPresiona ENTER para lanzar...")
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        suma = d1 + d2
        print(f"\nLanzaste: {d1} + {d2} = {suma}")

        if suma in [7, 11]:
            print("¡GANASTE INMEDIATO!")
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 2
            return

        if suma in [2, 3, 12]:
            print("Casa gana. Perdiste.")
            return
        punto = suma
        print(f"¡Punto establecido: {punto}! Tira hasta sacarlo o un 7.")

        while True:
            input("\nPresiona ENTER para volver a lanzar...")
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            nueva = d1 + d2
            print(f"Nuevo tiro: {d1} + {d2} = {nueva}")

            if nueva == 7:
                print("¡Siete! Pierdes.")
                return
            elif nueva == punto:
                print(f"¡Sacaste el punto {punto}! ¡GANASTE!")
                for v, c in apuesta.items():
                    self.jugador.chips[v] += c * 2
                return
            else:
                print(f"No es {punto} ni 7. Sigue tirando...")


class Bingo:
    def __init__(self, jugador: Jugador, apuesta: AFichas):
        self.jugador = jugador
        self.apuesta = apuesta
        self.carton = random.sample(range(1, 31), 5)

    def iniciar_juego(self):
        print("\nBINGO DEL CASINO")
        print(f"Tu cartón: {sorted(self.carton)}")
        apuesta = self.apuesta.cantidad_apuesta()
        if not apuesta:
            return

        print("\nSe cantan 10 números...")
        cantados = random.sample(range(1, 31), 10)
        print(f"Números: {cantados}")

        aciertos = len(set(self.carton) & set(cantados))
        print(f"\n¡Tienes {aciertos} aciertos!")

        if aciertos >= 4:
            print("¡¡BINGO!! Ganaste 5 veces tu apuesta.")
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 5
        elif aciertos == 3:
            print("Línea. Duplicaste tu apuesta.")
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 2
        elif aciertos >= 1:
            print("Premio menor. Recuperas tu apuesta.")
            for v, c in apuesta.items():
                self.jugador.chips[v] += c
        else:
            print("Sin suerte esta vez.")


class CarreraCaballos:
    def __init__(self, jugador: Jugador, apuesta: AFichas):
        self.jugador = jugador
        self.apuesta = apuesta
        self.caballos = ["Pablo", "Mario", "Pegaso", "Trueno", "Sombra"]

    def iniciar_juego(self):
        print("\n¡CARRERA DE CABALLOS!")
        for i, c in enumerate(self.caballos, 1):
            print(f"{i}. {c}")

        while True:
            eleccion = input("\nElige tu caballo (1-5): ")
            if eleccion.isdigit() and 1 <= int(eleccion) <= 5:
                elegido = self.caballos[int(eleccion) - 1]
                break
            print("Número inválido")

        print(f"\nApostaste por {elegido}")
        apuesta = self.apuesta.cantidad_apuesta()
        if not apuesta:
            return

        print("\n¡SUENA LA CAMPANA! Los caballos arrancan...")
        ganador = random.choice(self.caballos)
        print(f"\n¡¡Y EL GANADOR ES... {ganador.upper()}!!")

        if elegido == ganador:
            print("¡TU CABALLO GANÓ! Triplicaste tu apuesta.")
            for v, c in apuesta.items():
                self.jugador.chips[v] += c * 3
        else:
            print(f"{elegido} llegó en otro puesto. Mejor suerte la próxima.")

if __name__ == "__main__":
    casino = Casino()
    if casino.iniciar_sesion():
        casino.menu()