class Robot:
    def __init__(self, name, make, weight, height, strength, intelligence):
        #battery level, name, make, weight, height, strength, intelligence
        print("this is the init function running!")
        self.name = name
        self.make = make
        self.weight = weight
        self.height = height
        self.strength = strength
        self.intelligence = intelligence
        self.battery_level = 100

    def run_command(self,command):
        if(self.battery_level < 5):
            print(f"{self.name} is a little tired. please recharge")
        else:
            print(f"{self.name} is now running the {command} command")
            self.battery_level -= 5

bob = Robot("Bob","Mercedes",3000,7,5,3)
# hal = Robot("Hal","supercomputer",5000,1000,3,100)

# print(bob.name)
# print(bob.strength)
print(bob.battery_level)
bob.run_command("drive")
for i in range(20):
    bob.run_command("drive")
print(bob.battery_level)
# print(hal.name)