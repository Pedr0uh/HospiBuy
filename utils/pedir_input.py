import main

def pedir_input(texto): # função para validar input igual a zero e retorna para menu inicial
    valor = input(texto)
    if valor == "0":
        print("\nVoltando a o Menu Inicial...\n")
        return None
    return valor