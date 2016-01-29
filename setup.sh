#!/bin/bash

sudo apt-get install vim gcc g++ cmake python python-dev

# Initialize the vim plugins:
git submodule update --init --recursive --remote 

# Make .vim settings load
echo "source ~/.vim/runtime-config/vimrc-global" > ~/.vimrc
cat ~/.vimrc >> ~/.vim/runtime-config/vimrc-local
echo "source ~/.vim/runtime-config/vimrc-local" > ~/.vimrc

# YouCompleteMe compilation
cd bundle/YouCompleteMe/
./install.py
cd -

echo "All done!"
