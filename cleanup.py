import os
# Clears terminal window via os commands, checks operating system to make
# sure which command is kosher
def cleanup():

    os.system('cls' if os.name == 'nt' else 'clear')

