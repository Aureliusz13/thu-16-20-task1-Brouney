

import random
import time
class Car:
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.speed = 0
        self.distance = 0.
        self.time = 0
    def act(self,event,angl):
        event.run(angl)

class turn_left:
    def run(self,angl):
        angl.angle -= random.randint(0,20)
        #print("turn left, current angle: "+str(angl.angle))
        angl.time += 1
        angl.distance +=  angl.speed

class turn_right:
    def run(self,angl):
        angl.angle += random.randint(0,20)
        #print("turn right,current angle: "+str(angl.angle))
        angl.time += 1
        angl.distance +=  angl.speed

class up_speed:
      def run(self,angl):
            angl.speed += random.randint(0,20)    
            #print("speed up: current speed: "+str(angl.speed))
            angl.time += 1
            angl.distance +=  angl.speed

class down_speed:
      def run(self,angl):
            angl.speed -= random.randint(0,20)
            #print("speed down: current speed: "+str(angl.speed))
            angl.time += 1
            angl.distance +=  angl.speed


left = turn_left()
right = turn_right()
up = up_speed()
down = down_speed()
car1 = Car()
temp = [left,right,up,down]
print("if you want to stop, press : ctrl + c ")
while True:
    #run= int(input("press 1 to run/ 0 to stop: "))
    
    active = random.randint(0,3)
    car1.act(temp[active],car1)
    print("speed: "+str(car1.speed)+"m/s angle: "+str(car1.angle)+ " distance: "+str(car1.distance))
    time.sleep(1)



