
myfloat = 7.0
print(myfloat)

myfloat = float(7)
print(myfloat)


mystring = 'Hello'
print(mystring)
mystring = "Hello"
print(mystring)



mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "Hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


a, b, c = 3, 4, 5
print(a,b, c)

one = 1
two = 2
hello = "hello"

print(one + two )

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])



for x in mylist:
    print(x)
    


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


# Arithmetic operators
numbers = 1 + 2 * 3 / 4.0
print(numbers)

# remainder - modulo operator
remainder = 11 % 3
print(remainder)

#Using two multiplication symbols makes a power relationship
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#concatinating strings
hwlloworld = "hello" + " " + "world"
print(helloworld)

#multiplying strings
lotsofhellos = "hello " * 10
print(lotsofhellos)

#using operators with lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
allnumbers = odd_numbers + even_numbers
print(allnumbers)

#forming new lists with a repeating sequence
print([1, 2, 3] * 3)


#Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list constains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#booleans 
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# "and" and "or" boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# "in" operator checks is a specified object exists within an interable object container
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")


# loops in python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#for loop can interate a sequence of numbers using "range" and "xrange" functions
#prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)


#prints out 3,4,5
for x in range(3, 6):
    print(x)

#prints out 3,5,7

for x in range(3, 8, 2):
    print(x)

#while loop repeats as long as a certain boolean condition is met
count = 0
while count < 5:
    print(count)
    count += 1
    

# "break" and "continue" statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break



#prints only the odd numbers 
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

# use of "else" clause for loops
count = 0
while (count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % count)
    


for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


#Exercise
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)

#Functions
def my_function():
    print("Hello from my function")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))
    
def sum_two_numbers(a, b):
    return a + b


#How to call functions in python
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1, 2)
print(x)

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(2000)


def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return benefit + " is a benefit of functions"

def name_the_beneits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_beneits_of_functions()


class MyClass:
    varible = "blah"

    def function(self):
        print("This is my message inside a  class")


myobjectx = MyClass()
myobjectx.function()



class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())


phonebook = {}
phonebook["John"] = 938447566
phonebook["Jack"] = 938447564
phonebook["Jill"] = 938447581
print(phonebook)

#initalizing a dictionary
phonebook = {
    "John": 938447566,
    "Jack": 938447564,
    "Jill": 938447581
}

for name, number in phonebook.items():
    print("Phone numbers of %s is %d" % (name, number))
print(phonebook)

phonebook.update({"Jake": 938273443})
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


def collatz_list(n):
    result = []
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result.append(n)
        if n == 1:
            break
    return result

print(collatz_list(7))


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)


word_lengths = [len(word) for word in words if
word != "the"]

print(words)
print(word_lengths)


import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter pattern!")
        else:
            print("Pass")

#Testing you pattern
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)


def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)
    
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            do_stuff_with_number(0)

catch_this()

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split()[1]


#get_last_name()
print("All exceptions caught! Great job!")
print("The actor's name is %s" % get_last_name())

#sets are list with no duplicate entries
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

#to find out which members attended both events
print(a.intersection(b))
print(b.intersection(a))

#to find out which members attended only one event
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#to find out which members atteded only one event and not the other
print(a.difference(b))
print(b.difference(a))

#to recieve a list of all participants
print(a.union(b))

print(a.difference(b))



print(dir(Vehicle))


input("whats your name")
