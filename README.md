About
=====
These are my personal vim preferences which I originally forked
from my friend [Simon Pedersen's repo](https://bitbucket.org/mustig/vimconfig).

Feel free to copy or fork them if you find them appealing :)

INSTALL
=======
Install required programs
```bash
sudo apt-get install vim git cmake python python-dev
```

Clone this repo in to your home folder and rename it to '.vim'
```bash
git clone git@bitbucket.org:roffe/vimconfig.git ~/.vim
```

Add the following to the top of ~/.vimrc
```bash
echo "\n\n\" Old conf:" >> ~/vim/runtime-config/vimrc-global
cat ~/.vimrc >> ~/.vim/runtime-config/vimrc-global
echo "source ~/.vim/runtime-config/vimrc-global" > ~/.vimrc
```

Initialize the vim plugins:
```bash
git submodule init
```

YouCompleteMe compilation
```bash
cd ~/.vim/bundle/YouCompleteMe/ && ./install.sh && cd -
```

Maintain
========

Updating vim config
---------------
Inorder to assure that the changes are managed by git,
all vim config that normaly is put in ~/.vimrc should be
put in an appropriate file in /path-to-repo/runtime-config/

Update Plugins
--------------
```bash
git submodule update --recursive --remote
```