# minitask 1.3
# change the last du to DU
# expected output ['resource load failed', 'flow failed']import re
import re
pattern = re.compile(r'du(?!.*du)')
text = ['du du du', 'du po ledu', 'dopředu du', 'i dozadu du', 'dudu dupl']
for row in text:
    print(re.sub(pattern, 'DU', row))