from display import *
from draw import *
import math

screen = new_screen()
#color = [ 0, 255, 0 ]
f=open('img.ppm','w')
f.write('P3 500 500 255 ')


def draw_box(center,s,color):
    h=int(math.floor(s*(3**.5)/2))
    l=int(s/2)
    draw_line(center,center,center-h, center+l,screen,color)
    draw_line(center-h,center+l, center-h, center-l,screen,color)
    draw_line(center-h,center-l,center,center-s,screen,color)
    draw_line(center,center,center+h,center+l,screen,color)
    draw_line(center+h,center+l,center+h,center-l,screen,color)
    draw_line(center+h,center-l,center,center-s,screen,color)
    #Lines of slope=undefined
    draw_line(center,center,center,center-s,screen,color)
    draw_line(center-h,center+l,center,center+s,screen,color)
    draw_line(center,center+s,center+h,center+l,screen,color)
    draw_line(0,center,500,center,screen,color)
    #Lines of slope=0
    draw_line(0,center+100,500,center+100,screen,color)
    draw_line(0,center+200,500,center+200,screen,color)
    draw_line(0,center-100,500,center-100,screen,color)
    draw_line(0,center-200,500,center-200,screen,color)


j=10
while j<500:
    draw_box(200,j,[255,0,0])
    j+=20

i=20
while i<500: 
    draw_box(250,i,[0,255,0])
    i+=20

g=30
while g<500:
    draw_box(300,g,[255, 0,255])
    g+=40

print('img.png')
display(screen)
save_extension(screen, 'img.png')
