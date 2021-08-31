from vpython import *
#GlowScript 3.0 VPython

scene.width=950
scene.height=700
scene.background=vector(0.5, 0.5, 0.5)
scene.caption=("Click 's' to drop the ball")
scene.append_to_caption("\n Click 'q' to end the game")
scene.append_to_caption("\nUse Right Arrow to move right.")
scene.append_to_caption("\nUse Left Arrow to move left")
player=[]
player.append(arrow(pos = vector(0,-1.1,0),axis=vector(0,0.4,0), shaftwidth = 0.05, color = vector(255,255,255)))
player.append(sphere(pos = vector(0,-0.7,0), radius = 0.06, color = vector(255,255,255)))
eggdropper=box(pos=vector(0,1,0),color=color.red,size=vector(2,0.1,0.1))
v = vec(0,0,0)
dv = 0.1
dt = 0.01
score=0
def egg(evt):
    global score=0
    if evt.key=="s":
        r=random()*2
        r=(r-1)/2
        egg=sphere(pos=vector(r,1,0),color=color.green,radius=0.03)
        egg.velocity=vector(0,-1,0)
        delt=0.03
        while True:
            rate(20)
            egg.pos = egg.pos+egg.velocity*delt
            sub=egg.pos.y-player[1].pos.y
            sub2=egg.pos.x-player[1].pos.x
            if egg.pos.y<-1.3:
                egg.visible=False
            else if sub<0.1 and sub>-0.1 and sub2<0.1 and sub2>-0.1: 
                egg.visible=False
                score+=1
                print(score)
                break
    else if evt.key=="q":
        print ("End of Game")
        print("Your final score is :",score)

while True:
    rate(30)
    k = keysdown() # a list of keys that are down
    runn = scene.bind('keydown',egg)
    a=keysdown()
    if 'left' in a: v.x -= dv
    if 'right' in a: v.x += dv
    player[0].pos += v*dt
    player[1].pos+=v*dt
    if player[0].pos.x>1.5 or player[0].pos.x<-1.5:
        player[0].pos=vec(0,-1.1,0)
        player[1].pos=vec(0,-0.7,0)