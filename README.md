About
=====
These are my personal vim preferences which I originally forked
from my friend [Simon Pedersen's repo](https://bitbucket.org/mustig/vimconfig).

Feel free to copy or fork them if you find them appealing :)

INSTALL
=======
Install required programs
```bash
sudo apt-get install git
```

Clone this repo in to your home folder and rename it to '.vim'
```bash
git clone git@bitbucket.org:roffe/vimconfig.git ~/.vim
```

Run setup script
```bash
cd .vim && ./setup.sh && cd -
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
