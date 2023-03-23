# Welcome to Python My Classes!
Python my classes (pymc) is a Python cli that creates python files with classes!

## [Download the whl file here]()
---
## How does it work?
First, create a pymc.yaml file with the command:
```
pymc init
```
>This will create a file in your cwd called pymc.yaml

It will look something like this:
```
ClassName:
  _var1: null
  _var2: null
```

This file is you configuration file, it serves as a hub for all your classes.

The **ClassName** in this exemple will serve as the name of the file and the name of the class, and the **vars** will be the variable names.
>Variables that start with underscores will get their own getter/setters

--- 
Now, build the classes and files with the *build* command:
```
pymc build
```
And you are done!
You can add  new classes to the pymc.yaml file and build again if need be!



