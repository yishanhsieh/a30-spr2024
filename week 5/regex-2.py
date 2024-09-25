import re

input = "Once 9123 upon a 4567 there was a 12389"

print(input)

result = re.findall('\d\d', input)

print(result)

something = "Alex 28"

print(input)

result = re.sub('\d\d', '-', input)

print(result) # ----9

result = re.sub('\d((\d)(\d))\d', r'\1+\3', input)    # Replace a string with a part of itself

print(result)

julianne = "2364523"

result = re.sub('(\d)(\d)', r'\2\1', input) # julianne) # 3246253

print(result)

result = re.sub('(\d)(\d)', r'\1+\2', input) # julianne) # 2+36+45+23

print(result)

result = re.sub('(\d)(\d)', r'int(\1)', julianne) # 51073

print(result)

def add_two(match):
    return str(int(match.group()) + 2)

s = 'Alex 28'
result = re.sub(r'(\d+)', add_two, s)
print(result)

suraj = re.sub(r'(\d)(\d)', lambda m: str(int(m.group(1)) + int(m.group(2))), s)

print(suraj)

linjun = "12345"

suraj = re.sub(r'(\d)(\d)', lambda m: m.group(2) + m.group(1), linjun)
                #                     \2           \1

print(suraj) # 21435

text = "I am here."

text = re.sub('(\w)', r'(\1)', text)

print(text) # (I) (a)(m) (h)(e)(r)(e).