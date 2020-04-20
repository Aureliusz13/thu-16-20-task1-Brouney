import random
import time


class Car:
    def __init__(self, events = []):
        self.angle = 0
        self.speed = 0
        self.distance = 0.
        self.time = 0
        self.events = events
        self.log_file = None

    def act(self,event):
        event.run(self)

    def open_log_file(self, filename="Output.txt"):
        self.log_file = open(filename, "w")

    def close_log_file(self):
        if self.log_file is not None:
            self.log_file.close()
            close_success = True
        else:
            close_success = False
        return close_success

    def log_status(self):
        self.log_file.write(
            "speed: {} m/s angle: {} distance: {} \n".format(str(self.speed), str(self.angle),
                                                             str(self.distance)))

    def run_loop(self, loops=-1):
        self.open_log_file()
        if len(self.events):
            while loops:
                active = random.randint(0, len(self.events)-1)
                self.act(self.events[active])
                self.log_status()
                time.sleep(1)
                loops -= 1
            self.close_log_file()
            return True
        else:
            self.log_file.write("No events to proceed on with")
            self.close_log_file()
            return False


class TurnLeft:
    def run(self,angl):
        angl.angle -= random.randint(0,20)
        angl.time += 1
        angl.distance +=  angl.speed


class TurnRight:
    def run(self,angl):
        angl.angle += random.randint(0,20)
        angl.time += 1
        angl.distance +=  angl.speed


class SpeedUp:
      def run(self,angl):
            angl.speed += random.randint(0,20)
            angl.time += 1
            angl.distance +=  angl.speed


class SpeedDown:
      def run(self,angl):
            angl.speed -= random.randint(0,20)
            angl.time += 1
            angl.distance +=  angl.speed


if __name__ == "__main__":
    events = [TurnLeft(), TurnRight(), SpeedUp(), SpeedDown()]
    car = Car(events)
    print("if you want to stop, press : ctrl + c ")
    car.run_loop(10)