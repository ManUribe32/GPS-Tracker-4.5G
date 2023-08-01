# GPS-Tracker-4.5G
El programa propuesto tiene como objetivo controlar un dispositivo GPS que se comunica a través de una señal 4.5G móvil. La función principal del programa es obtener la ubicación actual del dispositivo GPS y enviar comandos para realizar esta tarea de forma periódica (cada hora).
características principales del programa:

Configuración del puerto UART: El programa utiliza la biblioteca pyserial para configurar y abrir una conexión con el puerto UART al que está conectado el dispositivo GPS. El puerto UART es la interfaz de comunicación utilizada para enviar y recibir datos desde el dispositivo.

Funciones para enviar y recibir comandos: El programa contiene funciones para enviar comandos al dispositivo GPS y leer las respuestas del mismo. En este ejemplo, se utiliza el comando AT+CGNSINF para obtener datos de ubicación GPS. Ten en cuenta que el comando específico puede variar según el dispositivo GPS que estés utilizando.

Obtención de la ubicación actual: La función obtener_ubicacion_actual() envía el comando al dispositivo GPS para obtener los datos de ubicación. La respuesta del GPS puede estar en formato NMEA, que es un estándar de comunicación GPS. Sin embargo, en este ejemplo, la lógica para procesar la respuesta y extraer la ubicación exacta no se proporciona, ya que esto dependerá del formato y protocolo específico del dispositivo GPS utilizado.

Bucle principal para programar la obtención de ubicación: El programa tiene un bucle infinito (while True) que se ejecuta continuamente. En cada iteración del bucle, se llama a la función obtener_ubicacion_actual() para obtener la ubicación actual del GPS. Después de eso, el programa espera una hora (time.sleep(3600)) antes de obtener la ubicación nuevamente. Esto permite que el programa obtenga la ubicación cada hora.
