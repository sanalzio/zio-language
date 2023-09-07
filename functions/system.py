cmd="system"
import os
def run(lines, line, cmd):
    os.system(" ".join(cmd[1:]))
