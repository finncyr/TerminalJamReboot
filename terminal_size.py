import os
from platform import system

term_columns,term_lines = os.get_terminal_size()

print(system())

