from __future__ import print_function
import psutil

# Verify the memory usage before the test
print(psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage
print('memory % used:', psutil.virtual_memory()[2])