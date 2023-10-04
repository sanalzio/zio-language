import sys
import os
import importlib
from random import randint
os.chdir(os.path.dirname(os.path.abspath(__file__)))
lastelse=None
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        cmd = line.strip().split(" ")
        lineindex=lines.index(line)
        # ---------- Keys ---------- #
        if cmd[0] == "define":
            var=" ".join(cmd[2:])
            vari=None
            varrand=None
            if "$random{" in var:
                ints=var.replace("$random{", "").replace("}", "").split(" ")
                int1=int(ints[0])
                int2=int(ints[1])
                if "." in ints[0]:
                    int1=int(float(ints[0]))
                if "." in ints[1]:
                    int2=int(float(ints[1]))
                varrand=randint(int1, int2)
            if "$inp{" in var:
                vari=input(var.replace("$inp{", "").replace("}", ""))
            for i in range(len(lines)):
                if "$random{" in var:
                    lines[i] = lines[i].replace("${"+cmd[1]+"}", str(varrand))
                if "$inp{" in var:
                    lines[i] = lines[i].replace("${"+cmd[1]+"}", vari)
                lines[i] = lines[i].replace("${"+cmd[1]+"}", var)
        if "$[" in line:
            for i in range(len(cmd)):
                this = cmd[i]
                if "$[" in this:
                    ana=this.replace("$[", "").replace("]", "")
                    if "/" in ana:
                        ints=ana.split("/")
                        int1=ints[0]
                        int2=ints[1]
                        sonuc=None
                        if "." in int1:
                            int1=float(ints[0])
                        else:
                            int1=int(ints[0])
                        if "." in int2:
                            int2=float(ints[1])
                        else:
                            int2=int(ints[1])
                        sonuc=int1/int2
                        cmd[i]=str(sonuc)
                    if "*" in ana:
                        ints=ana.split("*")
                        int1=ints[0]
                        int2=ints[1]
                        sonuc=None
                        if "." in int1:
                            int1=float(ints[0])
                        else:
                            int1=int(ints[0])
                        if "." in int2:
                            int2=float(ints[1])
                        else:
                            int2=int(ints[1])
                        sonuc=int1*int2
                        cmd[i]=str(sonuc)
                    if "+" in ana:
                        ints=ana.split("+")
                        int1=ints[0]
                        int2=ints[1]
                        sonuc=None
                        if "." in int1:
                            int1=float(ints[0])
                        else:
                            int1=int(ints[0])
                        if "." in int2:
                            int2=float(ints[1])
                        else:
                            int2=int(ints[1])
                        sonuc=int1+int2
                        cmd[i]=str(sonuc)
                    if "-" in ana:
                        ints=ana.split("-")
                        int1=ints[0]
                        int2=ints[1]
                        sonuc=None
                        if "." in int1:
                            int1=float(ints[0])
                        else:
                            int1=int(ints[0])
                        if "." in int2:
                            int2=float(ints[1])
                        else:
                            int2=int(ints[1])
                        sonuc=int1-int2
                        cmd[i]=str(sonuc)
                    lines[lines.index(line)]=" ".join(cmd)
        if cmd[0] == "if":
            if cmd[2] == "==":
                if cmd[1] == cmd[3]:
                    lines[lineindex]=" ".join(cmd[4:])
                    lastelse=False
                else:
                    lines.pop(lineindex)
                    lastelse=True
            if cmd[2] == "!=":
                if not cmd[1] == cmd[3]:
                    lines[lineindex]=" ".join(cmd[4:])
                    lastelse=False
                else:
                    lines.pop(lineindex)
                    lastelse=True
        if cmd[0] == "else":
            if lastelse==True:
                lines[lineindex]=" ".join(cmd[1:])
            else:
                lines.pop(lineindex)
        if cmd[0]=="uselib":
            libs=[]
            with open("liblist.zi", "r") as f:
                lib_lines = f.readlines()
                for lib in lib_lines:
                    libs.append(lib.replace("\n", ""))
                import urllib.request
                setup_url = f"https://raw.githubusercontent.com/{cmd[1]}/setup.zi"
                with urllib.request.urlopen(setup_url) as response:
                    breaked=False
                    data = response.read().decode()
                    lib_lines=data.split("\n")
                    for lin in lib_lines:
                        if breaked==True:
                            break
                        larg=lin.split(" ")
                        if len(larg)<2:
                            continue
                        filename=larg[1].rstrip('\r')
                        if larg[0] == "lib":
                            thislib=f"{larg[1]} {larg[2]}".strip()
                            if thislib in libs:
                                breaked=True
                                break
                            else:
                                libs.append(f"{larg[1]} {larg[2]}")
                        if larg[0] == "func":
                            with urllib.request.urlopen(f"https://raw.githubusercontent.com/{cmd[1]}/functions/{filename}") as responsem:
                                with open("functions/"+filename, "w") as f:
                                    f.write(responsem.read().decode())
                        if larg[0] == "key":
                            with urllib.request.urlopen(f"https://raw.githubusercontent.com/{cmd[1]}/keys/{filename}") as responsem:
                                with open("keys/"+filename, "w") as f:
                                    f.write(responsem.read().decode())
                        if larg[0] == "custom":
                            with urllib.request.urlopen(f"https://raw.githubusercontent.com/{cmd[1]}/{filename}") as responsems:
                                with open(filename, "w") as f:
                                    f.write(responsems.read().decode())
                    if breaked==False:
                        with open("liblist.zi", "w") as f:
                            f.write("\n".join(libs))
        # Custom Keys
        direc = "keys"
        dire = os.listdir(os.path.join(os.getcwd(), direc))
        for f in set(dire):
            if f.endswith(".py"):
                filel = f.replace(".py", "")
                module_name = f"{direc}.{filel}"
                m = importlib.import_module(module_name)
                if m.key == cmd[0]:
                    m.run(lines, line, cmd)
        # ---------- Keys ---------- #
        # -------- Functions ------- #
        # Custom Keys
        direc = "functions"
        dire = os.listdir(os.path.join(os.getcwd(), direc))
        for f in set(dire):
            if f.endswith(".py"):
                filel = f.replace(".py", "")
                module_name = f"{direc}.{filel}"
                m = importlib.import_module(module_name)
                if m.cmd == cmd[0]:
                    m.run(lines, line, cmd)
        # -------- Functions ------- #
