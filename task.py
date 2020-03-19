# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.

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



