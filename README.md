# file_checker


# Configuración del proyecto

En el fichero settings.py se configura la siguiente información:
* TELEGRAM_TOKEN -> Token del bot de Telegram
* TELEGRAM_CHAT_ID -> ID del chat al que se envían los mensajes de Telegram
* MAIN_DIRS -> Lista de directorios principales. Se controlarán lo ficheros de todos estos directorios y de los que haya dentro.

Ejemplo de MAIN_DIRS, dónde se indican 2 directorios a controlar, separados por comas:
> MAIN_DIRS = ["/Users/usuario/Documents/directorio1", /Users/usuario/Documents/directorio2"]

Ejemplos de TELEGRAM_TOKEN y TELEGRAM_CHAT_ID:
> TELEGRAM_TOKEN = "2992375568:AAFLcEQwSt6sX0g4gF4OZ_ssF47cXyeSedY"

> TELEGRAM_CHAT_ID = "1203935632"

Para crear un bot de Telegram y obtener el TOKEN y el CHAT_ID puede seguir el siguiente enlace: https://core.telegram.org/bots#6-botfather

O seguir el vídeo: https://www.youtube.com/watch?v=Qg5BaKTW1Uw
