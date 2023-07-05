# Day 1

# Indexing and String Operators
c = str("Hello World")
print("+ve Indexing: 7", c[7])
print("-ve Indexing: -5", c[-5])
print("First 5 letters:", c[0:7])
print("Last 5 letters:", c[4:])
print("First 4 letters:", c[:4])
print("Skip letters:", c[0:7:3])
# Reverse String in Python
print("Reverse String", c[::-1])
# Str is immutable but del c can be used
print(c * 4)

# lexicographical comparison in alphabets a<b A<a
print("kol" < "Kol")
print("hello" and "world")
print("" and "Hello")  # Empty String = false and Non-Empty String = true
print("" or "Hello")
# Membership operator IN notIn
print('h' in c or 'H' in c)  # False or True = True
print('world' not in c and 'World' not in c)  # True and False = False
# **Tricky AND OR
print("Hello" or "World")  # Hello: 1 or 0  will be 1 no matter what is next
print("Hello" and "World")  # World: 1 and 0 = 0,,,1 and 1 = 1 need to confirm the second input

# Slicing in Loop
for i in c[2:9:2]:
    print(i)
for i in c[::-1]:
    print(i)

# String Len, Max, Min, Sorted
print(len(c), max(c), min(c), sorted(c), sorted(c, reverse=True))
# String Capitalize/Title/Upper/Lower/Swapcase
print(c.title(), c.upper(), c.capitalize(), c.swapcase(), c.count('l'), c.find('w'), c.index('rld'))
print("Ends with 'ld':", c.endswith('ld'), "Start with 'ell':", c.startswith('ell'))
# **Format string
print("I like {1} for {0} hrs a day".format('coding', 9))  # 0 and 1 are positions
print("I like {hobby} for {duration} hrs a day".format(hobby='coding', duration=9))
# Validations
print("alphanumeric:", c.isalnum(), "isalpha", "HELLO".isalpha(), "ValidString", "HelloWorld".isidentifier())
# Split and Join
print("Covert String to List", c.split(), c.split(" "))
print("Joint:", "".join(['Hel', 'l', 'o Worl', 'd']))
print("     Name     ".strip())  # Used to make sure only correct string is taken without spaces

# # ##List###
List = [0, 1, 2, 3, 4, 5, [4, 5, 2, [3, 9]]]
print(List[-1][-1][0])
print("Reverse List", List[::-1])
# **Append and Extend
print("Append:", List.append([100, 300]), List, "Extend", List.extend([500, 800]), List)
print("Insert 4000", List.insert(4, [4000, 'goa']), List)

# Covert String first letter capital
L1 = "who are you?"
L2 = []
for i in L1.split():
    L2.append(i.capitalize())
print(" ".join(L2))
# Separating String from special character
L1 = "deepalidwaghmare@yahoo.com"
print(L1.split('@'))
for i in L1.split('@'):
    L2.append(i)
print(L2[3])
print(L1[:L1.find('@')])  # single line code
# Remove duplicate in List
L1 = [1, 1, 1, 2, 2, 3, 3, 3, 3]
L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)

# ###Tuples####  Create, Access, Edit ,Add, Delete, Operations, Functions
# Create Tuple
T = ('Goa', 1, 3, 4, 5)  # Tuples are immutable Edit and Del element cannot be possible
print(T[2:4])  # Tuples if declared with single element cannot be considered tuple
# Tuples are read-only data type
