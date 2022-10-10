#!/usr/bin/python3
import sys
import os

options = {
    "Detach all sessions": lambda: os.system("tmux detach-client -a; tmux detach-client")
}

if len(sys.argv) < 2:
    os.system("tmux ls")
    for option in options.keys():
        print(option)
else:
    if sys.argv[-1] in options:
        options[sys.argv[-1]]()
    else:
        id = sys.argv[-1].split(":")[0]
        os.system(f"coproc mate-terminal -e 'tmux attach-session -t {id}'")