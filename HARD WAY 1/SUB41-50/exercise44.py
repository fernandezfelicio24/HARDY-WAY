from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Thisk scens is not yet configured")
        print("Subclass it and implement enter().")
        exit(1)
class Engine(object):

    def __int__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a luser",
        "I have a small pupy that's better at this."
        "You're worse than your Dad's jokes."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent(
            """
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your las mission is to get the neutron destruct
            bomb from the Weapins Armory, put it in the bridge, and 
            blow the ship up after getting into an escape pod.
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, end evil clown costume flowing around his hate
            filled body. He's blocing the door to the Armory and 
            about to pull a weapon to blast you.
            """
        ))

        action = input("> ")

        if action == "shoot!":
            print(dedent(
                """
                Quick on the draw you yank out your blaster and fire 
                it at the Gothon. His clown costume is flowing and 
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother  
                bought him, which make him fly into an insane rage 
                and blast you repeatedly in the face until you are
                dead. Then he eats you.
                """
            ))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                  Like a world class boxer you dodge, weave, slip and
                  slide right as the Gothon's blaster crancks a laser
                  past your head. In the middle of your artfull dodge
                  yout foot slips and you bang your head on the metal
                  wall and pass out. You wake up shortly after only to
                  die as the Gothon stomps on your head and eats you.
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent(
                    """
                    Lucky for your they made your learn Gothon insults in
                    the academy. You tell the one Gothon joke you know:
                    Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                    fur fvgf nebhaq gur ubhfr. The Gothon stops, tries 
                    not to laugh, the busts out laughing and can't move.
                    While he's laughing you run up and shoot him square in 
                    the head putting him down, the jump through the 
                    Weapon Armory door.
                    """))

            return 'death'
        elif action == "tell a joke":
            print(dedent(
                """
                Lucky for you they made you learn Gothin insult in
                the academy. You tell the onr Gothon joke you know:
                Lbhe zbgure vf fb sng. jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops. tries
                not to lugh, then busts out laughing and can't move.
                While he's laughing you run ip and shoot him square in
                the head putting him down, the jump through the 
                Weapon Armoru door.
                """
            ))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return  'central_corridor'
class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
                You do a dive roll into the Weapon Armory, crouch and scan
                the room for more Gothons that might be hidding. It's dead
                quite, too quiet. You stand up and run to the far side of 
                the room and find the neutron bomb in its container/
                There's a keypad loc on the box and you need the code to
                geti the bomb out. If you get the code wrong 10 time then
                the lock closes forever and you can't get the bomb. The
                code is 3 digits.
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZEDDD!")
            guesses += 1
            guess = input()

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the 
                right spot. 
            """))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
                You burst onto the Bridege with the netron destruct bomb
                under your arm and suprise 5 Gothons who are trying to
                take control of the ship. Each of them has an even uglier
                clown costume than the last. They haven't pulled their 
                weapons out yet, as they see the active bomb under your
                arm and don't want to set it off.
        """))
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                    In a panic you throw the bomb at the group of Gothons
                    and make a leap for the door. Right as you drop it a 
                    Gothon shoots you right in the back killing you. As
                    you dire you see anothe Gothon frantically try to
                    disarm the bomb. You die knowing they will probably
                    blow up when it goes off
            """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                the Gothond put their hand up an start to sweat.
                You inch backward to the door, open it, and then
                careffuly place the bomb on the floor, pointing your 
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the 
                Gothins can't get out. Now that the bomb is placed
                you run to the escape pod to get off this thin can.
            """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE !")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass
    def next_scane(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()