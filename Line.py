#!/usr/bin/env python3

import Screen

## Produces weird lines with some coordinates, needs revision

def drawLine(screen, a, b, color):
    # Swap points a and b if a is to the right of b.
    # Only have to deal with octants I, II, VII, and VIII as a result
    if(b[0] < a[0]):
        # Swapping values without a third variable
        # Possibility for overflow errors
        b[0] = b[0] + a[0]
        a[0] = b[0] - a[0]
        b[0] = b[0] - a[0]
        
        b[1] = b[1] + a[1]
        a[1] = b[1] - a[1]
        b[1] = b[1] - a[1]
        
    # Plot point b
    # This has to be plotted anyway
    Screen.plot(screen, b[0], b[1], color)

    x = a[0]
    y = a[1]
            
    B = -1 * (b[0] - a[0])
    
    if a[1] >= b[1]:
        #Octant I, II
        A = a[1] - b[1]
        if A >= (-1 * B):
            #Octant II
            d = A + (2 * B)
            while(y > b[1]):
                Screen.plot(screen, x, y, color)
                if(d < 0):
                    x = x + 1
                    d = d + A
                y = y - 1
                d = d + B
        else:
            #Octant I
            d = (2 * A) + B
            while(x < b[0]):
                Screen.plot(screen, x, y, color)
                if(d > 0):
                    y = y - 1
                    d = d + B
                x = x + 1
                d = d + A
    else:
        #Octant VII, VIII
        A = a[1] - b[1]
        if A >= B:
            #Octant VIII
            d = (2 * A) - B
            while(x < b[0]):
                Screen.plot(screen, x, y, color)
                if(d < 0):
                    y = y + 1
                    d = d - B
                x = x + 1
                d = d + A
        else:
            #Octant VII
            d = A - (2 * B)
            while(y < b[1]):
                Screen.plot(screen, x, y, color)
                if(d > 0):
                    x = x + 1
                    d = d + A
                y = y + 1
                d = d - B
    Screen.plot(screen, b[0], b[1], color)
