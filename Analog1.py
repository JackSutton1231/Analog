#import
import board
from analogio import AnalogIn
from neopixel import NeoPixel
import time

np = NeoPixel(board.D2,30,auto_write=False,brightness=.4)
pot = AnalogIn(board.A1)

maximun = 65535
minimum = .1
rng = .45

def chase1(color):
    count = 0
    for i in range(np.n):
        np.fill(color)
        for i in range(np.n):
            if (i + count) % 3 == 0:
                np[i] = (0,0,0)
        np.show()
        move = pot.value / maximun * rng + minimum
        time.sleep(move)

        count = (count + 1) % 3

        
while True:
        chase1((255,0,0))

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
