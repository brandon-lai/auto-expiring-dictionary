from datetime import timedelta
import time;
from __init__ import AutoDict

dict = AutoDict(timedelta(0, 5, 0))
dict[4] = 3
print(dict[4])
time.sleep(5)
print(dict[4])