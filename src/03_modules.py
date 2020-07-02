"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv[0]) 
#prints the same way without [0], but only in [], easier for me to see


# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform) 
#darwim 
# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)  # <--- this one? 
"""3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)]"""
print(sys.version_info)
#sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())   # 5066

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())  #√√

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())  #root 
