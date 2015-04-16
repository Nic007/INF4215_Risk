from Controller import *
from MLAgent import *

import logging

class MyCsvFormatter(logging.Formatter):
    def __init__(self):
        fmt = "%(message)s" # Set a format that uses commas, like the other answers
        super(MyCsvFormatter, self).__init__(fmt=fmt)

logger = logging.getLogger()

formatter = MyCsvFormatter()

handler = logging.FileHandler("results.csv", "w")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

nbWin = 0
for i in xrange(100):
    ai1 = RandomAI()
    ai2 = MLAgent()
    controller = Controller("Americas", "HerpDerp", "Scrubby", ai1, ai2)
    winningPlayerIndex = controller.play()

    if winningPlayerIndex == 0:
        nbWin += 1
    logging.debug(str(winningPlayerIndex == 1))

print nbWin