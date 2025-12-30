s1 = "hello world"
s2= "python"

print (len(s1))          # Output: 11
print (s1.upper())       # Output: "HELLO WORLD"
print (s2.capitalize())  # Output: "Python"
print (s1.replace("world", "there"))  # Output: "hello there"
print (s1.split())       # Output: ['hello', 'world']
print (s1 + " from " + s2)  # Output: "hello world from python"
print (s1[0:5])          # Output: "hello"
print (s2[-1])           # Output: "n"
print (s1.find("world")) # Output: 6
print (s1.startswith("hello"))  # Output: True
print (s2.endswith("on"))      # Output: True
print (s1.count("l"))    # Output: 3
print (s1.isalpha())     # Output: False
print (s2.islower())     # Output: True
print (s1.strip())       # Output: "hello world"
print (s1.index("o"))    # Output: 4
print (s1.center(20))    # Output: "     hello world     "
print (s2.zfill(10))     # Output: "0000python"
print (s1.swapcase())   # Output: "HELLO WORLD"
print (s1.translate(str.maketrans("hel", "123")))  # Output: "123lo wor1d"
print (s2.encode())     # Output: b'python'
print (s1.isprintable()) # Output: True
print (s2.partition("th")) # Output: ('py', 'th', 'on')
print (s1.rfind("o"))   # Output: 7
print (s2.rsplit("o"))  # Output: ['pyth', 'n']
print (s1.title())      # Output: "Hello World"
print (s2.casefold())   # Output: "python"
print (s1.expandtabs()) # Output: "hello world"
print (s2.encode('utf-8')) # Output: b'python' 
print (s1.isidentifier()) # Output: False
print (s2.ljust(10))    # Output: "python    "
print (s1.rjust(15))    # Output: "     hello world"
print (s2.partition("y")) # Output: ('p', 'y', 'thon')

s = s1 + s2
print(s)
ss = s1 + " " + s2
print(ss)