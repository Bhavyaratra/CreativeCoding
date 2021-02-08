import pygame, math

pygame.init()
window=pygame.display.set_mode((600,600))
pygame.display.set_caption("Fractal Tree")
screen=pygame.display.get_surface()

def drawTree(x1,y1,angle,depth):
    angleV=20
    if(depth>0):
        x2=x1+ int(math.cos(math.radians(angle))*10*depth)
        y2=y1+ int(math.sin(math.radians(angle))*10*depth)
        pygame.draw.line(screen,(255,255,255),(x1,y1),(x2,y2),2)
        drawTree(x2,y2,angle-angleV,depth-1)
        drawTree(x2,y2,angle+angleV,depth-1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)



drawTree(300,600,-90,9)
pygame.display.update()
while True:
    input(pygame.event.wait())