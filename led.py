
import time
import board
import pwmio
from analogio import AnalogIn

pot = AnalogIn(board.A1)
led = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
maxs = 65535

while True:
            led.duty_cycle = pot.value

