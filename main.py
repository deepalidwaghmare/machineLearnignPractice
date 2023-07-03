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

# Tricky AND OR
print("Hello" or "World")  # Hello: 1 or 0  will be 1 no matter what is next
print("Hello" and "World")  # World: 1 and 0 = 0,,,1 and 1 = 1 need to confirm the second input

# Slicing in Loop
for i in c[2:9:2]:
    print(i)
for i in c[::-1]:
    print(i)

# Membership operator IN notIn
print('h' in c or 'H' in c)  # False or True = True
print('world' not in c and 'World' not in c)   # True and False = False

