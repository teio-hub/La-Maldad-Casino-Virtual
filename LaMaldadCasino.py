
from abc import ABC, abstractmethod


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
        pass

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