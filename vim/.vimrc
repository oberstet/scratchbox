" :set paste
" http://vim.wikia.com/wiki/Toggle_auto-indenting_for_code_paste

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'

" List your Vundle bundles here:
Plugin 'freeo/vim-kalisi'
Plugin 'bling/vim-airline'
Plugin 'tpope/vim-fugitive'
Plugin 'kien/ctrlp.vim'
Plugin 'klen/python-mode'
Plugin 'davidhalter/jedi-vim'
" Plugin 'ervandew/supertab'

call vundle#end()
filetype plugin indent on

" Put the rest of your config here:

set t_Co=256

colorscheme kalisi
set background=dark

" always show the statusline
set laststatus=2

" http://stackoverflow.com/a/7387750
set path=$PWD/**

" disable the autocompletion from python-mode since we use jedi instead
let g:pymode_rope_vim_completion = 0

" disable vertical red bar at column 80 for pymode
let g:pymode_options_colorcolumn = 0

" disable some pylint checks
let g:pymode_lint_ignore="E501,C901"

" Don't autofold code
" let g:pymode_folding = 0

" http://stackoverflow.com/a/21323445/884770
" Only do this part when compiled with support for autocommands.
if has("autocmd")
    " Use filetype detection and file-based automatic indenting.
    filetype plugin indent on

    " Use actual tab chars in Makefiles.
    autocmd FileType make set tabstop=8 shiftwidth=8 softtabstop=0 noexpandtab
endif

" For everything else, use a tab width of 4 space chars.
set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
                    " Vim will interpret it to be having
                    " a width of 4.
set shiftwidth=4    " Indents will have a width of 4.
set softtabstop=4   " Sets the number of columns for a TAB.
set expandtab       " Expand TABs to spaces.

set foldmethod=indent
set foldlevel=99

" https://github.com/ggreer/the_silver_searcher
" http://codeinthehole.com/writing/using-the-silver-searcher-with-vim/
let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'

