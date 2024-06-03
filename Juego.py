import sys
import random
import threading
from PyQt6 import QtWidgets, QtGui, QtCore
from battle_qt import Ui_MainWindow
import serial
import pyttsx3

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Señales personalizadas para actualizar la interfaz desde el hilo de procesamiento
    barco_impactado = QtCore.pyqtSignal(str, int)
    barco_hundido = QtCore.pyqtSignal(str)
    barco_movido = QtCore.pyqtSignal(str, str)
    explosion_material = QtCore.pyqtSignal(list)
    actualizar_boton = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Inicializa la comunicación serial con Arduino
        self.serial = serial.Serial('COM4', 9600)

        # Conectar señales a los slots correspondientes
        self.barco_impactado.connect(self.actualizar_barco_impactado)
        self.barco_hundido.connect(self.actualizar_barco_hundido)
        self.barco_movido.connect(self.actualizar_barco_movido)
        self.explosion_material.connect(self.actualizar_explosion_material)
        self.actualizar_boton.connect(self.cambiar_color_boton)

        # Nombre de los labels de los barcos
        self.label_names = [
            "A1", "A2", "A3", "A4", "A5",
            "B1", "B2", "B3", "B4", "B5",
            "C1", "C2", "C3", "C4", "C5",
            "D1", "D2", "D3", "D4", "D5",
            "E1", "E2", "E3", "E4", "E5",
        ]

        # Nombre de los botones
        self.buttons_names = [
            "A1_b", "A2_b", "A3_b", "A4_b", "A5_b",
            "B1_b", "B2_b", "B3_b", "B4_b", "B5_b",
            "C1_b", "C2_b", "C3_b", "C4_b", "C5_b",
            "D1_b", "D2_b", "D3_b", "D4_b", "D5_b",
            "E1_b", "E2_b", "E3_b", "E4_b", "E5_b",
        ]

        self.label_names_mod = self.label_names.copy()

        # Inicializar el número de ronda
        self.numero_ronda = 0

        # Inicializar el turno
        self.mi_turno = random.choice([True, False])

        self.imagen_agua = QtGui.QPixmap("img/agua.png")
        self.imagen_agua = self.imagen_agua.scaled(100, 100)

        self.imagen_bomba = QtGui.QPixmap("img/bomba.jpg")
        self.imagen_bomba = self.imagen_bomba.scaled(100, 100)

        for label_name in self.label_names:
            # Obtener el QLabel por su nombre
            label = getattr(self, label_name)

            # Establecer la imagen en el QLabel
            label.setPixmap(self.imagen_agua)

        # Imágenes de los barcos
        self.imagenes_barcos = {
            "portaaviones": QtGui.QPixmap("img/portaaviones.jpg").scaled(100, 100),
            "barco_guerra": QtGui.QPixmap("img/barco_guerra.jpg").scaled(100, 100),
            "submarino": QtGui.QPixmap("img/submarino.jpg").scaled(100, 100)
        }

        # Diccionario para almacenar las posiciones de los barcos propios
        self.posiciones_barcos = {}
        self.vidas_barcos = {
            "portaaviones": 3,
            "barco_guerra": 2,
            "submarino": 1
        }

        # Diccionario para almacenar las posiciones de los barcos enemigos
        self.posiciones_barcos_enemigos = {}

        # Lista para registrar posiciones de explosiones
        self.posiciones_explosionadas = []

        # Botón para colocar barcos aleatorios
        self.orden.clicked.connect(self.tablero)

        self.explosion.clicked.connect(self.ejecutar_explosion)
        self.uso_explosion = False  # Para controlar que se use una única vez

        for button_name in self.buttons_names:
            button = getattr(self, button_name)
            button.clicked.connect(self.enviar_posicion_barco)
            button.setMinimumSize(QtCore.QSize(80, 80))

        # Botón para jugar
        self.jugar.clicked.connect(self.jugar_partida)

        # Lista y lock para manejar las posiciones enviadas
        self.posiciones_ataques_recibidos = []
        self.lock = threading.Lock()

    def tablero(self):
        self.numero_ronda = 0
        self.label_names_mod = self.label_names.copy()
        self.n_rondas.setText(str(self.numero_ronda))

        # Primero, limpiar todos los labels a la imagen de agua
        for label_name in self.label_names:
            label = getattr(self, label_name)
            label.setPixmap(self.imagen_agua)

        # Reiniciar el diccionario de posiciones de los barcos
        self.posiciones_barcos = {}
        self.posiciones_barcos_enemigos = {}
        self.posiciones_explosionadas = []  # Reiniciar posiciones de explosiones

        # Asignar aleatoriamente las posiciones de los barcos
        self.asignar_posiciones_barco("portaaviones", 1)
        self.asignar_posiciones_barco("barco_guerra", 2)
        self.asignar_posiciones_barco("submarino", 4)

        # Colocar las imágenes de los barcos en los QLabel correspondientes
        for label_name, datos_barco in self.posiciones_barcos.items():
            label = getattr(self, label_name)
            label.setPixmap(datos_barco['imagen'])  # Acceder correctamente a la imagen

        print("Posiciones de los barcos propios:")
        for posicion, datos in self.posiciones_barcos.items():
            print(f"Posición: {posicion}, Vida: {datos['vida']}, Tipo: {datos['tipo']}")

    def asignar_posiciones_barco(self, tipo_barco, cantidad):
        posiciones_disponibles = self.label_names_mod
        for _ in range(cantidad):
            if not posiciones_disponibles:
                break
            posicion = random.choice(posiciones_disponibles)
            self.posiciones_barcos[posicion] = {
                "imagen": self.imagenes_barcos[tipo_barco],
                "vida": self.vidas_barcos[tipo_barco],
                "tipo": tipo_barco
            }
            posiciones_disponibles.remove(posicion)

    def enviar_posicion_barco(self):
        button = self.sender()
        button_name = button.objectName().replace("_b", "")
        self.serial.write(button_name.encode())
        button.setStyleSheet("background-color: orange")

        self.text_to_speech("Capitan, enviamos ataque.")

    def actualizar_barco_impactado(self, posicion, vida_restante):
        label = getattr(self, posicion)
        label.setPixmap(self.imagen_bomba)
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(f"¡El enemigo ha impactado en la posición {posicion}! Vida restante: {vida_restante}")
        msg_box.setWindowTitle("Impacto")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def actualizar_barco_hundido(self, posicion):
        label = getattr(self, posicion)
        label.setPixmap(self.imagen_bomba)
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(f"¡El enemigo ha hundido un barco en la posición {posicion}!")
        msg_box.setWindowTitle("Barco Hundido")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.text_to_speech("¡Oh no!, te atacarn.")

    def actualizar_barco_movido(self, posicion_antigua, nueva_posicion):
        barco = self.posiciones_barcos[nueva_posicion]
        label_nueva_posicion = getattr(self, nueva_posicion)
        label_nueva_posicion.setPixmap(barco['imagen'])

        label_antigua_posicion = getattr(self, posicion_antigua)
        label_antigua_posicion.setPixmap(self.imagen_agua)

    def mostrar_impacto_fallido(self):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("¡El enemigo ha fallado el impacto!")
        msg_box.setWindowTitle("Alerta")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()


    def actualizar_explosion_material(self, posiciones_afectadas):
        for posicion in posiciones_afectadas:
            label = getattr(self, posicion)
            label.setPixmap(self.imagen_bomba)
            if posicion in self.posiciones_barcos:
                del self.posiciones_barcos[posicion]

        # Agregar posiciones afectadas a la lista de explosiones
        self.posiciones_explosionadas.extend(posiciones_afectadas)
    
    def ejecutar_explosion(self):
        if self.numero_ronda < 6:
            self.alerta_explosion_ronda()
            return
        elif self.uso_explosion:
            self.alerta_explosion_uso()
            return
        self.explosion_ejecutada()
         # Seleccionar una posición aleatoria
        posicion_central = random.choice(self.label_names)
        self.uso_explosion = True  # Marcar la explosión como usada
        
        # Envía la posición central con el caracter "XX" para indicar que es la explosión de material
        self.exp_m = f"{posicion_central}XX"
        self.serial.write(self.exp_m.encode())

        fila = ord(posicion_central[0]) - ord('A')
        columna = int(posicion_central[1]) - 1
        posiciones_cruz = [posicion_central]

        # Arriba
        if fila > 0:
            posiciones_cruz.append(chr(fila + ord('A') - 1) + str(columna + 1))
        
        # Abajo
        if fila < 4:
            posiciones_cruz.append(chr(fila + ord('A') + 1) + str(columna + 1))
        
        # Izquierda
        if columna > 0:
            posiciones_cruz.append(chr(fila + ord('A')) + str(columna))
        
        # Derecha
        if columna < 4:
            posiciones_cruz.append(chr(fila + ord('A')) + str(columna + 2))

        print(posiciones_cruz)
        for cruz in posiciones_cruz:
            button = getattr(self, f"{cruz}_b")
            button.setStyleSheet("background-color: red")
            button.setEnabled(False)

    def explosion_ejecutada(self):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("Explosión de material realizada!")
        msg_box.setWindowTitle("Exito!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.text_to_speech("¡OH wow, se ven muchas luces a lo lejos.")

        
    def alerta_explosion_ronda(self):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("Explosión de material aún no disponible")
        msg_box.setWindowTitle("¡Aún NO!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.text_to_speech("Arma secreta disponible en ronda 6.")

    def alerta_explosion_uso(self):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("Explosión de material ya utilizada")
        msg_box.setWindowTitle("Atención!!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.text_to_speech("Ya usaste tu arma secreta.")

    def alerta(self, exp):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(f"Te enviaron una explosión de material en {exp}")
        msg_box.setWindowTitle("¡¡¡Alerta!!!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        self.text_to_speech("¡Oh no!, te atacaron fuerte.")

    def victoria(self):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("FELICIDADES! HAZ GANADO EL JUEGO")
        msg_box.setWindowTitle("FELICIDADES!")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()
        self.turno.setText("Ganador")

        self.text_to_speech("¡Felicidades!, haz ganado el juego.")

        for button_name in self.buttons_names:
            button = getattr(self, button_name)
            button.setEnabled(False)
        self.explosion.setEnabled(False)
        self.jugar.setEnabled(False)

    def derrota(self):
        self.text_to_speech("¡Lo lamento!, mas suerte para la proxima.")
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("Lo harás mejor la próxima vez")
        msg_box.setWindowTitle("DERROTA")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()
        self.turno.setText("Perdedor")

        for button_name in self.buttons_names:
            button = getattr(self, button_name)
            button.setEnabled(False)
        self.explosion.setEnabled(False)
        self.jugar.setEnabled(False)

    def jugar_partida(self):
        # Mostrar alerta
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText("Esperando al otro jugador")
        msg_box.setWindowTitle("Espera")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

        # Enviar el carácter 'JJ' por comunicación serial
        self.serial.write(b'JJ')

        # Configurar un temporizador para verificar si se recibe 'JJ' de vuelta
        self.timer_jj = QtCore.QTimer(self)
        self.timer_jj.timeout.connect(self.verificar_jj_recibido)
        self.timer_jj.start(20)

    def verificar_jj_recibido(self):
        if self.serial.in_waiting > 0:
            data = self.serial.readline().decode().strip()
            if 'JJ' in data:
                print("Ambos jugadores están listos. ¡Comienza la partida!")
                self.text_to_speech("Comienza el juego.")
                self.numero_ronda = 1

                self.orden.setEnabled(False)

                self.n_rondas.setText(str(self.numero_ronda))
                self.timer_jj.stop()

                self.timer_ss = QtCore.QTimer(self)
                self.timer_ss.timeout.connect(self.procesar_confirmacion_impacto)
                self.timer_ss.start(20)

                if self.mi_turno:
                    self.turno.setText("Tu Turno")
                    self.partida = "TT\n"
                    self.serial.write(self.partida.encode())

                    for button_name in self.buttons_names:
                        button = getattr(self, button_name)
                        button.setEnabled(True)
                    self.explosion.setEnabled(True)
                    self.jugar.setEnabled(True)
                else:
                    self.turno.setText("Turno Oponente")
                    self.partida = "TO\n"
                    self.serial.write(self.partida.encode())

                    for button_name in self.buttons_names:
                        button = getattr(self, button_name)
                        button.setEnabled(False)
                    self.explosion.setEnabled(False)
                    self.jugar.setEnabled(False)
                
    def cambiar_color_boton(self, posicion):
        button = getattr(self, f"{posicion}_b")
        button.setStyleSheet("background-color: green")

    def procesar_confirmacion_impacto(self):
        if self.serial.in_waiting > 0:
            data = self.serial.read(self.serial.in_waiting).decode().strip()
            if data.endswith('SS'):
                posicion = data.split('SS')[0]
                self.actualizar_boton.emit(posicion)
                self.mostrar_confirmacion_impacto(posicion, True)
                self.text_to_speech("¡¡Bien!!, barco destruido.")
                self.numero_ronda += 1
                self.n_rondas.setText(str(self.numero_ronda))
                self.mi_turno = not self.mi_turno
                self.turnos_juego()

            elif data.endswith('NN'):
                posicion = data.split('NN')[0]
                self.mostrar_confirmacion_impacto(posicion, False)
                self.text_to_speech("¡¡Oh no!!, hay que apuntar mejor.")
                self.numero_ronda += 1
                self.n_rondas.setText(str(self.numero_ronda))
                self.mi_turno = not self.mi_turno
                self.turnos_juego()


            if data in self.label_names:
                self.numero_ronda += 1
                self.n_rondas.setText(str(self.numero_ronda))
                self.mi_turno = not self.mi_turno
                self.turnos_juego()

                if data in self.posiciones_barcos:
                    self.mensaje = f"{data}SS"
                    self.serial.write(self.mensaje.encode())
                    self.posiciones_explosionadas.append(data)

                    barco = self.posiciones_barcos[data]
                    barco['vida'] -= 1
                    self.barco_impactado.emit(data, barco['vida'])

                    if barco['vida'] <= 0:
                        self.barco_hundido.emit(data)
                        del self.posiciones_barcos[data]
                    else:
                        # Excluir posiciones explosionadas
                        posiciones_disponibles = [pos for pos in self.label_names if pos not in self.posiciones_barcos and pos not in self.posiciones_explosionadas]
                        if posiciones_disponibles:
                            nueva_posicion = random.choice(posiciones_disponibles)
                            self.posiciones_barcos[nueva_posicion] = self.posiciones_barcos.pop(data)
                            self.barco_movido.emit(data, nueva_posicion)

                    if not self.verificar_barcos_con_vida():
                        print("Ya no te quedan barcos con vida.")
                        self.gg = "GG"
                        self.serial.write(self.gg.encode())

                elif data not in self.posiciones_barcos:
                    self.mostrar_impacto_fallido()
                    self.mensaje = f"{data}NN"
                    self.serial.write(self.mensaje.encode())
                    self.text_to_speech(f"¡¡UU!!, por poco nos disparan. El enemigo atacó en {data}")

            elif "TO" in data:
                self.turno.setText("Tu Turno")
                self.mi_turno = True

                for button_name in self.buttons_names:
                        button = getattr(self, button_name)
                        button.setEnabled(True)
                self.explosion.setEnabled(True)
                self.jugar.setEnabled(True)

            elif "TT" in data:
                self.turno.setText("Turno Oponente")
                self.mi_turno = False

                for button_name in self.buttons_names:
                        button = getattr(self, button_name)
                        button.setEnabled(False)
                self.explosion.setEnabled(False)
                self.jugar.setEnabled(False)

            elif data.endswith('XX'):
                exp = data.split('XX')[0]
                self.alerta(exp)

                # Seleccionar una posición
                posicion_central = exp

                # Calcular las posiciones afectadas por la explosión en cruz
                fila = posicion_central[0]
                columna = int(posicion_central[1:])
                posiciones_afectadas = [posicion_central]  # Incluir la posición central

                # Posiciones horizontales y verticales adyacentes
                if columna > 1:
                    posiciones_afectadas.append(f"{fila}{columna - 1}")
                if columna < 5:
                    posiciones_afectadas.append(f"{fila}{columna + 1}")
                if fila > 'A':
                    posiciones_afectadas.append(f"{chr(ord(fila) - 1)}{columna}")
                if fila < 'E':
                    posiciones_afectadas.append(f"{chr(ord(fila) + 1)}{columna}")

                # Emitir señal para actualizar las posiciones afectadas
                self.explosion_material.emit(posiciones_afectadas)
                print(f"Explosión de material ejecutada en {posicion_central}.")

            # Verificar si ya no te quedan barcos con vida al final del procesamiento
            if not self.verificar_barcos_con_vida():
                print("Ya no te quedan barcos con vida.")
                self.gg = "GG"
                self.serial.write(self.gg.encode())
                self.derrota()

            if "GG" in data:
                self.victoria()

    def turnos_juego(self):
        if self.mi_turno:
            self.turno.setText("Tu Turno")
            for button_name in self.buttons_names:
                button = getattr(self, button_name)
                button.setEnabled(True)
            self.explosion.setEnabled(True)
            self.jugar.setEnabled(True)
        else:
            self.turno.setText("Turno Oponente")
            for button_name in self.buttons_names:
                button = getattr(self, button_name)
                button.setEnabled(False)
            self.explosion.setEnabled(False)
            self.jugar.setEnabled(False)


    def mostrar_confirmacion_impacto(self, posicion, impacto):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        if impacto:
            msg_box.setText(f"¡Has impactado un barco en la posición {posicion}!")
        else:
            msg_box.setText("Has fallado el impacto.")
        msg_box.setWindowTitle("Resultado del ataque")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def verificar_barcos_con_vida(self):
        for barco in self.posiciones_barcos.values():
            if barco["vida"] > 0:
                return True
            else: 
                return False
            
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowTitle("Battleship del Mr.Willu")
    sys.exit(app.exec())