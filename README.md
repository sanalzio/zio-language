# zioLang
My simple programing language.

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)  ![Version](https://img.shields.io/static/v1?label=Version&message=1.0&style=for-the-badge&labelColor=222831&color=393E46) ![Python Version](https://img.shields.io/static/v1?label=Version&message=3.x&style=for-the-badge&labelColor=4B8BBE&color=FFE873&logo=python&logoColor=ffffff) ![LICENSE](https://img.shields.io/static/v1?label=LICENSE&message=MIT&style=for-the-badge) [<img alt="downloadbtn" src="https://dabuttonfactory.com/button.png?t=Download&f=Ubuntu-Bold&ts=30&tc=fff&hp=15&vp=15&c=6&bgt=unicolored&bgc=238636&bs=4&bc=37914a" width="77px">](https://github.com/sanalzio/zio-language/releases/download/zioLang/zio.7z)

![ZioLang](logos/repoimage/ziolang.svg)

# updates
- **Added custom keys system in keys/ folder** [Go!](#keys)
- **Added else key** <a href="#else">Go!</a>
- **Added uselib key** <a href="#uselib">Go!</a>
- **Added library system** <a href="#library-system">Go!</a>
- Changed project name to **zioLang**

# usage
**just open .zi file with zio.exe**
or use:
```
cd "zio folder" example: "C:\Users\User\Desktop\myLang\myLang"
.\zio.exe "file path" example: "C:\Users\User\Desktop\myLang\example.zi"
```

# keys
**Keys are executed before functions, allowing keywords like 'if' and 'else' to work smoothly.**
## define
```
define var 123
echo int ${var}
```
## if
```
define random $random{1 9}
define input $inp{}
if ${random} == ${input}
    echo str True!
if ${random} != ${input}
    echo str False!
```
## else
```
define random $random{1 9}
define input $inp{}
if ${random} == ${input}
    echo str True!
else
    echo str False!
```
## uselib
```
uselib sanalzio/examplelib-zio/master
system color a
echo str Green color!
```
**Create custom library** <a href="#library-system"> Go!</a>

# variable types
## default
```
define var 123
echo int ${var}
```
## input
```
define var $inp{Give input: }
echo str Your input is: ${var}
```
## random
```
define var $random{1 9}
echo str Your random integer is: ${var}
```

# functions
## echo
```
echo str Hello.
echo int 1
echo float 1.5
```
## delay
```
echo int 1
delay 1
echo int 2
```
## system
```
system color a
echo str Color is green!
```
## quit
```
quit
```

# Library system
**[Example ZIO language library repository Go!](https://github.com/sanalzio/examplelib-zio/)**
