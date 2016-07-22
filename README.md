About
=====
These are my personal vim preferences which I originally forked
from my friend [Simon Pedersen's repo](https://bitbucket.org/mustig/vimconfig).

Feel free to copy or fork if you find this appealing :)

Install
=======
Clone this repo in to your home folder and rename it to '.vim'
```bash
git clone https://roffe@bitbucket.org/roffe/vimconfig.git ~/.vim
```

Run setup script
```bash
cd .vim && ./setup.py init && cd -
```

Maintain
========

Local settings
--------------
Add local settings to the file ~/.vim/runtime-config/vimrc-local.
This file is automatically loaded by the ~/.vimrc file. However,
it is ignored by the git repository.
```bash
vim ~/.vim/runtime-config/vimrc-local
```

Updating global vim config
--------------------------
Inorder to assure that the changes are managed by git,
all global vim config that normaly is put in ~/.vimrc should be
put in ~/.vim/runtime-config/vimrc-globali
```bash
vim ~/.vim/runtime-config/vimrc-global
```

License
=======
See license file
