class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

# define all rooms
vor_der_burg = Room("Vor der Burg",
    "Vor dir ragt eine alte trutzige Burg auf, das Ziel deiner tagelangen "
    "Reise durch die Wälder von Mordag. Im Norden führt eine herabgelassene "
    "Zugbrücke zu einem düsteren Burghof. Es ist still hier. Sehr still.")
burghof = Room("Der Burghof",
    "Die hohen Mauern lassen nur weg Licht der untergehenden Sonne hinein. "
    "Der Hof ist unübersichtlich. Im Laufe der Jahrhunderte hat sich hier "
    "viel Schutt und Müll angesammelt. Doch im Westen führt ein Tor in den "
    "Burgfried. Alle anderen Zugänge scheinen verschüttet zu sein.")
burgfried = Room("Der Burgfried",
    "Hier ist es richtig dunkel. Wie praktisch wäre jetzt ein Licht. Nach "
    "einige Treppen kommt ein kleiner Raum, in dem es entsetzlich stinkt. "
    "Wäre die restliche Treppe nicht eingestürzt, ginge es hier zum Dach.")

# all directions
directions = ("norden", "osten", "süden", "westen", "oben", "unten")

# connect rooms
vor_der_burg.exits["norden"] = burghof
burghof.exits["süden"] = vor_der_burg
burghof.exits["westen"] = burgfried
burgfried.exits["osten"] = burghof

# the current room
current_room = None

def enter_room(room):
    global current_room
    current_room = room
    describe_room()

def describe_room():
    emit()
    emit(current_room.name); emit()
    emit(current_room.description); emit()


def emit(s="", width=80):
    column = 0
    for word in str(s).split():
        column += len(word) + 1
        if column > width:
            column = len(word) + 1
            print()
        print(word, end=" ")
    print()

def play():
    enter_room(vor_der_burg)
    while execute_command():
        pass

def execute_command():
    words = read_command()
    if words:
        if words[0] in ("gehe", "geh"):
            if len(words) > 2 and words[1] == "nach":
                execute_go(words[2])
            elif len(words) > 1:
                execute_go(words[1])
            else:
                emit("Wohin soll ich gehen?")
        elif words[0] in directions:
            execute_go(words[0])
        elif words[0] in ("schaue", "schau", "beschreibung"):
            describe_room()
        elif words[0] == "ende":
            return False
        else:
            emit("Ich verstehe '%s' nicht." % "".join(words))
    return True

def read_command():
    return [word.lower() for word in input("? ").rstrip(".?!").split()]

def execute_go(direction):
    room = current_room.exits.get(direction)
    if room:
        enter_room(room)
    else:
        emit("Du kannst nicht nach '%s' gehen." % direction)

play()