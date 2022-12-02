
from command_console import CallCommands
        
def main():
    obj = input('Digite seu comando: ')
    CallCommands(obj)
    if obj != "stop":
        main()
main()