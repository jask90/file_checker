# file_checker

# Requisitos

* Python 3 (Cómo instalar Python3 en Mac: https://www.youtube.com/watch?v=itBE25gYEeY)

# Ejecutar aplicación

Abrir una terminal en la raiz del proyecto y ejecutar python3 main.py
Otra opción el abrir el fichero con "Python Launcher", y esto ya abrirá una terminal ejecutando el fichero.

# Cerrar la aplicación

Al cerrar la terminal se terminará la ejecución del programa.
Otras formas pueden ser hacer "Ctrl + C" en la terminal para cerrar el proceso, o al apagar el ordenador.

# Configuración del proyecto

La configuración del proyecto está en el fichero settings.py.
Para modificarlo basta con abrirlo con cualquier aplicación de texto como un bloc de notas y guardar los cambios.

En el fichero settings.py se configura la siguiente información:
* TELEGRAM_TOKEN -> Token del bot de Telegram
* TELEGRAM_CHAT_ID -> ID del chat al que se envían los mensajes de Telegram
* MAIN_DIRS -> Lista de directorios principales. Se controlarán lo ficheros de todos estos directorios y de los que haya dentro.
* WAIT_TIME -> Cantidad de tiempo en segundos que se espera entre comprobación y comprobación.

Ejemplo de MAIN_DIRS, dónde se indican 2 directorios a controlar, separados por comas:
> MAIN_DIRS = ["/Users/usuario/Documents/directorio1", /Users/usuario/Documents/directorio2"]

Ejemplos de TELEGRAM_TOKEN y TELEGRAM_CHAT_ID:
> TELEGRAM_TOKEN = "2992375568:AAFLcEQwSt6sX0g4gF4OZ_ssF47cXyeSedY"

> TELEGRAM_CHAT_ID = "1203935632"

Para crear un bot de Telegram y obtener el TOKEN y el CHAT_ID puede seguir el siguiente enlace: https://core.telegram.org/bots#6-botfather

O seguir el vídeo: https://www.youtube.com/watch?v=Qg5BaKTW1Uw
