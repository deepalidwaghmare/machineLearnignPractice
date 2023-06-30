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
print("kol"<"Kol")
