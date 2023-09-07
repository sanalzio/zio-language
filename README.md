# myLang
My simple programing language.

# usage
```
cd "myLang folder" example: "C:\Users\User\Desktop\myLang\myLang"
.\myLang "file path" example: "C:\Users\User\Desktop\myLang\example.my"
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
## system
```
system color a
echo str Color is green!
```
## quit
```
quit
```
