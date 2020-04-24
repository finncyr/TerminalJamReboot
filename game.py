from os import system as sys_cmd
from os import get_terminal_size
from platform import system

term_col, term_lin = get_terminal_size()
current_desc = None

class Game_Window:
    def __init__(self, columns, lines):
        self.columns = columns
        self.lines = lines

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

class Descision:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.options = {}
    
    def showOptions(self):
        for option in self.options:
            print(option, ': ', self.options.get(option), sep='')

# Function to clear screen
def clear():
    if system() in ["Linux", "Darwin"]:
        sys_cmd('clear')
    if system() == "Windows":
        sys_cmd('cls')

# Function to emit words based on Terminal size
def emit(s="", width=term_col):
    column = 0
    for word in str(s).split():
        column += len(word) + 1
        if column > width:
            column = len(word) + 1
            print()
        print(word, end=" ")
    print()


# Input "?" Prompt
def read_command():
    return [word.lower() for word in input("? ").rstrip(".?!").split()]

#TODO: Execcute Go Function
def execute_go(direc)

def interprete_answer(answer):
    if answer:
        if answer[0] == "go":
            execute_go(answer[1])
        elif answer[0] == "execute":
            execute_sy(answer[0])
        elif answer[0] == ("show"):
            describe_room()
        elif answer[0] == "end":
            return False
        else:
            emit("Ich verstehe '%s' nicht." % "".join(words))
    return True


def execute_input():
    answer = read_command()
    if answer (int) in current_desc.options:
        status = interprete_answer(answer)
        if status = False:
            return False
    else:
        emit("Please select a valid option!")



# All Rooms that are in the game

starting_room = Room("Starting Room",
        "This is an example description for a Room!")
    
# All Descisions that are in the Game

demo_desc = Descision("Demo-Descision", "This is context information for the descision")
demo_desc.options[1] = "wanna play this game?"
demo_desc.solutions[1] = "go room1"
demo_desc.options[2] = "nah, lets quit"
demo_desc.solutions[2] = "end"
demo_desc.options[3] = "Clear this screen"
demo_desc.solutions[3] = "execute clear"




def play():
    emit()
    emit(demo_desc.name); emit()
    emit(demo_desc.description); emit()
    demo_desc.showOptions()
    emit()
    execute_input()


play()