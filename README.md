# zioLang
My simple programing language.

# updates
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

# commands
## echo
```
echo str Hello.
echo int 1
echo float 1.5
```
## define
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
## delay
```
echo int 1
delay 1
echo int 2
```
## if
```
define random $random{1 9}
define input $inp{}
if random == input
    echo str True!
if random != input
    echo str False!
```
## else
```
define random $random{1 9}
define input $inp{}
if random == input
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