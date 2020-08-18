###########################################################################################
# Name: Parsa Jahanlou and Leandro Lopes Jose Londin
# Date: Due June 23rd, 2020
# Description: Room Adventure
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
    # the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
        # items (e.g., table), item descriptions (for each item), and grabbables (things that can
        # be taken into inventory)

    # getters and setters for the instance variables
    # ...
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value
    
    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

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
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

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
        #Count the number of elements that the user sees
        count = 1
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see:\n"
        for item in self.items:
            s += "{} - ".format(count) + item + "\n"
            count += 1
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s

###########################################################################################
# creates the rooms
def createRooms():
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r4)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom
    # create the rooms and give them meaningful names
    r1 = Room("Rito Village")
    r2 = Room("Korok Forest")
    r3 = Room("Goron City")
    r4 = Room("Hyrule Ridge")
    r5 = Room("Hyrule Castle")
    r6 = Room("Zora's Domain")
    r7 = Room("Gerudo Town")
    r8 = Room("Lake Hylia")
    r9 = Room("Hateno Village")
    # add exits to living room (1)
    r1.addExit("east", r2) # -> to the east of room 1 is room 2
    r1.addExit("south", r4)
    r1.addExit("north", None)
    r1.addExit("west", None)
    # add grabbables to room 1
    r1.addGrabbable("Great_Eagle_Bow")
    # add items to room 1
    r1.addItem("Akh_Vaquot_Shrine", "It is made of stone and surprisingly no one is there.")
    r1.addItem("Kaneli_Nest", "It is made of hard wood. Great_Eagle_Bow is essential for beating Ganon.")
    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r5)
    r2.addExit("east", r3)
    r2.addExit("north", None)
    # add items to room 2
    r2.addItem("Keo_Ruug_Shrine", "You can do puzzles here, but Zelda needs your help ASAP")
    r2.addItem("General_Store", "Daz is there as always.")
    # add exits to study room 3
    r3.addExit("south", r6)
    r3.addExit("west", r2)
    r3.addExit("north", None)
    r3.addExit("east", None)
    # add grabbables to room 3
    r3.addGrabbable("Goron_Spice")
    # add items to room 3
    r3.addItem("Stolock_Bridge", "Fugo tells to leave him alone.")
    r3.addItem("Southern_Mine", "There is nothing special about it.")
    r3.addItem("Goron_Gusto_Shop", "You can get some Goron_Spice here, but not needed.")
    # add exits to room 4
    r4.addExit("north", r1)
    r4.addExit("south", r7)
    r4.addExit("east", r5)
    r4.addExit("west", None)
    # add grabbables to room 4
    r4.addGrabbable("Hyrule_Herb")
    # add items to room 4
    r4.addItem("Ridgeland_Tower", "Some Hyrule_Herb can be obtained here, but are you really going to waste time?.")
    # add exits to room 5
    r5.addExit("north", r2)
    r5.addExit("west", r4)
    r5.addExit("south", r8)
    r5.addExit("east", r6)
    # add grabbables to room 6
    # r5.addGrabbable("None")
    # add items to room 6
    # r5.addItem("None")
    # add exits to Music Room(6)
    r6.addExit("north", r3)
    r6.addExit("west", r5)
    r6.addExit("south", r9)
    r6.addExit("east", None)
    # add grabbables to room 6
    r6.addGrabbable("Lightscale_Trident")
    # add items to room 6
    r6.addItem("Coral_Reef", "Dento has built your Lightscale_Trident")
    r6.addItem("Toto_Lake", "Swimming sounds nice, but what about Zelda")
    # add exits to room 7
    r7.addExit("north", r4)
    r7.addExit("east", r8)
    r7.addExit("west", None)
    r7.addExit("south", None)
    # add grabbables to room 7
    r7.addGrabbable("Topaz_Earrings")
    # add items to room 7
    r7.addItem("Jewelry_shop", "Topaz_Earrings are on sale, but Zelda is suffering and you wanna look pretty?")
    # add exits to room 8
    r8.addExit("north", r5)
    r8.addExit("west", r7)
    r8.addExit("south", None)
    r8.addExit("east", r9)
    # add grabbables to room 8
    r8.addGrabbable("Farosh_Scale")
    # add items to room 8
    r8.addItem("Giant_Dragon", "You can get a Farosh_Scale, but why waste time?")
    # add exits to room 9
    r9.addExit("north", r6)
    r9.addExit("west", r8)
    r9.addExit("south", None)
    r9.addExit("east", None)
    # add grabbables to room 9
    r9.addGrabbable("Soldier_Armor")
    # add items to room 9
    r9.addItem("Armor_Shop", "Sophie is offering you Soldier_Armor for free!")
    r9.addItem("Your_house", "I know you want to sleep, but Zelda is waiting for you.")
    # set room 1 as the current room at the beginning of the game
    currentRoom = r1

# a funny message for when the player dies
# implies "bye bye"
def death():
  print("▒░░░░░░▄▄▄░░▄██▄░░░")
  print("░░░░░░▐▀█▀▌░░░░▀█▄░")
  print("░░░░░░▐█▄█▌░░░░░░▀█▄")
  print("░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀")
  print("░░░░░▄▄▄██▀▀▀▀░░░░░")
  print("░░░░█▀▄▄▄█░▀▀░░░░░░")
  print("░░░░▌░▄▄▄▐▌▀▀▀░░░░░")
  print("░▄░▐░░░▄▄░█░▀▀░░░░░")
  print("░▀█▌░░░▄░▀█▀░▀░░░░░")
  print("░░░░░░░░▄▄▐▌▄▄░░░░░")
  print("░░░░░░░░▀███▀█░▄░░░")
  print("░░░░░░░▐▌▀▄▀▄▀▐▄░░░")
  print("░░░░░░░▐▀░░░░░░▐▌░░")
  print("░░░░░░░█░░░░░░░░█░░")
  print("░░░░░░▐▌░░░░░░░░░█░")

#Gives the description for each room
def description(room):

    # Description for Room 1
    if(room.name == "Rito Village"):
        print("East leads to Korok Forest")
        print("South leads to Hyrule Ridge")

    # Description for Room 2
    elif(room.name == "Korok Forest"):
        print("South leads to Hyrule Castle")
        print("West leads to Rito Village")
        print("East leads to Goron City")

    # Description for Room 3
    elif(room.name == "Goron City"):
        print("West leads to Korok Forest")
        print("South leads to Zora's Domain")

    # Description for Room 4
    elif(room.name == "Hyrule Ridge"):
        print("North leads to Rito Village")
        print("East leads to Hyrule Castle")
        print("South leads to Gerudo Town")

    # Description for Room 5
    elif(room.name == "Hyrule Castle"):
        print("North leads to Korok Forest")
        print("West leads to Hyrule Ridge")
        print("south leads to Lake Hylia")
        print("East leads to Zora's Domain")
        
    # Description for Room 6
    elif(room.name == "Zora's Domain"):
        print("North leads to Goron City")
        print("West leads to Hyrule Castle")
        print("South leads to Hateno Village")

    # Description for Room 7
    elif(room.name == "Gerudo Town"):
        print("North leads to Hyrule Ridge")
        print("East leads to Lake Hylia")

    # Description for Room 8
    elif(room.name == "Lake Hylia"):
        print("North leads to Hyrule Castle")
        print("West leads to Gerudo Town")
        print("East leads to Hateno Village")

    # Description for Room 9
    elif(room.name == "Hateno Village"):
        print("North leads to Zora's Domain")
        print("West leads to Lake Hylia")
        
# Asking for the player's name in order to make the game more user-friendly
def userName():
    playerName = raw_input("What would you like to be called? ")
    return playerName.capitalize()

# Giving a brief explanation about how you can win in this game
def gameInfo(name):
    print ("=========================================================")
    print("Dear {}, there is a way to win in this game.".format(name))
    print("If you have ever played the latest Zelda game, then use that knowledge in this game.")
    print("Hint: Every not described direction goes off the map, so do not go there ;)")
    print ("=========================================================")

######################################################################
# START THE GAME!!!
######################################################################
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game
name = userName() # getting the player's name
gameInfo(name) # giving the necessary info to the player
# play forever (well, at least until the player dies or asks to quit or wins)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    if(inventory == []):
        status = "Currently, you are not carrying any items.\n{}".format(currentRoom)
    else:
        status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
    # if the current room is None, then the player is dead
    # this only happens if the player goes off the map
    if (currentRoom == None):
        status = "You have died {}.".format(name)
    # players wins if they are in room 5 with the required grabbles and exits the game
    if ((inventory == ["Great_Eagle_Bow", "Lightscale_Trident", "Soldier_Armor"]) and (currentRoom.name == "Hyrule Castle")):
        status = "Congratulations {}, you beat Ganon with all the necessary equipment, and have rescued Zelda!".format(name)
        break
    # display the status
    print ("=========================================================")
    print (status)
    # if the current room is None (and the player is dead), exit the game
    if (currentRoom == None):
        death()
        break
    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    # we use raw_input here to treat the input as a string instead of
    # a numeric value
    # giving a description of different exits for each room
    description(currentRoom)
    action = raw_input("What to do? ")
    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()
    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces)
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
        for i in range(len(currentRoom.exits)):
            # a valid exit is found
            if (noun == currentRoom.exits[i]):
                # change the current room to the one that is
                # associated with the specified exit
                currentRoom = currentRoom.exitLocations[i]

                 # set the response (success)
                response = "Room changed."
                # no need to check any more exits
                break
    # the verb is: look
    elif (verb == "look"):
        # set a default response
        response = "I don't see that item."
        # check for valid items in the current room
        for i in range(len(currentRoom.items)):
            if (noun == currentRoom.items[i].lower()):
                # set the response to the item's description
                response = currentRoom.itemDescriptions[i]
                # no need to check any more items
                break
    # the verb is: take
    elif (verb == "take"):
        # set a default response
        response = "I don't see that item."
        # check for valid grabbable items in the current room
        for grabbable in currentRoom.grabbables:
            # a valid grabbable item is found
            if (noun == grabbable.lower()):
                # add the grabbable item to the player's
                # inventory
                inventory.append(grabbable)
                # remove the grabbable item from the room
                currentRoom.delGrabbable(grabbable)
                # set the response (success)
                response = "Item grabbed."
                # no need to check any more grabbable items
                break
    # display the response
    print ("\n{}".format(response))
# display the status
print ("=========================================================")
print (status)
