#import statistics
import sys
\
#print(statistics.mean([100, 90]))
if len(sys.argv) < 1:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("Hello, my name is", sys.argv[1])


