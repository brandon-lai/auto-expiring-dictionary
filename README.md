# auto-expiring-dictionary
Data structure written in Python that handles auto-expiring keys.

Given a specific time to live, a key is no longer valid (inaccessible) once the duration has exceeded the time limit from the time of creation. All data associated with invalidated keys is automatically removed to reduce memory usage.

## Though Process Questions
### What specific problems or difficulties did you encounter?
I had never created a data structure in Python, so many of the difficulties I encountered were related to figuring out how to implement Python classes and working out the nuances of the time module.

### Would you have done anything differently?
I would have liked to handle the error more gracefully and elegantly so that the program does not stop, but for now, the user has to handle the error manually.

### Why did you pick this language?
Python appeared to be the natual choice for this kind of data structure because it natively has a dictionary data structure and time module. 

### Would a different language have worked better?
A low level language such as C or C++ could allow for better performance by allowing low-level manipulation of hardware and more finite control over memory.

## Usage
### Add this code block at top of file
```
from datetime import timedelta
import time;
from __init__ import AutoDict
```
