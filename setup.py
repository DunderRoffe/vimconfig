#!/usr/bin/env python
import argparse
import os
from shutil import copyfile


def parseArgs():
    """
    Parses arguments and selects mode
    """

    INIT = "init"
    CHECK_UPDATE = "check_update"
    UPDATE = "update"

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('command', choices=[INIT, CHECK_UPDATE, UPDATE],
                        help='Which what command to execute')

    args = parser.parse_args()
    if args.command == INIT:
        init()
    elif args.command == CHECK_UPDATE:
        new_version_exists = check_update()
        if new_version_exists:
            ask_update()
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

def check_update():
    """
    Check if there is an avaliable update from the upstream git repo
    """

    pull_ok = os.system("git pull -r origin master")
    return False

def ask_update():
    """
    Ask if the vimconf should be updated to the latest version
    """

    print("New version found!")
    answer = input("Do you want to update?(Y/n): ")
    if not answer.to_lower() == "n":
        update()

def update():
    """
    Update the vimconf to the latest upstream version
    """

    os.system("git pull -r origin master && git submodule update --init --recursive")


if __name__ == "__main__":
    parseArgs()


