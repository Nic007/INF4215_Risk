from AI import AI
from Controller import *
from RandomAI import RandomAI
from MLAgent import MLAgent

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

ai1 = AI()
#ai1 = RandomAI()
ai2 = MLAgent()

for i in xrange(0, 100000):
    controller = Controller("Americas", "Pedro", "Scrubby", ai1, ai2)
    controller.play()
    logging.debug(str(ai2.HasWon()))

print "NB Of victories " + str(ai2.GetNbVictories())