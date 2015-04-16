from Controller import *
from MLAgent import *
from AI import *
from FMAI import *

import logging

class MyCsvFormatter(logging.Formatter):
    def __init__(self):
        fmt = "%(message)s" # Set a format that uses commas, like the other answers
        super(MyCsvFormatter, self).__init__(fmt=fmt)

logger = logging.getLogger()

formatter = MyCsvFormatter()

handler = logging.FileHandler("test.csv", "w")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

nbWin = 0
for i in xrange(10):
    ai1 = MLAgent()
    ai2 = FMAI(0.5)
    controller = Controller("Americas", "Scrubby", "FM", ai1, ai2)
    winningPlayerIndex = controller.play()

    if winningPlayerIndex == 1:
        nbWin += 1
    logging.debug(str(winningPlayerIndex == 1))
print nbWin