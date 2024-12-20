# String initialization
text = "Hello World"
num_text = "12345"
space_text = "   "
mixed_text = "Python3"

# 1. Basic String Manipulation
print(text.upper())        # Output: HELLO WORLD
print(text.lower())        # Output: hello world
print(text.capitalize())   # Output: Hello world
print(text.title())        # Output: Hello World
print(text.swapcase())     # Output: hELLO wORLD

# 2. Checking String Properties
print(text.isalpha())      # Output: False (contains space)
print(num_text.isdigit())  # Output: True
print(mixed_text.isalnum())# Output: True
print(space_text.isspace())# Output: True
print(text.islower())      # Output: False
print(text.isupper())      # Output: False

# 3. Searching and Replacing
print(text.find("World"))  # Output: 6
print(text.index("World")) # Output: 6
print(text.replace("World", "Python"))  # Output: Hello Python
print(text.count("l"))     # Output: 3

# 4. Splitting and Joining
csv = "a,b,c"
print(csv.split(","))      # Output: ['a', 'b', 'c']
print(csv.rsplit(",", 1))  # Output: ['a,b', 'c']
multiline = "line1\nline2"
print(multiline.splitlines()) # Output: ['line1', 'line2']
words = ["Python", "is", "fun"]
print(" ".join(words))     # Output: Python is fun

# 5. Stripping Characters
strip_text = "  hello  "
print(strip_text.strip())  # Output: hello
print(strip_text.lstrip()) # Output: hello  
print(strip_text.rstrip()) # Output:   hello

# 6. Formatting Strings
name = "John"
print("Hello, {}!".format(name)) # Output: Hello, John!
print("42".zfill(5))       # Output: 00042

# 7. String Alignment
print(text.center(15))     # Output: '  Hello World   '
print(text.ljust(15))      # Output: 'Hello World    '
print(text.rjust(15))      # Output: '    Hello World'

# 8. Encoding and Decoding
encoded = text.encode("utf-8")
print(encoded)             # Output: b'Hello World'
print(encoded.decode("utf-8"))  # Output: Hello World

# 9. Checking Prefixes and Suffixes
print(text.startswith("Hello")) # Output: True
print(text.endswith("World"))   # Output: True
