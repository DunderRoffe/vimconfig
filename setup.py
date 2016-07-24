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

    parser = argparse.ArgumentParser(description='Tool for managing the vimconfig.')
    parser.add_argument('command', choices=[INIT, UPDATE],
                        help='Which what command to execute')

    args = parser.parse_args()
    if args.command == INIT:
        init()
    elif args.command == UPDATE:
        update()


def init():
    """
    Installs dependencies and initializes the vimconf
    """

    update()

    this_dir = os.path.dirname(os.path.abspath(__file__))
    home_dir, _  = os.path.split(this_dir)
    vimrc_home   = os.path.join(home_dir, ".vimrc")
    vimrc_global = os.path.join(this_dir, "runtime-config", "vimrc-global")
    vimrc_local  = os.path.join(this_dir, "runtime-config", "vimrc-local")

    copyfile(vimrc_home, vimrc_home + ".bak")

    try:
        with open(vimrc_home, mode="w") as f:
            f.write("source {}\n".format(vimrc_global))
            f.write("source {}\n".format(vimrc_local))
    except Exception as e:
        raise Exception("Could not write load config to file '{}'".format(vimrc_home), e)

    try:
        with open(vimrc_local, mode="w") as f:
            f.write('" Put computer specific vim setting in this file\n')
            f.write('" Note that any settings set in this file overrides settings set in the global config\n')
    except Exception as e:
        raise Exception("Could create '{}'".format(vimrc_home), e)


def update():
    """
    Update the vimconf to the latest upstream version
    """

    if os.system("git pull -r origin master") != 0:
       raise Exception("Could not pull from origin master to local master")
    
    if os.system("git submodule update --init --recursive") != 0:
       raise Exception("Something went wrong when updating the vim plugins (git submodules)")


if __name__ == "__main__":
    try:
        parseArgs()
        print("Success :D")
    except Exception as e:
        print(str(e))
