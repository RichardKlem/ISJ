import re
text = '<b>foo</b> and <i>so on</i>'
print(re.findall(r'<(.*?)>', text))