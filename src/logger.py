import logging
import os
from datetime import datetime

# Nombre del archivo log

LOG_NAME = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"


# Ruta del directorio de logs

log_dir = os.path.join(os.getcwd(), 'logs')

os.makedirs(log_dir,exist_ok=True)


LOG_FILE_PATH = os.path.join(log_dir, LOG_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

if __name__ == '__main__':
    logging.info('Logging ha comenzado')  # Mensaje de log