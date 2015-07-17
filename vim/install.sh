#!/bin/sh

mkdir -p ~/.vim
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
ln -s ~/scm/scratchbox/vim/.vimrc ~/.vimrc
vim +PluginInstall +qall
git config --global core.editor "vim"
