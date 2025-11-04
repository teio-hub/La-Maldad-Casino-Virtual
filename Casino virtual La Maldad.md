**Casino virtual La Maldad**



**Los valores de la clase Jugador se inicializaran en el codigo antes de la interfaz**



##### clase Jugador:

metodo \_\_init\_\_:

billetera: int

chips: dict\[int: int]

(el dinero será contado en dolares)



metodo mostrar\_saldo: muestra al jugador el saldo actual que tenga



metodo historial(talvez): se guarda en una lista los juegos en los que ha estado el jugador, si ganó o no y el dinero ganado o perdido



##### clase Cashier'sCage:

metodo \_\_init\_\_:

jugador: Jugador



metodo convertir\_dinero: teniendo en cuenta el valor de jugador.billetera se le pregunta al jugador cuantas y cuales fichas quiere intercambiar por el dinero que tenga



metodo convertir\_chips: teniendo en cuenta el valor de jugador.chips se le pregunta al jugador cuantos y cuales chips quiere volver a recibir en dinero



##### clase Baraja:

metodo \_\_init\_\_:

baraja: dict\[str: int]



**En la interfaz de la consola se llama primero la clase casino**



##### clase Casino:

metodo iniciar\_sesion: pide el nombre de usuario para ingresar



**Luego de iniciar sesion se le da al usuario la eleccion de que juego quiere jugar, cambiar la moneda que porte o revisar su propio saldo, en caso de querer jugar se llama a la clase Apuesta**



##### clase Apuesta(ABC):

@abstractmethod

metodo cantidad\_apuesta -> None: ...

(saltar error si la apuesta es <=0 o si ya no tiene el dinero suficiente)



**Esta clase sera la clase padre que luego se heredará a dos hijas siendo estas una de fichas(chips) y otra de dinero convencional(se llamarán segun el juego elegido)**



##### clase Blackjack

metodo \_\_init\_\_:

mano: dict \[str: int]

mano\_crupier: dict \[str: int]



metodo iniciar\_juego: al inicio del juego el crupier saca 2 cartas para el jugador y para el mismo, del crupier una de las cartas será revelada mientras que la otra estará oculta



metodo hit: se saca una carta aleatoria del mazo, si supera el numero 21 pierde.



metodo stand: se comprueba que el valor de las cartas sea mayor o menor que el del crupier, si es menor pierde, si es mayor gana la apuesta (o sea gana su dinero 2 veces)



Notas de la clase:

(en cualquiera de los 2 metodos hit o stand, se debe comprobar de que el crupier tenga un valor de 17 o mayor en sus cartas en caso de ser menor, DEBE sacar una carta, y si se pasa de 21 el crupier pierde ("bust")



(hacer del ... de la baraja inicial cada que se saca una carta)



##### clase Ruleta



**En la interfaz se le pide al jugador que decida si prefiere apostar por numero o color (se ejecuta el metodo respectivo segun la eleccion)**



metodo jugar\_num: gana en caso de acertar el numero y se añade el dinero ganado(investigar el multiplicador)



metodo jugar\_color: gana en caso de acertar el color y se añade el dinero ganado(investigar el multiplicador)





##### clase Tragamonedas



**En la interfaz esta seria la unica clase que no llama a la clase Apuesta debido a que para jugar tiene un cobro fijo, de manera distinta se le pregunta al jugador cuantas tiradas quiere hacer al mismo tiempo**



metodo \_\_init\_\_:

simbolos: list\[str]

matriz: list\[str]

filas:int = field(init = False, default = 3)

columnas:int = field(init = False, default = 3)



metodo jugar(num\_de\_intentos): se ejecutan la cantidad de tiradas especificadas, se muestra el resultado de la matriz y posteriormente se compruebra si existen filas ganadoras, sean diagonales u horizontales (investigar el dinero que se gana al acertar en un tragamonedas)











