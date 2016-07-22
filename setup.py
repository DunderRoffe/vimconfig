#!/usr/bin/env python
import argparse
import os
from shutil import copyfile


def parseArgs():
    """
    Parses arguments and selects mode
    """

    INIT = "init"
    UPDATE = "update"

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('command', choices=[INIT, UPDATE],
                        help='Which what command to execute')

    args = parser.parse_args()
    if args.command == INIT:
        init()
    elif args.command == UPDATE:
        update()


def init():
    """
    Initializes the vimconf
    """

    if os.system("sudo apt-get install vim gcc g++ cmake python") == 0:
        if os.system("git submodule update --init --recursive") == 0:
            this_dir = os.path.dirname(os.path.abspath(__file__))
            home_dir, _  = os.path.split(this_dir)
            vimrc_home   = os.path.join(home_dir, ".vimrc")
            vimrc_global = os.path.join(this_dir, "runtime-config", "vimrc-global")
            vimrc_local  = os.path.join(this_dir, "runtime-config", "vimrc-local")

            copyfile(vimrc_home, os.path.join(vimrc_home, ".bak"))

            with open(vimrc_home, mode="w") as f:
                f.write("source {}", vimrc_global)
                f.write("source {}", vimrc_local)
        else:
            print("Could not update git submodule, aborting...")
    else:
        print("Could not install required programs via apt-get, aborting...")

def update():
    """
    Update the vimconf to the latest upstream version
    """

    success = os.system("git pull -r origin master && git submodule update --init --recursive")
    if success != 0:
       raise Exception("Something went wrong during update please fix")


if __name__ == "__main__":
    try:
        parseArgs()
    except Exception as e:
        print(str(e))
