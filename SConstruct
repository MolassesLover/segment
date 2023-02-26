#!/bin/scons

import colorama
import sys

sys.path.append("src/python")

import build_pack
from build_pack import *
from colorama import Fore

match __name__:
    case "__main__":
        print(f":: Running as a {Fore.YELLOW}Python{Fore.RESET} script.")
        build()
    case "SCons.Script":
        print(f":: Running as a {Fore.YELLOW}SCons{Fore.RESET} script.")
        build()
    case "SConstruct":
        f":: {Fore.RED}Error{Fore.RESET}: The {Fore.YELLOW}SConstruct{Fore.RESET} file should not be used as a module."
        sys.exit(1)
    case _:
        f":: {Fore.RED}Error{Fore.RESET}: The {Fore.YELLOW}SConstruct{Fore.RESET} script seems to have been used abnormally, exiting..."
        sys.exit(1)
