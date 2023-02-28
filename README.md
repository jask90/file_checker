# file_checker


# Configuración del proyecto

En el fichero settings.py se configura la siguiente información:
* TELEGRAM_TOKEN -> Token del bot de Telegram
* TELEGRAM_CHAT_ID -> ID del chat al que se envían los mensajes de Telegram
* MAIN_DIRS -> Lista de directorios principales. Se controlarán lo ficheros de todos estos directorios y de los que haya dentro.

Ejemplo de MAIN_DIRS, dónde se indican 2 directorios a controlar, separados por comas:
> MAIN_DIRS = ["/Users/danielfraga/Documents/directorio1", /Users/danielfraga/Documents/directorio2"]
