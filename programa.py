import math
import os
import sys
import re
import json
from datetime import datetime



print(math.pow(2,3))
# print(os.getcwd())
# os.makedirs("example")
# print("directory created")
# os.removedirs("example")
# print("done deleted!...")

print(sys.version)

print(sys.argv)


text="Hello world!!"
pattern="world"

if re.search(pattern,text):
    print("pattern found!")
else:
    print("pattern not found! ")


data={"name":"Alice","age":26}
json_data=json.dumps(data)
print(json_data)

python_data=json.loads(json_data)
print(python_data)


now=datetime.now()
print(now)

formatted_date=now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)