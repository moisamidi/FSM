import random
import queue

class FSM:
    def __init__(self):
        """
        Initializes the FSM

        Attributes:
        - energy (int): energy level of the FSM.
        - money (int): amount of money for day
        - satiety (int): satiety level of the FSM.
        - my_queue (Queue): queue
        - time (int): current time
        """
        self.energy = 100
        self.money = 200
        self.satiety = 100
        self.my_queue = queue.Queue(24)
        self.time = 0
    
    def start(self):
        """
        Starts the FSM
        """
        self.sleep()


    def messages(self, exception):
        """
        Generates random messages

        Args:
        - exception (int): the exception number to avoid generating a particular message

        """
        rand = random.randint(1, 10)
        if rand != exception and not self.my_queue.full():
            if rand == 1 and self.time > 6:
                print('-----There is too much dirt in the room! I need to clean.')
                self.clean()
            elif rand == 2:
                print("-----Friends suggest playing... I can't refuse.")
                self.play()
            elif rand == 3 and self.time > 4:
                print("-----THERE IS A NEW TASK!!! I NEED TO STUDY.")
                self.study()
            elif rand == 4:
                print("------My friends suggest going to Palylna.")
                self.coffee_cigarettes()

    def sleep(self):
        """
        Simulates the sleeping
        """
        self.energy = 100
        while not self.my_queue.full():
            print(f'{self.time}:00 - sleeping')
            print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
            self.my_queue.put("sleeping")
            self.satiety -= 2
            self.time += 1
            if self.time == 6:
                self.clean()
            self.messages(4)


    def clean(self):
        """
        Simulates the cleaning state
        """
        self.energy -= 30
        self.satiety -= 5
        while not self.my_queue.full():
            print(f'{self.time}:00 - cleaning')
            print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
            self.my_queue.put("cleaning")
            self.time += 1
            if self.time == 11 or random.random() > 0.4:
                self.study()
            if self.time == 14 or self.time == 19:
                if random.random() > 0.5:
                    self.eat()
                else:
                    self.rollerskating()

    def eat(self):
        """
        Simulates the eating state
        """
        self.energy -= 30
        self.satiety += 20
        while not self.my_queue.full():
            if random.random() > 0.7 and self.time > 19:
                print(f'{self.time}:00 - eating at home')
                print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
                self.my_queue.put("eating")
                self.time += 1
                self.messages(0)
                self.study()
            else:
                print(f'{self.time}:00 - took delivery')
                self.money -= 30
                self.time += 1
                print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
                self.my_queue.put("eating")
                self.messages(0)
                self.coffee_cigarettes()

    def study(self):
        """
        Simulates the studying state
        """
        while not self.my_queue.full():
            print(f'{self.time}:00 - studying')
            print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
            self.my_queue.put("studying")
            self.energy -= 5
            self.satiety -= 4
            self.time += 1
            self.messages(3)
            if self.time == 16 and random.random() > 0.8:
                self.rollerskating()
            if self.time == 20:
                self.play()

    def coffee_cigarettes(self):
        """
        Simulates the coffee_cigarettes state
        (wonderful time on Palylna)
        """
        is_cigarettes = random.choice([True, False])
        self.money -= 25
        self.energy += 30
        while not self.my_queue.full():
            if not is_cigarettes:
                print('-----Ohhhhh, firstly, need to buy cigarettes')
                self.money -= 10
            print(f'{self.time}:00 - chilling on palylna')
            print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
            self.my_queue.put("chilling")
            self.time += 1
            self.messages(4)
            self.study()

    def play(self):
        """
        Simulates the playing state
        """
        while not self.my_queue.full():
            print(f'{self.time}:00 - playing csgo')
            print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
            self.my_queue.put("playing")
            self.time += 1
            if self.time == 23:
                self.sleep()
            if self.time == 21 and random.random() > 0.8:
                self.study()
            if random.random() > 0.08:
                self.messages(2)
                self.eat()

    def rollerskating(self):
        """
        Simulates the rollerskating state
        """
        weather = random.choice([True, False])
        while not self.my_queue.full():
            if weather:
                print(f'{self.time}:00 - rollerskating')
                print(f'\nENERGY={self.energy}\nSATIETY={self.satiety}\nMONEY={self.money}\n')
                self.my_queue.put("rollerskating")
                self.time += 1
                if self.time == 23:
                    self.sleep()
                if self.time == 21 and random.random() > 0.5:
                    self.messages(4)
                    self.study()
            else:
                print('There is bad weather for rollerskating -> I go play csgo')
                self.play()

def main():
    """
    The main function
    """
    day = FSM()
    print('\n------schedule in details------\n')
    day.start()
    print('\n------just schedule------\n')
    time = 0
    while not day.my_queue.empty():
        print(f'{time}:00 - {day.my_queue.get()}')
        time += 1

if __name__ == "__main__":
    main()


