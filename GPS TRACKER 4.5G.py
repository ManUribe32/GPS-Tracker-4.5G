import serial
import time

# Configuración del puerto UART
serial_port = "/dev/ttyUSB0"  # Reemplaza esto con el nombre del puerto UART de tu dispositivo
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def enviar_comando(comando):
    ser.write(comando.encode())

def leer_respuesta():
    return ser.readline().decode().strip()

def obtener_ubicacion_actual():
    enviar_comando("AT+CGNSINF\r\n")  # Comando específico para obtener datos de ubicación GPS en algunos dispositivos 4.5G
    respuesta = leer_respuesta()
    # Procesar la respuesta para obtener la ubicación actual
    # La respuesta del GPS puede estar en formato NMEA, que es un estándar de comunicación GPS

# Bucle principal para programar la obtención de la ubicación cada hora
while True:
    obtener_ubicacion_actual()
    time.sleep(3600)  # Esperar una hora antes de obtener la ubicación nuevamente
