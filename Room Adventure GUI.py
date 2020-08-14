###########################################################################]
# Name: Parsa Jahanlou
# Date: Due July 28th, 2020
# Description: Room Adventure
###########################################################################

# Room Adventure GUI

# Importing tkinter
from tkinter import *

# the blueprint for a room
class Room(object):
        # the constructor
        def __init__(self, name,image):
                # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
                # items (e.g., table), item descriptions (for each item), and grabbables (things that can
                # be taken into inventory)
                self.name = name
                self.image = image
                self.exits = {}
                self.items = {}
                self.grabbables = []
                self.descriptions = {}

        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value

        @property
        def image(self):
                return self._image

        @image.setter
        def image(self, value):
                self._image = value

        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value

        @property
        def descriptions(self):
                return self._descriptions

        @descriptions.setter
        def descriptions(self, value):
                self._descriptions = value

        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value

        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate dictionary
                self._exits[exit] = room

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addDescription(self, description, room):
                # append the description and room to the appropriate dictionary
                self._descriptions[room] = description

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate dictionary
                self._items[item] = desc

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                count = 1
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items.keys():
                    s += "\n {} - ".format(count) + item + ""
                    count += 1
                s += "\n"

                # next, the descriptions for the room
                s += "You can go to: "
                for description in self.descriptions.keys():
                    s += description + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits.keys():
                        s += exit + " "
                return s

# the game class
# inherits from the frame class of tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)

    # creates the rooms
    def createRooms(self):
        # r1 through r9 are the nine rooms in the zelda world
        # currentRoom is the room the player is currently in (which can
        # be one of r1 through r9)
        # since it needs to be changed in the main part of the program,
        # it must be global
        global currentRoom
        # create the rooms and give them meaningful names
        r0 = Room("The Start Page", "Start.gif")
        r1 = Room("Rito Village", "Ritovillage.gif")
        r2 = Room("Korok Forest", "KorokForest.gif")
        r3 = Room("Goron City", "GoronCity.gif")
        r4 = Room("Hyrule Ridge", "HyruleRidge.gif")
        r5 = Room("Hyrule Castle", "HyruleCastle.gif")
        r6 = Room("Zora's Domain", "ZoraDomain.gif")
        r7 = Room("Gerudo Town", "GerudoTown.gif")
        r8 = Room("Lake Hylia", "LakeHylia.gif")
        r9 = Room("Hateno Village", "HatenoVillage.gif")
        # letting the player to get to the first room
        r0.addExit("world", r1)
        # add exits to room 1
        r1.addExit("east", r2)  # -> to the east of room 1 is room 2
        r1.addExit("south", r4)
        r1.addExit("north", None)
        r1.addExit("west", None)
        # add descriptions to room 1
        r1.addDescription(r1, "\n 1 - East leads to Korok Forest\n 2 - South leads to Hyrule Ridge")
        # add grabbables to room 1
        r1.addGrabbable("great_eagle_bow")
        # add items to room 1
        r1.addItem("akh_vaquot_shrine", "It is made of stone and surprisingly no one is there.")
        r1.addItem("kaneli_nest", "It is made of hard wood. Great_Eagle_Bow is essential for beating Ganon.")
        # add exits to room 2
        r2.addExit("west", r1)
        r2.addExit("south", r5)
        r2.addExit("east", r3)
        r2.addExit("north", None)
        # add descriptions to room 2
        r2.addDescription(r2, "\n 1 - South leads to Hyrule Castle\n 2 - West leads to Rito Village"\
                          "\n 3 - East leads to Goron City")
        # add items to room 2
        r2.addItem("keo_ruug_shrine", "You can do puzzles here, but Zelda needs your help ASAP")
        r2.addItem("general_store", "Daz is there as always.")
        # add exits to study room 3
        r3.addExit("south", r6)
        r3.addExit("west", r2)
        r3.addExit("north", None)
        r3.addExit("east", None)
        # add descriptions to room 3
        r3.addDescription(r3, "\n 1 - West leads to Korok Forest\n 2 - South leads to Zora's Domain")
        # add grabbables to room 3
        r3.addGrabbable("goron_spice")
        # add items to room 3
        r3.addItem("stolock_bridge", "Fugo tells to leave him alone.")
        r3.addItem("southern_mine", "There is nothing special about it.")
        r3.addItem("goron_gusto_Shop", "You can get some goron_spice here, but not needed.")
        # add exits to room 4
        r4.addExit("north", r1)
        r4.addExit("south", r7)
        r4.addExit("east", r5)
        r4.addExit("west", None)
        # add descriptions to room 4
        r4.addDescription(r4, "\n 1 - North leads to Rito Village\n 2 - East leads to Hyrule Castle"\
                          "\n 3 - South leads to Gerudo Town")
        # add grabbables to room 4
        r4.addGrabbable("hyrule_herb")
        # add items to room 4
        r4.addItem("ridgeland_tower", "Some hyrule_herb can be obtained here, but are you really going to waste time?.")
        # add exits to room 5
        r5.addExit("north", r2)
        r5.addExit("west", r4)
        r5.addExit("south", r8)
        r5.addExit("east", r6)
        # add descriptions to room 5
        r5.addDescription(r5, "\n 1 - North leads to Korok Forest\n 2 - West leads to Hyrule Ridge"\
                          "\n 3 - South leads to Lake Hylia\n 4 - East leads to Zora's Domain")
        # add grabbables to room 6
        # r5.addGrabbable("None")
        # add items to room 6
        # r5.addItem("None")
        # add exits to Music Room(6)
        r6.addExit("north", r3)
        r6.addExit("west", r5)
        r6.addExit("south", r9)
        r6.addExit("east", None)
        # add descriptions to room 6
        r6.addDescription(r6, "\n 1 - North leads to Goron City\n 2 - West leads to Hyrule Castle"\
                          "\n 3 - South leads to Hateno Village")
        # add grabbables to room 6
        r6.addGrabbable("lightscale_trident")
        # add items to room 6
        r6.addItem("coral_reef", "Dento has built your lightscale_trident")
        r6.addItem("toto_lake", "Swimming sounds nice, but what about Zelda")
        # add exits to room 7
        r7.addExit("north", r4)
        r7.addExit("east", r8)
        r7.addExit("west", None)
        r7.addExit("south", None)
        # add descriptions to room 7
        r7.addDescription(r7, "\n 1 - North leads to Hyrule Ridge\n 2 - East leads to Lake Hylia")
        # add grabbables to room 7
        r7.addGrabbable("topaz_earrings")
        # add items to room 7
        r7.addItem("jewelry_shop", "topaz_earrings are on sale, but Zelda is suffering and you wanna look pretty?")
        # add exits to room 8
        r8.addExit("north", r5)
        r8.addExit("west", r7)
        r8.addExit("south", None)
        r8.addExit("east", r9)
        # add descriptions to room 8
        r8.addDescription(r8, "\n 1 - North leads to Hyrule Castle\n 2 - West leads to Gerudo Town"\
                          "\n 3 - East leads to Hateno Village")
        # add grabbables to room 8
        r8.addGrabbable("farosh_scale")
        # add items to room 8
        r8.addItem("giant_dragon", "You can get a farosh_scale, but why waste time?")
        # add exits to room 9
        r9.addExit("north", r6)
        r9.addExit("west", r8)
        r9.addExit("south", None)
        r9.addExit("east", None)
        # add descriptions to room 1
        r9.addDescription(r9, "\n 1 - North leads to Zora's Domain\n 2 - West leads to Lake Hylia")
        # add grabbables to room 9
        r9.addGrabbable("soldier_armor")
        # add items to room 9
        r9.addItem("armor_shop", "Sophie is offering you soldier_armor for free!")
        r9.addItem("your_house", "I know you want to sleep, but Zelda is waiting for you.")

        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = r0

        # initialize the player's inventory
        Game.inventory = []

    # sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)

        # setup the player at the bottom of GUI
        # the widget is a tkinter entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doest have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a tkinter label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=400, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a tkinter text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    # set the current room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="skull.gif")

        # displaying the right image for when the player wins with all the right grabbles
        # and is also in the right room
        elif ((Game.inventory == ["great_eagle_bow", "lightscale_trident", "soldier_armor"]) and (Game.currentRoom.name == "Hyrule Castle")):
            Game.img = PhotoImage(file="Ganon.gif")

        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the gui
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now is quit")

        # displaying the right text for when the player wins with all the right grabbles
        # and is also in the right room
        elif ((Game.inventory == ["great_eagle_bow", "lightscale_trident", "soldier_armor"]) and\
               (Game.currentRoom.name == "Hyrule Castle")):
            Game.text.insert(END, "You have saved Zelda from Ganon. Congratulations on winning the game!")

        # text for the starting page
        elif (Game.currentRoom.name == "The Start Page"):
            Game.text.insert(END, "This is the starting page of this game \n" + "\nIf you have ever played the latest Zelda game, then use that knowledge in this game to win." +
                   "\n\nHint: Every not described direction goes off the map, so do not go there ;)" +
                   "\n\nType \"Go World\" to start the game\n" )

        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
                         "\nYou are carrying: " + str(Game.inventory) +\
                         "\n\n" + status)
        Game.text.config(state=DISABLED)

    # play the game
    def play(self):
        # add the rooms to the game
        self.createRooms()
        # configure the GUI
        self.setupGUI()
        # set the current room
        self.setRoomImage()
        # set the current status
        self.setStatus("")

    # processes the player's input
    def process(self, event):
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to
        # compare the verb and noun to known values
        action = action.lower()
        # set a default response

        response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

        # exit the game if the player wants to leave (supports quit,
        # exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
            exit(0)
            
        # if the player is dead if goes off the map
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return

        # clearing the player's input for when the player wins with all the right grabbles
        # and is also in the right room
        if ((Game.inventory == ["great_eagle_bow", "lightscale_trident", "soldier_armor"]) and\
               (Game.currentRoom.name == "Hyrule Castle")):
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by
        # spaces) and store the words in a list
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."

                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    # if one is found, change the current room to
                    # the one that is associated with the
                    # specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    # set the response (success)
                    response = "Room changed."

            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # if one is found, set the response to the
                    # item's description
                    response = Game.currentRoom.items[noun]

            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item."

                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the
                        # room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable
                        # items
                        break

        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

###########################################
######## The Main Part of the Game ########
###########################################

# Determining the height and width
WIDTH = 800
HEIGHT = 600

# Creating the window
window = Tk()

# Title of the window
window.title("Room Adventure")

# Executing the main parts of the game
g = Game(window)
g.play()

# Infinite loop
window.mainloop()