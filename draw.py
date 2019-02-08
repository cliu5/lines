from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0!=x1:
        slope = (y1-y0)/(x1-x0)
        # Octant 1 & 5
        if slope>=0 and slope <=1:
            if x0<x1:
                octant_one(x0,y0,x1,y1,screen,color)
            octant_one(x1,y1,x0,y0,screen,color)
        # Octant 2 & 6
        elif slope>1:
            if x0<x1:
                octant_two(x0,y0,x1,y1,screen,color)
            octant_two(x1,y1,x0,y0,screen,color)
        # Octant 8 & 4
        elif slope<=0 and slope >=-1:
            if x0<x1:
                octant_eight(x0,y0,x1,y1,screen,color)
            octant_eight(x1,y1,x0,y0,screen,color)
        # Octant 7 & 3
        elif slope<=-1:
            if x0<x1:
                octant_seven(x0,y0,x1,y1,screen,color)
            octant_seven(x1,y1,x0,y0,screen,color)
    else:
        undefined(x0,y0,x1,y1,screen,color)
def undefined(x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    if y0<y1:
        while y<y1:
            plot(screen,color,x,y)
            y+=1
    else:
        while y>y1:
            plot(screen,color,x,y)
            y-=1
    pass
    
def octant_one(x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    a=(y1-y0)
    b=-1*(x1-x0)
    d=2*a+b
    while x<=x1:
        plot(screen,color,x,y)
        if d>0:
            y+=1
            d+=2*b
        x+=1
        d+=2*a
    pass

def octant_two(x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    a=(y1-y0)
    b=-1*(x1-x0)
    d=2*b+a
    while y<=y1:
        plot(screen,color,x,y)
        if d<0:
            x+=1
            d+=2*a
        y+=1
        d+=2*b
    pass

def octant_eight(x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    a=(y1-y0)
    b=-1*(x1-x0)
    d=2*a+b
    while x<=x1:
        plot(screen,color,x,y)
        if d<0:
            y-=1
            d-=2*b
        x+=1
        d+=2*a
    pass

def octant_seven(x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    a=(y1-y0)
    b=-1*(x1-x0)
    d=a-2*b
    while y>=y1:
        plot(screen,color,x,y)
        if d>0:
            x+=1
            d+=2*a
        y-=1
        d-=2*b
    pass
            


    
