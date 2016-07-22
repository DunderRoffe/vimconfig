About
=====
This is my vim config setup. It uses git submodules manage vim plugins.
Feel free to copy or fork if you find this appealing :)

Install
=======

Prerequisites
-------------
* vim
* git
* python

Procedure
---------
Clone this repo in to your home folder and rename it to '.vim'
```bash
git clone https://github.com/DunderRoffe/vimconfig.git ~/.vim
```

Run setup script
```bash
cd .vim && ./setup.py init && cd -
```

Maintain
========

Local settings
--------------
Add computer specific settings to the file ~/.vim/runtime-config/vimrc-local.
This file is automatically loaded by the ~/.vimrc file but ignored by git.
```bash
vim ~/.vim/runtime-config/vimrc-local
```

Global settings
---------------
Inorder to assure that the changes are managed by git,
all global vim config that normaly is put in ~/.vimrc should be
put in ~/.vim/runtime-config/vimrc-global
```bash
vim ~/.vim/runtime-config/vimrc-global
```

License
=======
See license file
