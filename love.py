
import math, random
try:
    import pygame
except ImportError:
    print("Missing dependency: pygame. Install it with 'pip install pygame'.")
    raise SystemExit
pygame.init()
W,H=900,700
screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()
font=pygame.font.SysFont("arial",48)

def heart(t):
    x=16*math.sin(t)**3
    y=13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)
    return x*18+W//2,-y*18+H//2-60

targets=[heart(i*0.05) for i in range(int(2*math.pi/0.05))]
parts=[]
for tx,ty in targets:
    sx=random.choice([random.randint(-100,1000),random.choice([-50,H+50])])
    sy=random.choice([random.randint(-100,800),random.choice([-50,H+50])])
    parts.append([sx,sy,tx,ty])

done=False
while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit();raise SystemExit
    screen.fill((0,0,0))
    done=True
    for p in parts:
        x,y,tx,ty=p
        dx=(tx-x)*0.05
        dy=(ty-y)*0.05
        if abs(tx-x)>1 or abs(ty-y)>1:
            done=False
        p[0]+=dx
        p[1]+=dy
        pygame.draw.circle(screen,(255,60,90),(int(p[0]),int(p[1])),2)
    if done:
        txt=font.render("Love You ❤️",True,(255,120,180))
        screen.blit(txt,(W//2-txt.get_width()//2,H-90))
    pygame.display.flip()
    clock.tick(60)
