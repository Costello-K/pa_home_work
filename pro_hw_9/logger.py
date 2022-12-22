import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-25s %(filename)-25s %(lineno)-3d %(levelname)-8s %(message)s')

filehandler = logging.FileHandler(f'logger.log')
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)
