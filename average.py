#import statistics
import sys
\
#print(statistics.mean([100, 90]))
if len(sys.argv) < 1:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, my name is", arg)


