from Controller import *
from AI import *
from RandomAI import RandomAI
from MLAgent import MLAgent

#ai1 = AI()
ai1 = RandomAI()
ai2 = MLAgent()
controller = Controller("Americas", "Pedro", "Scrubby", ai1, ai2)
controller.play()