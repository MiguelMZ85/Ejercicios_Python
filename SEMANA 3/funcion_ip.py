#nombre:Miguel Angel Muso Zuñiga
#nivel:3 A
def validar_ip(ip: str) -> bool:
    """Recibe una dirección IP y devuelve True si es válida, False si no."""
    partes = ip.split(".")
    if len(partes) != 4:
        #aqui se inicializa el proceso en el cual se parte a la direccion en 4 partes
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        if not 0 <= int(parte) <= 255:
            return False
    return True
class Dispositivo:
    """Representa un dispositivo de red con nombre, IP y estado."""

    def __init__(self, nombre: str, ip: str):
        self.nombre = nombre
        self.ip = ip
        self.estado = "apagado"

    def encender(self):
        """Enciende el dispositivo."""
        self.estado = "encendido"
        print(f"✔ El dispositivo '{self.nombre}' ha sido encendido.")

    def mostrar_info(self):
        """Muestra la información del dispositivo."""
        print("-" * 35)
        print(f"  Nombre : {self.nombre}")
        print(f"  IP     : {self.ip}")
        print(f"  Estado : {self.estado}")
        print("-" * 35)

if __name__ == "__main__":
    # 1. Crear un dispositivo, encenderlo y mostrar su información
    router = Dispositivo("Router Principal", "192.168.1.1")
    router.encender()
    router.mostrar_info()

    # 2. Probar la función de validación de IPingresada por teclado
    print()
    while True:
       ip = input("Ingresa la IP para validar: ").strip()
       if ip.lower() == "salir":
        print("¡Hasta luego!")
        break

       if validar_ip(ip):
            print(f'✔ La IP "{ip}" es VÁLIDA.\n')
       else:
            print(f'✘ La IP "{ip}" es INVÁLIDA.\n')

