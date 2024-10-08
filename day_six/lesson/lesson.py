import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
print(result)

result = re.findall(r'AV', text)
print(result)

result = re.search(r'Analytics', text)
print(result)

result = re.search(r'AV', text)
print(result)

result = re.findall(r'A[a-zA-Z]+', text)
print(result)

result = re.split(r'i', text)
print(result)

result = re.sub(r' ', r', ', text)
print(result)

result = re.sub(r'[aiyuoe]', r'#', text)
print(result)

result = re.sub(r'[A-Z]', r'&', text)
print(result)

with open(file='test_regs.txt', mode='r', encoding='utf-8') as file:
    content = file.read()
    print(content)

    mega_list = re.findall(r'\+996 (?:55\d|99[7-905])[0-9 ]{9}', content)
    print(f'mega_list ({len(mega_list)}): {mega_list}')

    beeline_list = re.findall(r'\+996 (?:77\d|22[0-57])[0-9 ]{9}', content)
    print(f'beeline_list ({len(beeline_list)}): {beeline_list}')

    o_list = re.findall(r'\+996 (?:50[0-27-945]|70\d)[0-9 ]{9}', content)
    print(f'o_list ({len(o_list)}): {o_list}')
