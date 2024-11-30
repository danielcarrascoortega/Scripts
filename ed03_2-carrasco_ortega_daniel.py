"""import"""
import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
logger = logging.getLogger('CalculadoraCientifica')
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('calculadora.log')
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class CalculadoraCientifica:
    """Calculadora científica"""
    def __init__(self):
        logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Se esperaba un número, se recibió {type(num)}")

    # Operaciones básicas
    def sumar(self,
              a,
              b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info("Sumando {%d} + {%d}", a, b)
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info("Restando {a} - {b}")
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info("Multiplicando {a} * {b}")
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info("Dividiendo {a} / {b}")
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info("Calculando {base} ^ {exponente}")
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error("Intento de calcular raíz cuadrada de número negativo: {numero}")
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        logger.info("Calculando raíz cuadrada de {numero}")
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo de número no positivo: {numero}")
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo natural de {numero}")
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo base 10 de número no positivo: {numero}")
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo base 10 de {numero}")
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando seno de {angulo} radianes")
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando coseno de {angulo} radianes")
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando tangente de {angulo} radianes")
        return math.tan(angulo)

def main():
    """main"""
    # Crear instancia de la calculadora
    calc = CalculadoraCientifica()

        #pedir números por consola
    a = int(input("Introduce el número a: "))
    b = int(input("Introduce el número b: "))

    try:
        # Ejemplos de uso de operaciones básicas
        print("\n=== Operaciones Básicas ===")
        print(f"Suma de {a} + {b} = {calc.sumar(a, b)}")
        print(f"Resta de {a} - {b} = {calc.restar(a, b)}")
        print(f"Multiplicación de {a} * {b} = {calc.multiplicar(a, b)}")
        print(f"División de {a} / {b} = {calc.dividir(a, b)}")

        # Ejemplos de uso de operaciones avanzadas
        print("\n=== Operaciones Avanzadas ===")
        print(f"Potencia de {a} ^ {b} = {calc.potencia(a, b)}")
        print(f"Raíz cuadrada de {a} = {calc.raiz_cuadrada(a)}")
        print(f"Logaritmo natural de {a} = {calc.logaritmo_natural(a)}")
        print(f"Logaritmo base 10 de {a} = {calc.logaritmo_base_10(a)}")

        # Ejemplos de funciones trigonométricas
        print("\n=== Funciones Trigonométricas ===")
        angulo = math.pi/2
        print(f"Seno de π/2 = {calc.seno(angulo)}")
        print(f"Coseno de π/2 = {calc.coseno(angulo)}")
        print(f"Tangente de π/4 = {calc.tangente(math.pi/4)}")

        # Ejemplo de manejo de errores
        print("\n=== Prueba de Manejo de Errores ===")
        print("Intentando dividir por cero:")
        calc.dividir(a, 0)

    except ValueError as e:
        logger.error("Error de valor: {str(e)}")
        print(f"Error de valor: {e}")
    except TypeError as e:
        logger.error("Error de tipo: {str(e)}")
        print(f"Error de tipo: {e}")
    except ImportError as e:
        logger.error("Error inesperado: {str(e)}")
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
