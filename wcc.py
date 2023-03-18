"""Windows Command Center"""
#NAME - Windows Command Center
#AUTHOR - Otas02CZ
#DATE - 18.3.2023
#INFO - Simple (probably useless) python script for managing simple tasks in Windows OS

from subprocess import call
from enum import Enum
from rich import print as rprint
from rich.console import Console
from rich.prompt import IntPrompt
from os import system

class WindowsCommandCenter:
    
    class COMMANDS(Enum):
        SFC_CHECK=0,
        DISM_CHECK=1,
        EXIT=2
    
    class COMMAND:
        name: str
        command: str
        
        def __init__(self, name: str, command: str) -> None:
            self.name = name
            self.command = command
       
    COMMAND_LIST : dict[COMMAND] = {
        0: COMMAND("SFC scannow check", "sfc /SCANNOW"),
        1: COMMAND("dism online check", "dism /Online /Cleanup-Image /CheckHealth"),
        2: COMMAND("Exit the utility", ""),
    }
    
    def showCommandMenu(self):
        rprint("[bold red]Command List[/bold red]")
        rprint("[bold white]KEY\t- NAME OF THE COMMAND\t- COMMAND ITSELF[/bold white]")
        for key, command in self.COMMAND_LIST.items():
            rprint(f"[bold yellow]{key}[/bold yellow]\t- [bold blue]{command.name}[/bold blue]\t- [bold green]{command.command}[/bold green]")
    
    def getExecuteCommand(self) -> bool:
        choice : int = IntPrompt.ask(prompt="Insert command", choices=["0", "1", "2"], show_choices=True)
        if choice == self.COMMANDS.EXIT.value:
            return False
        else:
            call(self.COMMAND_LIST[choice].command , shell=True)
            return True

def main():
    wcc : WindowsCommandCenter = WindowsCommandCenter()
    console : Console = Console()
    while True:
        system("cls")
        wcc.showCommandMenu()
        if not wcc.getExecuteCommand():
            break
        console.input("[bold yellow]Press enter to continue[/bold yellow]")
    
if __name__ == "__main__":
    main()