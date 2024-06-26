# multi-val-dict
A multi-value dictionary

This is a command line program written in Python.
It stores a multi-value dictionary in memory. All keys and members are strings. It can treat inputs "in quotes" as one string.

### Commands
It supports the following commands:

- KEYS, MEMBERS, ADD, REMOVE, REMOVEALL, CLEAR, KEYEXISTS, MEMBEREXISTS, ALLMEMBERS, and ITEMS

In addition, I have added support for:
- HELP -- Lists all supported commands
- QUIT -- Exits the program and prints out the final results of the dictionary

Further information can be found in the Documentation folder. 

### Running
The commands in this section are intended for a **Linux-based system**. I use the Linux subsystem for Windows. 

Make sure your version of Python is updated to **Python 3.10**. You may run into interpretation errors if you attempt to run the program with an earlier version.

To begin, clone a copy of this repo to your machine:
```
git clone https://github.com/sdvgallardo/multi-val-dict.git
```
Move to the folder you just cloned:
```
cd multi-val-dict
```
Then, execute the program by running it with Python 3:
```
python3 mvd.py
```
Then enter your desired commands, adding members to the multi-value dictionary and manipulating it as desired.

When finished, enter `QUIT` at the prompt, your final dictionary will be provided and the program will cease operation. Any members entered in the dictionary will be lost. 

### Testing
A file of tests has been included.

To run tests, make sure Pytest has been installed:
```
pip3 install pytest
```
Then execute the tests by running them with Pytest:
```
pytest tests.py
```
There are 11 tests written with a total of 25 assertions, testing various pieces of the multi-value dictionary program.


