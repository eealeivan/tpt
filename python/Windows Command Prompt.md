
# Windows Command Prompt

Command Prompt (cmd) is program that helps you to work with operating system. It is rarely used by normal users but it is an everyday tool for software developers. To open cmd click on Start Menu and type *cmd*. Run application which is named Command Prompt *Desktop app*.

When cmd is open you will see the black window with some text. The bottom text will look something like that (actual text may vary):
```
C:\Users\Harry>
```

This is your current location in file system.  It is somewhat similar to File Explorer because you always have a location. You can do a lot of things with cmd but we will mostly use it for navigation in file system and running the code we write.

## Commands

### dir

Displays the contents of current directory.
```
C:\Users\Harry>dir
```

Sample output (shrinked):
```
04.10.2018  22:10 <DIR>   Documents
29.09.2018  01:25     236 hello.py
```

Here we have one directory named *Documents* and one file *hello.py*

### cd

With this command you can navigate to other directories. Use the directory names that you see in `dir` output.
```
C:\Users\Harry>cd Documents
```

After running this command your location will be changed to:
```
C:\Users\Harry\Documents>
```

To navigate to parent directory (back) use `..`
```
C:\Users\Harry>cd ..
```

### Up/Down key

You can switch to previously entered commands, which means that you don’t need to type a command every time from scratch.

### cls

Cleans contents of command prompt window.
```
C:\Users\Harry>cls
```

## Running Python Program

First you need to navigate to directory where your python file is located. Use `cd` and `dir` commands for that. Then if you can see your python file in `dir` output, then run the following command (of course you will have your own path and python file name, this is just an example):
```
C:\Users\Harry\Documents>python hello.py
```











