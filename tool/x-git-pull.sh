#!/bin/bash

find . -mindepth 1 -maxdepth 1 -type d -exec bash -c "cd {}; echo; echo; pwd; echo '------------------------------------------------------------------'; git pull; cd .." \;
