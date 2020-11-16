Safe Input: Take that, idiot user!
# Enquire
A Python module to enquire user input safely.

# About
Whenever you ask a user for specific input, there is a good chance he/she messes it up.  
```
Enter a number between 1 and 5: SePhEn  
>>> Traceback (most recent call last):  
>>>   File "<project>", line 99, in <module>  
>>> ValueError: invalid literal for int() with base 10: 'SePhEn'  
>>>   
```
_Hey dude, your program doesn't work. I thought you were a hacker._  
So you have to make sure that no input can crash your code.  
With each project I pursued one of two policies:
1. re-invent the wheel
2. don't give a crap

And with each project I thought: Wouldn't it be clever to have something reusable? 
Well, here we are.

Enquire keeps asking for input until the user gets it right. 
## What it's for
Use Enquire when user input is limited to specific values, like choosing options or entering an integer.
## What it's not for
- Input without validation
- Input for further processing
# Requirements
Python 3.6+

# Installation
Copy the file `enquire.py` to an appropriate folder.

# Usage
Enquire is used quite like `input` with extra steps:
- Ask for a number with `Enquire.number()`. Returns an integer.
- Ask for a string with `Enquire.letter()`. Returns a lowercase string.
- Add specification about allowed numbers / letters.
- Add a default value returned upon empty entry.

Input is non-case-sensitive.  
Returned strings are always lowercase.
## Examples
```
from enquire import Enquire

enq = Enquire()

# a number within limits
number_from_user = enq.number("Enter a number between 1 and 5: ", allowed="1_5")

# a number within limits and with a default return value
number_from_user = enq.number("Enter 1-10, default is 5: ", allowed="1_10", default=5)

# a letter from a specific set
letter_from_user = enq.letter("Enter one of these: W T F: ", allowed="w,t,f")

# one out of a set of options
option_from_user = enq.letter("Type (Play|Pause|Skip|Quit): ", allowed="play,pause,skip,quit")
```
## Specification
Add string parameter `allowed` to specify allowed input.  
Specifications are non-case-sensitive.
### Specify Range
Specify a range of numbers or consecutive letters by a string of lower and upper limits, separated by an underscore.  
Default is `allowed="0_9"` for numbers and `allowed="a_z"` for letters.
### Specify Set 
Define a set of valid entries by comma separated values inside a string.  
Example for numbers: `allowed="2,4,6,8"`  
Example for letters: `allowed="a,b,x,y"`  
Example for options: `allowed="option1, option2, option3"`
# Well
I just figured out that there's a thing called PyPI with a truckload of professional grade modules for safe input.  
Well, this is mine.  
Keep coding!