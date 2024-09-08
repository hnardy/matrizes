#5. Mini Projeto: Sistema de Reservas para um Pequeno Cinema
#Descrição:
#Um pequeno cinema possui várias salas e cada sala tem um número determinado de assentos.
# Vamos criar um sistema simples onde os clientes podem escolher uma sala e um assento, e o sistema registra a reserva.
#Estrutura:
#1. A matriz representará as salas e assentos. Se uma sala tiver 5 assentos, uma matriz 1x5 será criada, e assim por diante.
#Uma sala com 20 assentos poderia ser representada como uma matriz 4x5.
#2. Uma célula da matriz com valor 0 indica que o assento está disponível. Se tiver valor 1, o assento está reservado.
#Funcionalidades:
#1. Exibir as salas e assentos com seus respectivos estados (reservado ou disponível).
#2. Permitir a reserva de um assento em uma sala.
#3. Cancelar a reserva de um assento.
#4. Mostrar a taxa de ocupação de cada sala.
#


class Cinema:
    def __init__(self):
        # Criar várias salas, cada uma com uma matriz de assentos (0 - disponível, 1 - reservado)
        self.salas = {
            1: [[0, 0, 0, 0, 0]],    # Sala 1 - 1 fila com 5 assentos
            2: [[0, 0, 0, 0, 0],      # Sala 2 - 2 filas com 5 assentos
                [0, 0, 0, 0, 0]],
            3: [[0, 0, 0, 0, 0],      # Sala 3 - 4 filas com 5 assentos
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        }

    def exibir_salas(self):
        """Exibe o estado atual dos assentos em cada sala."""
        for sala, assentos in self.salas.items():
            print(f"Sala {sala}:")
            for fila in assentos:
                print(" ".join(str(a) for a in fila))
            print()  # Separação entre as salas

    def reservar_assento(self, sala, fila, assento):
        """Reserva um assento se estiver disponível."""
        if self.salas[sala][fila][assento] == 0:
            self.salas[sala][fila][assento] = 1
            print(f"Assento {assento + 1} na fila {fila + 1} da Sala {sala} foi reservado.")
        else:
            print("Assento já está reservado.")

    def cancelar_reserva(self, sala, fila, assento):
        """Cancela a reserva de um assento."""
        if self.salas[sala][fila][assento] == 1:
            self.salas[sala][fila][assento] = 0
            print(f"Reserva do assento {assento + 1} na fila {fila + 1} da Sala {sala} foi cancelada.")
        else:
            print("Assento já está disponível.")

    def taxa_ocupacao(self, sala):
        """Calcula e exibe a taxa de ocupação de uma sala."""
        total_assentos = sum(len(fila) for fila in self.salas[sala])
        assentos_ocupados = sum(assento for fila in self.salas[sala] for assento in fila)
        taxa = (assentos_ocupados / total_assentos) * 100
        print(f"Taxa de ocupação da Sala {sala}: {taxa:.2f}%")

# Exemplo de uso do sistema
cinema = Cinema()

# Exibir o estado inicial das salas
cinema.exibir_salas()

# Reservar alguns assentos
cinema.reservar_assento(1, 0, 2)  # Reservar o assento 3 da fila 1 da sala 1
cinema.reservar_assento(3, 2, 4)  # Reservar o assento 5 da fila 3 da sala 3

# Exibir o estado atual das salas após as reservas
cinema.exibir_salas()

# Cancelar uma reserva
cinema.cancelar_reserva(1, 0, 2)

# Exibir o estado atual das salas após o cancelamento
cinema.exibir_salas()

# Mostrar a taxa de ocupação da sala 3
cinema.taxa_ocupacao(3)
