import datetime
a = "{[()]}"
stack = []
mapping = {')':'(', ']':'[', '}':'{'}

for char in a:
    if char in mapping.values():
        stack.append(char)
    elif char in mapping:
        if not stack or stack.pop() != mapping[char]:
            print("not ok")
date = datetime.datetime.now()    
print(f"This is okay akash jaiswal: {date}")
