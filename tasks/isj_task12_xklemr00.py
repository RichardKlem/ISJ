# minitask 1.2
# expected output ['resource load failed', 'flow failed']
import re
text = '''
INFO 2019-02-17 12:13:44 resource load failed
INFO 2019-02-18 22:09:17 authentication failed
INFO 2019-02-18 10:55:48 data received
INFO 2019-02-19 19:53:31 flow failed
'''
pattern = '''
    \w+                 # failure type
    \s                  # a white character
    [\d-]+              # date such as 2019-02-21
    \s                  # a white character
    [\d:]+              # time such as 21:15:06
    \s                  # a white character
    (.*[d|w]\sfailed)        # failure description
'''
print(re.findall(pattern,text, re.VERBOSE))

#pridal jsem [d|w]