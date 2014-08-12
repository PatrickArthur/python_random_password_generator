#### By importing the random and string module in Python,
#### you can generate randome passwords using this


import random
import string
password = ''.join(random.choice(string.ascii_uppercase + string.digits)
  for x in range(10))
print password
