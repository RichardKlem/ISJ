# minitask 1.4
# strings/lines that contain _words_ David and Pavel and
# do not contain neither _words_ Petr nor Jan
# expected output:
# Iva Pavel David Ada
# Pavel David Jansen
import re

texts = ['David Petr', 'Iva Pavel David Ada',
         'Davidson Pavelek', 'Pavel David Jansen', 'Jan Patocka',
         'Petra Novakova', 'Janous Petrarka', ]
for text in texts:
    if re.search(r'^(?!.*(Petr)).*$', text):
        print(text)
