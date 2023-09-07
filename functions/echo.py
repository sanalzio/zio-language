cmd="echo"
def run(lines, line, cmd):
    if cmd[1] == "str":
        print(str(" ".join(cmd[2:])))
    if cmd[1] == "float":
        try:
            print(float(cmd[2]))
        except:
            print(float(int(cmd[2])))
    if cmd[1] == "int":
        try:
            print(int(cmd[2]))
        except:
            print(int(float(cmd[2])))
