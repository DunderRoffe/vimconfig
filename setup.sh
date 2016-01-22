#!/bin/bash

sudo apt-get install vim gcc g++ cmake python python-dev

# Initialize the vim plugins:
git submodule update --init --recursive --remote 

# Add the following to the top of ~/.vimrc
echo "\n\n\" Old conf:" >> ~/.vim/runtime-config/vimrc-global
cat ~/.vimrc >> ~/.vim/runtime-config/vimrc-global
echo "source ~/.vim/runtime-config/vimrc-global" > ~/.vimrc

# YouCompleteMe compilation
cd bundle/YouCompleteMe/
./install.py
cd -

echo "All done!"
