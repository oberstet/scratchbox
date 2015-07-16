# VIM

* https://github.com/tpope/vim-pathogen
* https://github.com/freeo/vim-kalisi
* https://github.com/bling/vim-airline

* http://www.sontek.net/blog/2011/05/07/turning_vim_into_a_modern_python_ide.html
* https://wiki.python.org/moin/Vim
* http://blog.dispatched.ch/2009/05/24/vim-as-python-ide/
* http://docs.python-guide.org/en/latest/dev/env/

https://github.com/chriskempson/tomorrow-theme
http://unlogic.co.uk/2013/02/08/vim-as-a-python-ide/



<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>S</kbd> for horizontal splitting

<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>V</kbd> for vertical splitting

<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>Q</kbd> to close one

<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>W</kbd> to switch between windows

<kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>J</kbd> (xor <kbd>K</kbd>, <kbd>H</kbd>, <kbd>L</kbd>) to switch to adjacent window (intuitively up, down, left, right)

```
:Explore **/*.txt
```

## Moving

```
h   move one character left
j   move one row down
k   move one row up
l   move one character right
w   move to beginning of next word
b   move to beginning of previous word
e   move to end of word
W   move to beginning of next word after a whitespace
B   move to beginning of previous word before a whitespace
E   move to end of word before a whitespace

0   move to beginning of line
$   move to end of line
^   move to first non-blank char of the line
_   same as above, but can take a count to go to a different line
g_  move to last non-blank char of the line (can also take a count as above)

gg  move to first line
G   move to last line
nG  move to n'th line of file (where n is a number)

H   move to top of screen
M   move to middle of screen
L   move to bottom of screen

z.  put the line with the cursor at the center
zt  put the line with the cursor at the top
zb  put the line with the cursor at the bottom of the screen

Ctrl-D  move half-page down
Ctrl-U  move half-page up
Ctrl-B  page up
Ctrl-F  page down
Ctrl-o  jump to last cursor position
Ctrl-i  jump to next cursor position

n   next matching search pattern
N   previous matching search pattern
*   next word under cursor
#   previous word under cursor
g*  next matching search pattern under cursor
g#  previous matching search pattern under cursor

%   jump to matching bracket { } [ ] ( )
```

## Copy and Paste

```
Cut and paste:

Position the cursor where you want to begin cutting.
Press v to select characters (or uppercase V to select whole lines).
Move the cursor to the end of what you want to cut.
Press d to cut (or y to copy).
Move to where you would like to paste.
Press P to paste before the cursor, or p to paste after.
Copy and paste is performed with the same steps except for step 4 where you would press y instead of d:

d = delete = cut
y = yank = copy
```
