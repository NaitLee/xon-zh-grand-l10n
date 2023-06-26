
from sys import stdin, stdout

header = '''
msgid ""
msgstr ""
"Content-Transfer-Encoding: 8bit\\n"
"Content-Type: text/plain; charset=UTF-8\\n"

'''

start = False
concatenate = False

while line := stdin.readline():
    if line == 'msgstr ""\n':
        if not start:
            while stdin.readline() != '\n':
                pass
            stdout.write(header)
            start = True
            continue
        concatenate = True
        stdout.write('msgstr "')
        continue
    if not start:
        continue
    if concatenate:
        if line == '\n':
            stdout.write('"\n\n')
            concatenate = False
        else:
            stdout.write(line[1:-2])
        continue
    else:
        stdout.write(line)

if concatenate:
    stdout.write('"\n')
